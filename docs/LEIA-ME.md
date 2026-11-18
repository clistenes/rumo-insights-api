# COPSOQ II-Br — arquivo de definição e casos de teste

Pacote inicial do cálculo da Rumo Insights. Substitui o cadastro de questionário
pergunta a pergunta: o instrumento é um arquivo, e um único motor o lê.

Gerado em 17/11/2026, a partir do protótipo Rumo Insights e das regras da
*Especificação da plataforma — COPSOQ II-Br e NR-1* (27/10/2026).

## Os arquivos

| Arquivo | O que é |
| --- | --- |
| `copsoq_ii_br.json` | O instrumento: 7 escalas com pontuação, 40 itens, 23 dimensões, 4 perguntas abertas, regras de cálculo, cortes de classificação, regras de qualidade e de privacidade |
| `casos_de_teste.json` | 21 casos com respostas conhecidas e resultado esperado |
| `verificar_calculo.py` | Motor de cálculo de referência e verificador dos casos |
| `respondentes_ficticios.csv` | 60 respondentes fictícios do protótipo, com setor, turno, liderança e sexo, para popular o ambiente de teste |

## Como rodar

```
python3 verificar_calculo.py
```

Não precisa instalar nada. Em 18/11/2026, os 21 casos passaram.

Esse comando deve rodar a cada alteração na plataforma. Se um caso falhar, o
cálculo mudou: ou foi erro, ou foi uma decisão técnica que precisa ser registrada
e o caso atualizado junto.

## As regras que estão implementadas

1. Cada item é normalizado pelo máximo da sua própria escala e a dimensão vira
   uma pontuação de 0 a 100.
2. Os valores das opções já estão na direção final no arquivo. O item 1B usa a
   escala invertida e **não** deve ser invertido outra vez. O caso C02 existe
   justamente para pegar essa inversão dupla.
3. A dimensão só é calculada se pelo menos metade dos seus itens foi respondida.
4. Zero é resposta válida. Ausência de resposta nunca vale zero nem o valor do meio.
5. Arredondamento para 2 casas decimais antes de classificar.
6. Cortes por tercis, 33,33 e 66,67, do Manual COPSOQ II. A direção da dimensão
   decide a cor: em risco, pontuação alta é vermelha; em proteção, é verde.
7. Exposição é lida item a item, com a frequência e a origem. Qualquer resposta
   diferente de "Não" conta como relato. Os quatro itens nunca são somados em um
   índice único: a validação brasileira encontrou consistência baixa nesse bloco
   (alfa = 0,54).
8. Recorte filtrado com menos de 5 pessoas não produz resultado, nem na tela nem
   na exportação.
9. Adesão abaixo de 50% gera alerta de cautela.
10. Questionário com a mesma resposta em todos os itens é marcado para revisão
    humana, nunca excluído automaticamente.

## As duas estruturas do instrumento

O arquivo carrega as duas, e elas convivem: item, 23 dimensões, 11 dimensões
validadas, 7 domínios.

- **23 dimensões** da versão curta internacional. É o que a primeira versão
  apresenta, e é o que a própria tese usou ao aplicar o instrumento numa empresa.
- **11 dimensões validadas em 7 domínios**, da validação brasileira (Gonçalves,
  UFSCar, 2019, Tabelas 2 e 3). Cada dimensão validada é a união exata de
  dimensões das 23, com alfa de Cronbach publicado. O verificador confere essas
  uniões.

Regras de apresentação, gravadas no arquivo:

- **O domínio é título, sem pontuação própria.** Em "Saúde e bem-estar" e em
  "Interface trabalho-indivíduo" a análise fatorial encontrou dois fatores
  distintos; somá-los contraria o que o estudo achou.
- **A dimensão validada pode ter pontuação agregada**, porque tem consistência
  interna publicada. É o caso de "Burnout e estresse" (alfa 0,87), que permite
  apresentar esgotamento e estresse num número só.
- **Comportamentos ofensivos nunca recebe pontuação agregada** (alfa 0,54), e a
  própria tese registra que esse domínio não é pontuado por soma como os demais.

## Relato de violência física ou assédio sexual: alerta, não piso

Um relato desses não muda o nível de risco por si só. A NR-1 não prescreve
matriz nem nível; quem define o método é a organização, que precisa declarar os
critérios. E relato não é ocorrência apurada: forçar "Alto" seria tratar um
relato anônimo como fato comprovado.

O que a plataforma faz, então:

1. **Alerta de apuração imediata** no topo dos resultados, nomeando o tipo de
   relato, a frequência e a origem, sem identificar ninguém.
2. **Ação obrigatória no plano**, com prazo de 15 dias, indicador "apuração
   concluída e registrada, com medidas adotadas", e origem marcada como
   obrigatória por alerta. Entra por um clique e fica na trilha de auditoria.
3. **O perigo aparece no inventário como "sob apuração"**, qualquer que seja o
   nível calculado. O nível só muda depois da conclusão, com evidência anexada.
4. **A tela declara o limite**: nenhum dado dessa origem pode embasar medida
   disciplinar, porque é anônimo e não apurado.

A matriz continua íntegra: probabilidade pela adesão e pela distribuição,
severidade pelo tipo de perigo. Nada é empurrado para cima por regra.

Hoje a regra vale para assédio sexual (item 20) e eventos violentos (item 22).
Estender para ameaças de violência (21) e assédio moral (23) é decisão da
Rosalina.

## Uma decisão pendente

- **Recorte mínimo de pessoas.** Está em 5, herdado do sistema antigo, marcado no
  arquivo como "a confirmar". É você quem decide.

## Escala: soma ou 0 a 100

A tese pontua cada dimensão pela soma dos itens, com amplitudes diferentes
conforme o número de questões (0 a 24, 0 a 16, 0 a 6, 0 a 4, 0 a 3). A escala de
0 a 100 usada aqui vem do manual português (Silva et al.), de onde também vêm os
tercis. A conversão é direta e preserva a ordem. O verificador devolve as duas,
`soma` e `pontuacao`. A metodologia do relatório deve declarar qual delas é usada.

## Duas observações técnicas

- **Os textos dos itens vieram do protótipo, não da publicação oficial.** Antes de
  usar com clientes, confira item por item contra a versão brasileira de
  referência. É o único ponto do pacote que depende de uma fonte que eu não tive.
- **Satisfação no trabalho não alcança a faixa amarela.** É uma dimensão de um só
  item, com quatro opções: os resultados possíveis são 0, 33,33, 66,67 e 100.
  Pelos cortes dos tercis, nenhum cai na faixa do meio. Não é erro de cálculo, é
  propriedade do instrumento, mas convém explicar isso no relatório.

## Para quem for programar, ou para a IA que for gerar o código

O `verificar_calculo.py` é a referência. O cálculo na plataforma deve viver em um
único lugar, ler tudo do JSON e não repetir cortes ou pontuações em nenhuma tela.
Incluir outro instrumento, como o HSE, é acrescentar outro arquivo no mesmo
formato, com seus próprios casos de teste, sem reprogramar o motor.
