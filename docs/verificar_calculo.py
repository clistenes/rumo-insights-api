#!/usr/bin/env python3
"""
Rumo Insights — motor de cálculo de referência do COPSOQ II-Br e verificador dos casos de teste.

Uso:
    python3 verificar_calculo.py

Lê copsoq_ii_br.json e casos_de_teste.json, calcula e compara com o resultado esperado.
Serve a dois propósitos: provar que as regras estão corretas e servir de referência
para quem (ou qual IA) for implementar o cálculo na plataforma.

Regras implementadas, conforme a especificação:
  1. Cada item é normalizado pelo máximo da sua própria escala: valor / valor_maximo.
  2. Pontuação da dimensão = média dos itens respondidos x 100, na escala 0 a 100.
  3. Os valores das opções já estão na direção final. O item 1B usa escala invertida
     e NÃO deve ser invertido outra vez.
  4. A dimensão só é calculada se pelo menos metade dos seus itens foi respondida.
  5. Zero é resposta válida. Ausência de resposta nunca vale zero.
  6. Arredondamento para 2 casas decimais ANTES de classificar.
  7. Cortes por tercis: 33,33 e 66,67. A direção da dimensão decide a cor.
  8. Exposição é item a item: qualquer frequência diferente de "Não" é relato.
     Nunca agregar os itens de exposição em um índice único.
  9. Recorte filtrado abaixo do mínimo de pessoas não produz resultado.
"""
import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))


def carregar(nome):
    with open(os.path.join(BASE, nome), encoding='utf-8') as f:
        return json.load(f)


# ----------------------------------------------------------------- motor

def pontuacao_dimensao(definicao, dimensao_id, respostas):
    """Pontuação 0–100 de uma dimensão para uma pessoa."""
    dim = next(d for d in definicao['dimensoes'] if d['id'] == dimensao_id)
    itens = {i['id']: i for i in definicao['itens']}
    total = len(dim['itens'])
    proporcoes = []
    for item_id in dim['itens']:
        valor = respostas.get(item_id)
        if valor is None:
            continue
        maximo = itens[item_id]['valor_maximo']
        proporcoes.append(valor / maximo)

    usados = len(proporcoes)
    minimo = definicao['regras_calculo']['minimo_proporcao_itens_respondidos']
    if total == 0 or usados / total < minimo:
        return {'pontuacao': None, 'faixa': None, 'rotulo': None,
                'itens_usados': usados, 'itens_total': total, 'disponivel': False}

    casas = definicao['escala_resultado']['casas_decimais']
    pontuacao = round(sum(proporcoes) / usados * 100, casas)
    faixa, rotulo = classificar(definicao, dim['direcao'], pontuacao)
    return {'pontuacao': pontuacao, 'faixa': faixa, 'rotulo': rotulo,
            'itens_usados': usados, 'itens_total': total, 'disponivel': True}


def classificar(definicao, direcao, pontuacao):
    """Cor e rótulo de uma pontuação já arredondada."""
    if pontuacao is None:
        return None, None
    regras = definicao['classificacao'][direcao]['faixas']
    if direcao == 'risco':
        verde, amarelo, vermelho = regras[0], regras[1], regras[2]
        if pontuacao <= verde['ate']:
            return 'verde', verde['rotulo']
        if pontuacao <= amarelo['ate']:
            return 'amarelo', amarelo['rotulo']
        return 'vermelho', vermelho['rotulo']
    if direcao == 'protecao':
        verde, amarelo, vermelho = regras[0], regras[1], regras[2]
        if pontuacao >= verde['de']:
            return 'verde', verde['rotulo']
        if pontuacao >= amarelo['de']:
            return 'amarelo', amarelo['rotulo']
        return 'vermelho', vermelho['rotulo']
    if direcao == 'exposicao':
        sem, com = regras[0], regras[1]
        return ('verde', sem['rotulo']) if pontuacao == 0 else ('vermelho', com['rotulo'])
    raise ValueError('direção desconhecida: ' + direcao)


def exposicao_item(definicao, item_id, resposta, origens=None):
    """Um item de exposição, lido isoladamente."""
    if resposta is None:
        return {'faixa': None, 'relato': None, 'origens': origens or []}
    relato = resposta > 0
    rotulos = definicao['classificacao']['exposicao']['faixas']
    return {'faixa': 'vermelho' if relato else 'verde',
            'rotulo': rotulos[1]['rotulo'] if relato else rotulos[0]['rotulo'],
            'relato': relato,
            'frequencia': rotulo_da_resposta(definicao, item_id, resposta),
            'origens': origens or []}


def rotulo_da_resposta(definicao, item_id, valor):
    item = next(i for i in definicao['itens'] if i['id'] == item_id)
    for opcao in definicao['escalas'][item['escala']]['opcoes']:
        if opcao['valor'] == valor:
            return opcao['rotulo']
    return None


def resultado_grupo(definicao, dimensao_id, respondentes, recorte_minimo=None, recorte_filtrado=True):
    """Distribuição e média de um grupo, com proteção de recorte pequeno."""
    if recorte_minimo is None:
        recorte_minimo = definicao['privacidade']['recorte_minimo_pessoas']
    n = len(respondentes)
    if recorte_filtrado and n < recorte_minimo:
        return {'protegido': True, 'n': n, 'media': None, 'faixa_media': None,
                'distribuicao': None,
                'mensagem': 'Recorte protegido: menos de %d pessoas.' % recorte_minimo}

    pontuacoes = []
    contagem = {'verde': 0, 'amarelo': 0, 'vermelho': 0}
    for respostas in respondentes:
        r = pontuacao_dimensao(definicao, dimensao_id, respostas)
        if not r['disponivel']:
            continue
        pontuacoes.append(r['pontuacao'])
        contagem[r['faixa']] += 1

    if not pontuacoes:
        return {'protegido': False, 'n': n, 'media': None, 'faixa_media': None,
                'distribuicao': None, 'mensagem': 'Sem pontuação utilizável neste recorte.'}

    casas = definicao['escala_resultado']['casas_decimais']
    media = round(sum(pontuacoes) / len(pontuacoes), casas)
    dim = next(d for d in definicao['dimensoes'] if d['id'] == dimensao_id)
    faixa, _ = classificar(definicao, dim['direcao'], media)
    validos = len(pontuacoes)
    distribuicao = {k: round(v / validos * 100, casas) for k, v in contagem.items()}
    return {'protegido': False, 'n': n, 'respondentes_com_pontuacao': validos,
            'media': media, 'faixa_media': faixa, 'distribuicao': distribuicao}


def adesao(definicao, respondentes, trabalhadores):
    casas = definicao['escala_resultado']['casas_decimais']
    if not trabalhadores:
        return {'adesao': None, 'alerta': None}
    valor = round(respondentes / trabalhadores * 100, casas)
    limite = definicao['regras_de_qualidade']['alerta_adesao_abaixo_de']
    return {'adesao': valor, 'alerta': valor < limite}


def marcar_para_revisao(definicao, respostas):
    """Respostas iguais em todos os itens: marcar, nunca excluir automaticamente."""
    pontuaveis = [i['id'] for i in definicao['itens']]
    valores = [respostas[i] for i in pontuaveis if respostas.get(i) is not None]
    identicas = len(valores) == len(pontuaveis) and len(set(valores)) == 1
    return {'marcar_para_revisao': identicas, 'excluido_automaticamente': False}


# ----------------------------------------------------------------- verificação

def compara(esperado, obtido):
    faltas = []
    for chave, valor in esperado.items():
        atual = obtido.get(chave)
        if isinstance(valor, float) and isinstance(atual, (int, float)):
            ok = abs(valor - atual) < 0.005
        else:
            ok = valor == atual
        if not ok:
            faltas.append('%s: esperado %r, obtido %r' % (chave, valor, atual))
    return faltas


def executa(definicao, caso):
    tipo = caso['tipo']
    if tipo == 'dimensao':
        return pontuacao_dimensao(definicao, caso['dimensao'], caso['respostas'])
    if tipo == 'exposicao':
        return exposicao_item(definicao, caso['item'], caso['resposta'], caso.get('origens'))
    if tipo == 'grupo':
        return resultado_grupo(definicao, caso['dimensao'], caso['respondentes'],
                               caso.get('recorte_minimo'))
    if tipo == 'adesao':
        return adesao(definicao, caso['respondentes'], caso['trabalhadores'])
    if tipo == 'qualidade':
        respostas = {i['id']: caso['respostas_todos_itens'] for i in definicao['itens']}
        return marcar_para_revisao(definicao, respostas)
    if tipo == 'estrutura':
        itens = {i['id'] for i in definicao['itens']}
        escalas = set(definicao['escalas'])
        exposicao = [d for d in definicao['dimensoes'] if d['direcao'] == 'exposicao']
        orfaos = [i for i in itens
                  if not any(i in d['itens'] for d in definicao['dimensoes'])]
        inexistentes = [d['id'] for d in definicao['dimensoes']
                        if any(i not in itens for i in d['itens'])]
        sem_escala = [i['id'] for i in definicao['itens'] if i['escala'] not in escalas]
        return {
            'total_itens': len(itens),
            'total_dimensoes': len(definicao['dimensoes']),
            'dimensoes_exposicao': [d['id'] for d in exposicao],
            'itens_por_dimensao_exposicao': max(len(d['itens']) for d in exposicao),
            'itens_orfaos': len(orfaos),
            'dimensoes_com_item_inexistente': len(inexistentes),
            'escalas_inexistentes': len(sem_escala),
        }
    raise ValueError('tipo de caso desconhecido: ' + tipo)


def main():
    definicao = carregar('copsoq_ii_br.json')
    testes = carregar('casos_de_teste.json')

    print('Rumo Insights — verificação do cálculo do COPSOQ II-Br')
    print('Instrumento: %s | arquivo %s' % (definicao['instrumento']['nome'],
                                            definicao['instrumento']['versao_arquivo']))
    print('Itens: %d | Dimensões: %d | Escalas: %d\n'
          % (len(definicao['itens']), len(definicao['dimensoes']), len(definicao['escalas'])))

    falhas = 0
    for caso in testes['casos']:
        obtido = executa(definicao, caso)
        faltas = compara(caso['esperado'], obtido)
        if faltas:
            falhas += 1
            print('FALHOU  %s — %s' % (caso['id'], caso['titulo']))
            for f in faltas:
                print('        %s' % f)
        else:
            resumo = ''
            if 'pontuacao' in obtido and obtido.get('pontuacao') is not None:
                resumo = '%.2f (%s)' % (obtido['pontuacao'], obtido['faixa'])
            elif obtido.get('media') is not None:
                resumo = 'média %.2f (%s)' % (obtido['media'], obtido['faixa_media'])
            elif obtido.get('protegido'):
                resumo = 'protegido'
            elif obtido.get('adesao') is not None:
                resumo = '%.2f%%' % obtido['adesao']
            print('ok      %s — %-45s %s' % (caso['id'], caso['titulo'][:45], resumo))

    total = len(testes['casos'])
    print('\n%d de %d casos passaram.' % (total - falhas, total))
    if definicao['dominios_validados']['situacao'] == 'pendente':
        print('Pendente: mapeamento dos 7 domínios validados (ver copsoq_ii_br.json).')
    if 'a confirmar' in definicao['privacidade']['situacao_recorte_minimo']:
        print('Pendente: confirmar o recorte mínimo de %d pessoas.'
              % definicao['privacidade']['recorte_minimo_pessoas'])
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())
