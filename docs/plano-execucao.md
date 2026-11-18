# Plano de execução do Rumo Insights

**Referência do planejamento:** 18/11/2026.  
**Objetivo:** permitir que a Rumo e uma empresa cliente conduzam uma avaliação psicossocial completa, da configuração da coleta à devolutiva, à emissão do relatório técnico e ao acompanhamento das ações com evidências.

O plano cobre os três repositórios Git independentes, `api`, `app` e `bd`. O HTML define o escopo funcional. O print de planejamento orienta a primeira entrega. As decisões confirmadas abaixo prevalecem sobre os comportamentos de demonstração. O documento descreve trabalho a implementar.

## 1. Decisões confirmadas

| Tema | Regra de produto |
|---|---|
| Empresas clientes | Cada pessoa jurídica possui cadastro próprio, usuários administrativos, avaliações, dados e documentos isolados. Um admin global da Rumo pode acessar qualquer empresa e suspender ou reativar seu acesso por inadimplência. A cobrança é externa na primeira versão. |
| Trabalhadores | Participam anonimamente, sem cadastro e sem login permanente. A empresa gera convites individuais em lote e os distribui por seu próprio canal. Cada convite tem um link e um QR Code que representa o mesmo link. |
| Aderência ao HTML | O HTML já contempla códigos individuais de uso único e também um código coletivo. Implementar exclusivamente a modalidade individual. A administradora da empresa precisa de permissão para emitir e revogar convites. No HTML, o modelo de perfil de RH tem apenas leitura na área de ciclo. |
| Unidade de controle | Cada convite permite uma submissão. A plataforma desconhece a identidade de quem recebeu o convite. Distribuir um único convite por pessoa é responsabilidade da empresa. |
| Fiscalização | Manter somente o auditor-fiscal externo, com acesso temporário, revogável, de leitura e restrito à empresa. A responsável técnica da Rumo revisa e assina o relatório. |
| Privacidade | Publicar cada indicador somente quando houver pelo menos cinco respondentes válidos para aquele indicador, inclusive no total da empresa. Com menos de cinco, disponibilizar o acompanhamento operacional da coleta. Aplicar o mesmo critério a todas as formas de entrega de resultados. |
| Resumo do instrumento | Implementar os 23 resultados operacionais definidos no pacote. O painel que organiza o instrumento brasileiro em sete domínios e 11 dimensões depende da homologação de Rosalina. |

**Primeira entrega.** Cadastro da PJ e dos acessos, instrumento versionado, nova avaliação em quatro passos, coleta móvel anônima, painel de adesão e prazos, resultados com filtros e conclusão, relatório técnico revisado e assinado, inventário, plano de ação tabular, evidências, auditoria e testes automáticos.

**Complementos para cobrir o HTML.** Incluir pasta fiscal completa e dossiê, visão do auditor externo, autorização temporária à consultoria, envio externo de evidências, cronograma, sugestões revisáveis de ações, exportações e comparação entre ciclos. As restrições de acesso devem estar ativas desde a primeira entrega de cada recurso.

**Evoluções posteriores.** Pagamentos online, autoatendimento comercial, parceiros com marca própria, HSE e outros instrumentos, referências por segmento, assistente de RH, envio integrado por WhatsApp e canal de denúncias ficam fora da primeira versão. Os instrumentos legados continuam no sistema atual enquanto forem utilizados.

## 2. Referências e verificações iniciais

| Fonte | Uso na implementação |
|---|---|
| [Protótipo HTML](../../app/docs/prototipo-rumo-insights.html) | Jornada do trabalhador, navegação administrativa, permissões por área, cadastro, cálculo demonstrativo, inventário, avaliação do perigo, ações, evidências, fiscal, relatório, auditoria e identidade visual. O link relativo pressupõe os três clones em pastas irmãs. |
| [LEIA-ME](LEIA-ME.md) e [definição COPSOQ II-Br](copsoq_ii_br.json) | Regras, escalas, itens, dimensões, classificação, origens de exposição, consentimento e perguntas abertas. A versão 1.0.0 reúne sete escalas, 40 itens, 23 dimensões e quatro campos abertos opcionais. |
| [Casos conhecidos](casos_de_teste.json) e [verificador Python](verificar_calculo.py) | Referência executável para a implementação em Go. Na análise inicial, 18 de 18 casos passaram. Executar a partir do diretório que contém os três repositórios com `python3 -B api/docs/verificar_calculo.py`. |
| [Respondentes fictícios](respondentes_ficticios.csv) | Massa integrada de 60 participantes. Operação tem 26, Administrativo 18, Comercial 12 e Manutenção quatro. Usar os quatro setores para verificar tanto a classificação quanto a proteção de grupos pequenos. |
| [Questionário brasileiro curto](copsoq_II_curto_versao_adap_brasil.pdf) | Os 40 enunciados do JSON foram encontrados no texto do PDF após normalizar espaços e ligaturas. Conferir opções, introduções e períodos de referência na homologação. No item 17, as opções vão de 0 a 4 e a legenda informa total até 8. O JSON adota máximo 4, coerente com as opções. Registrar a decisão técnica. |
| [Artigo de adaptação cultural](adaptacao_cultural_copsoq_brasil.pdf) e [tese brasileira](tese_de_doutorado_copsoq_brasil_jsg_final.pdf) | A Tabela 2 do artigo e a correspondente da tese fornecem o agrupamento por domínio, pergunta e fator. Usá-las para preparar o quadro de homologação. Os três agrupamentos de apresentação do HTML têm finalidade visual própria. |

O HTML mantém dados no navegador, usa data fixa e simula autenticação, geração de documentos e algumas integrações. Na finalização do questionário, os textos abertos preenchidos não são copiados para a resposta persistida. Na visualização do relatório, algumas seções em leitura podem ser renderizadas enquanto o texto da interface promete ocultar o rascunho do cliente. Incluir testes específicos para ambas as situações na plataforma real.

### Pergunta para encaminhar à psicóloga Rosalina

> Rosalina, precisamos da sua orientação sobre como apresentar os resultados do COPSOQ às empresas. O questionário tem 40 perguntas e hoje conseguimos mostrar 23 aspectos do trabalho separadamente. Por exemplo, a empresa pode ver se a dificuldade está no volume de tarefas, no ritmo ou nas exigências emocionais. O estudo brasileiro também organiza essas perguntas em sete grandes temas, com 11 dimensões.
>
> Podemos lançar a primeira versão com os 23 aspectos e deixar o resumo em sete temas para depois da sua revisão? Quando incluirmos esse resumo, você prefere que cada tema seja um título que reúne os resultados relacionados ou quer que alguma dimensão tenha uma pontuação própria?
>
> Por exemplo, em “Saúde e bem-estar”, podemos mostrar saúde geral, esgotamento e estresse lado a lado. Caso queira também uma pontuação conjunta para esgotamento e estresse, pode indicar a referência e dar um exemplo de como gostaria que ela fosse calculada e explicada ao cliente?
>
> Para atenção sexual indesejada, ameaças, violência física e bullying, propomos manter os quatro resultados separados, para que um tipo de ocorrência não esconda outro. Você concorda?

Quando houver resposta, registrar a decisão, referência, responsável e data. Se houver novo cálculo, documentar itens, direção, tratamento de respostas ausentes, valores esperados e interpretação antes de ativar o painel. Essa pendência permite avançar com a coleta e o detalhamento dos 23 resultados.

## 3. Arquitetura e repositórios

Versões estáveis consultadas em 18/11/2026. Na implementação no outro PC, conferir novamente as versões oficiais, registrar as escolhidas e fixar versões de compilador, dependências e imagens.

| Componente | Escolha e justificativa |
|---|---|
| Backend | Go 1.27.4, `net/http`, roteador `chi/v5` e driver `pgx`. O chi integra grupos de rotas e middleware de identidade, empresa e permissões aos tipos HTTP da biblioteca padrão. Usar uma aplicação modular e um worker com a mesma base de código. [Versões do Go](https://go.dev/doc/devel/release) · [chi](https://github.com/go-chi/chi) |
| Frontend | Next.js 16.4.6, TypeScript, App Router e Bootstrap com tema próprio. Usar exportação estática no Amplify e carregar dados privados pela API após autenticação. A documentação de SSR gerenciado da AWS consultada cobria Next.js até a versão 15. [Release do Next.js](https://github.com/vercel/next.js/releases/tag/v16.4.6) · [Exportação estática](https://nextjs.org/docs/app/guides/static-exports) · [Suporte do Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/ssr-amplify-support.html) |
| Banco | PostgreSQL 18.7, em contêiner no desenvolvimento e na instância Lightsail de produção. Na consulta, a versão 19 estava em RC. Aplicar migrations SQL, chaves compostas e políticas de segurança por linha. [Versões oficiais do PostgreSQL](https://www.postgresql.org/support/versioning/) |
| Arquivos | Proposta de armazenamento privado em S3 para evidências, atas, relatórios e exportações. O PostgreSQL armazena metadados, chave do objeto, versão e hash. No desenvolvimento, usar armazenamento privado local ou compatível com S3. |
| Processamento assíncrono | Executar geração de PDFs, dossiês, exportações, verificação de anexos e rascunhos de IA em worker Go. A primeira versão pode manter a fila de tarefas no PostgreSQL, com estado, tentativas, idempotência e retomada após falha. |

| Repositório | Entregas |
|---|---|
| `bd` | Migrations, constraints, índices, políticas de acesso, usuários técnicos, seed sintético, backup, restauração e Compose de integração referenciando `../api` e `../app`. |
| `api` | OpenAPI versionado, autenticação, regras de negócio, coleta, motor de cálculo, publicação, relatórios, auditoria e worker. Os documentos de referência permanecem em `docs/`. |
| `app` | Páginas públicas e privadas em Next.js, tema responsivo, cliente tipado a partir do OpenAPI, gráficos, tabelas acessíveis e testes de jornada. O HTML permanece como referência funcional. |

Mudanças que atravessam repositórios seguem a ordem de migration compatível, API compatível e frontend. Registrar a combinação de versões homologadas. Executar remoções de campos antigos depois da transição de todos os consumidores.

## 4. Identidade, permissões e isolamento

| Ator | Permissões |
|---|---|
| Admin global da Rumo | Acessa qualquer empresa, gerencia equipe, contas e planos, suspende e reativa clientes. Auditar empresa selecionada, operador e ação. A assinatura do relatório exige designação técnica. |
| Responsável técnica | Revisa resultados, confirma metodologia e ajustes, aprova seções e assina versões. Registrar vínculo, nome e registro profissional. |
| Consultoria | Atua nas empresas atribuídas. Para plano, evidências e pasta fiscal, precisa de autorização do cliente por área. Usar 30 dias como duração inicial proposta no HTML, com revogação antecipada. |
| Suporte e comercial | Suporte atua na operação da conta. Comercial consulta dados cadastrais, plano e situação contratual. Restringir acesso a informações de avaliação conforme a atribuição. |
| Administradora da PJ | Administra a própria empresa, seus usuários, convites, acessos fiscais e autorizações à Rumo. Pode delegar operações por área. |
| Usuários da PJ | Partir dos perfis RH, SST, Qualidade de Vida, Gestor e Diretoria. Configurar cada área com níveis sem acesso, visualizar ou editar. |
| Auditor-fiscal externo | Consulta resultados agregados, método, instrumento, versões emitidas, inventário, plano, evidências, pasta fiscal e trilha autorizada. Acesso restrito à empresa e válido por sete dias por padrão. |
| Participante | Responde pelo convite individual. A empresa apresenta posteriormente a devolutiva global publicável. |
| Responsável por evidência | Recebe link temporário e de uso único para enviar o documento de uma ação específica. |

- **Sessões administrativas.** Usar hash seguro de senha, JWT de acesso curto mantido em memória, refresh token rotativo revogável em cookie `HttpOnly` e `Secure`, recuperação de senha e ativação por convite. Implementar segundo fator para a equipe Rumo. Configurar origens CORS explícitas, política `SameSite` para os domínios escolhidos e validação de origem/CSRF nas rotas autenticadas por cookie.
- **Autorização.** Resolver ator, empresa, área, operação e concessões vigentes no servidor, inclusive para arquivos e tarefas concluídas. A interface recebe as permissões efetivas para montar menus e botões. Restringir operações administrativas globais a rotas próprias.
- **PostgreSQL.** Incluir `empresa_id` em dados de negócio, validar relações com FKs compostas e aplicar segurança por linha. Definir o contexto da empresa dentro da transação ao usar pool de conexões. A conta de execução da API opera sem privilégios de proprietário ou de contorno das políticas.
- **Suspensão manual.** Registrar autor, data e motivo. Revalidar o estado da empresa nas sessões ativas, convites, acesso fiscal, uploads, exportações e downloads. Na reativação, preservar histórico, dados e prazos originais das credenciais.

## 5. Jornada de uma avaliação

1. **Criar em quatro passos.** Selecionar ou cadastrar empresa e responsável técnica. Configurar setores, perfil e quantitativos. Definir período e próxima revisão. Conferir os dados, abrir a avaliação e gerar convites. Salvar o progresso de configuração como rascunho.
2. **Congelar a configuração.** Fixar no ciclo a versão do instrumento, textos de participação, opções de perfil, efetivos e regras metodológicas. Alterações cadastrais posteriores preservam o histórico.
3. **Distribuir convites.** A empresa informa a quantidade. A API gera segredos criptograficamente aleatórios, guarda hashes únicos e entrega os links e QR Codes na emissão. Permitir copiar, imprimir ou baixar o lote e revogar convites disponíveis. Gerar o QR localmente para preservar o segredo. A plataforma dispensa lista nominal de destinatários.
4. **Apresentar a pesquisa.** Mostrar empresa, período, responsável técnica e condições de participação voluntária. Uma pré-visualização do link não consome o convite. Trocar o segredo por credencial de escopo limitado, retirá-lo da URL e impedir seu registro em logs, métricas ou cabeçalhos de referência.
5. **Responder pelo celular.** Oferecer perfil, sete páginas de itens fechados, múltiplas origens quando houver relato e uma página de abertas opcionais. Incluir progresso, voltar, pausar e retomar. Setor participa da configuração obrigatória. O trabalhador pode escolher “Prefiro não informar”. Proposta inicial de retomada no mesmo navegador com rascunho protegido, prazo de expiração e limpeza ao finalizar.
6. **Finalizar atomicamente.** Revalidar empresa, ciclo, validade, consentimento e respostas. Na mesma transação, consumir o convite e criar submissão com ID aleatório independente. Excluir da resposta final qualquer identificador de convite, destinatário, usuário, IP ou dispositivo. Duas requisições concorrentes devem resultar em uma submissão. Se a confirmação se perder, uma nova tentativa informa a conclusão anterior sem revelar respostas.
7. **Acompanhar.** Exibir finalizados, adesão e prazos. Rascunhos ficam fora do numerador. Usar quantitativos do ciclo como denominadores. Limitar granularidade temporal das informações de coleta para impedir correlação entre horário de uso do convite e resposta.
8. **Encerrar e devolver resultados.** Fechar a coleta, registrar a apuração, revisar a conclusão, emitir PDF e disponibilizar a devolutiva agregada à empresa. Vincular ata ou evidência de devolutiva ao ciclo.

## 6. Tabelas e relações do PostgreSQL

As tabelas abaixo são a proposta lógica para as migrations. O ciclo pertence a uma empresa e concentra o histórico de uma aplicação. Nas relações entre tabelas de negócio, a referência deve garantir que os registros pertençam à mesma empresa e, quando aplicável, ao mesmo ciclo.

| Área | Tabelas propostas | Relações e integridade |
|---|---|---|
| Empresas e contrato | `empresas`, `planos_comerciais`, `contratos_empresa`, `historico_status_empresa` | PJ com CNPJ normalizado, único e textual, razão social, fantasia, CNAE, grau de risco e localização. O contrato vincula plano e empresa. O histórico registra bloqueios e reativações. |
| Identidade | `usuarios`, `vinculos_empresa`, `papeis`, `permissoes`, `papel_permissoes`, `permissoes_vinculo`, `atribuicoes_equipe_rumo` | Os vínculos identificam empresas e permissões dos usuários administrativos. O papel global e a atribuição individual de consultoras são explícitos. |
| Autenticação | `sessoes_usuario`, `fatores_mfa`, `tokens_ativacao_recuperacao` | Um usuário tem várias sessões revogáveis. Guardar por hash os segredos de renovação, ativação e recuperação, com validade e consumo. |
| Responsabilidade técnica | `responsaveis_tecnicos_empresa` | Vincula profissional, registro e vigência à empresa. A versão emitida guarda os dados da signatária no momento da assinatura. |
| Organização e perfil | `setores`, `campos_perfil`, `opcoes_campo_perfil`, `ciclos`, `campos_ciclo`, `opcoes_ciclo`, `populacoes_ciclo` | Empresa tem muitos ciclos. Cada ciclo congela efetivos e opções de setor, turno, liderança, sexo, faixa etária, tempo de empresa, regime e campos personalizados. |
| Instrumento e método | `instrumento_versoes`, `metodologia_versoes` | JSON validado, hash, versão, fonte, aprovação e vigência. O ciclo referencia versões imutáveis. Itens, escalas e dimensões podem residir no próprio JSON. Validar referências e códigos na importação. |
| Convites públicos | `lotes_convites`, `convites` | Ciclo tem vários lotes e cada lote vários convites. Hash único por convite, estado e expiração. Manter o controle de distribuição independente das respostas. |
| Respostas anônimas | `submissoes`, `respostas_itens`, `respostas_origens`, `respostas_perfil`, `respostas_abertas` | Submissão pertence ao ciclo. Uma resposta por item e submissão, múltiplas origens de exposição, perfil autodeclarado e abertas opcionais. Validar contra o instrumento daquele ciclo. |
| Qualidade e apuração | `revisoes_qualidade`, `apuracoes`, `indicadores_agregados` | Decisão humana de qualidade com motivo. Apuração identifica ciclo, versão do motor, conjunto de entradas e política de publicação. Registrar agregados usados nas emissões. |
| Inventário | `perigos`, `perigo_dimensoes`, `inventarios`, `riscos_inventario`, `avaliacoes_risco` | Perigos podem depender de várias dimensões. Cada risco referencia setor, perigo e inventário. Persistir memória de cálculo, níveis, ajustes, fontes, avaliador e justificativa. |
| Plano de ação | `acoes`, `acao_riscos`, `historico_acoes` | Uma ação pode tratar vários riscos e setores ou ter alcance de empresa inteira. Guardar tipo de medida, responsável, prazo, meta, situação e origem. |
| Evidências e arquivos | `arquivos`, `evidencias`, `evidencia_acoes`, `pedidos_evidencia` | O arquivo guarda chave privada, tipo, tamanho, hash e estado de processamento. Evidências documentam ações, participação, atas ou devolutiva. O pedido externo refere-se a uma ação. |
| Relatórios | `relatorios`, `versoes_relatorio`, `secoes_relatorio`, `assinaturas_relatorio` | Uma avaliação tem relatório com versões. Cada versão referencia apuração, seções, aprovações e PDF. Seção de conclusão pode servir à página de resultados quando publicada. Retificação gera nova versão. |
| Acessos especiais | `solicitacoes_acesso_rumo`, `autorizacoes_rumo`, `acessos_fiscais` | Guardar pedido, decisão e validade de autorização por área. Acesso fiscal tem escopo, expiração, revogação, identificação do acesso externo e segredo persistido por hash. |
| Auditoria e operação | `eventos_auditoria`, `tarefas`, `exportacoes` | Evento administrativo identifica empresa, ator, papel, operação, recurso e data. Restringir modificações na trilha. Exportação referencia solicitante, período ou apuração, tarefa e arquivo. |

Indexar `(empresa_id, ciclo_id)`, eventos por empresa e data, ações por prazo e estado, convites por hash e tarefas por próxima tentativa. Impedir assinaturas finais concorrentes e relações cruzadas entre empresas. Testar migrations com base vazia e durante atualização de uma base anterior. Usar massa fictícia exclusivamente em desenvolvimento e testes.

## 7. Cálculo, publicação e inventário

### Motor de cálculo em Go

1. Normalizar cada item respondido pelo máximo da própria escala. A pontuação da dimensão é a média das proporções multiplicada por 100. O valor do item 1B já está invertido na definição.
2. Calcular apenas com pelo menos metade dos itens respondidos. Zero é resposta válida. Ausência permanece ausência. Manter essa regra no motor mesmo se a jornada móvel exigir todos os itens fechados antes do envio.
3. Arredondar para duas casas antes de classificar. Para risco, até 33,33 é favorável, de 33,34 a 66,67 é atenção e acima disso é crítico. Para proteção, até 33,33 é crítico, de 33,34 a 66,66 é atenção e a partir de 66,67 é favorável. Obter os valores da definição. Conferir o arredondamento em Go com a referência Python.
4. Para cada grupo, calcular a média dos escores individuais válidos e a distribuição percentual das classificações individuais. Informar o denominador válido quando publicável. O frontend recebe dados calculados, rótulos e estado de proteção.
5. Mostrar separadamente atenção sexual indesejada, ameaças, violência física e bullying. Qualquer frequência diferente de “Não” é relato. Preservar frequência e múltiplas origens quando o detalhamento for publicável. Não produzir índice único de exposição.
6. Calcular adesão como finalizados divididos pelo efetivo do recorte. Denominador desconhecido ou zero gera indisponibilidade. Abaixo de 50%, alertar para cautela. Respostas idênticas nos 40 itens geram revisão humana e permanecem na base.
7. Guardar AB1, AB2, AB3 e OBS como abertas opcionais, fora da pontuação. Remover identificadores e publicar somente sínteses seguras. Registrar o tratamento das três perguntas adicionais da plataforma e do comentário livre.

### Política de publicação

Preservar a referência 1.0.0 e os 18 casos históricos. O JSON original permite resultado geral sem mínimo e o verificador mede o grupo antes de filtrar escores indisponíveis. Acrescentar à API uma política versionada com o critério confirmado de cinco válidos por indicador. Com oito submissões e quatro escores válidos, suprimir aquele indicador. Outra dimensão da mesma empresa pode atender ao mínimo e ser publicada.

Aplicar a política antes de serializar respostas HTTP, gerar arquivos ou fornecer insumos à IA. Ela cobre painel, alertas, filtros, origens de exposição, temas das abertas, inventário, matriz, dossiê e exportações. Permitir até três filtros combinados. Nas comparações, reunir categorias em “Outros” ou suprimir células complementares quando a subtração do total revelar um grupo protegido. Testar inferência por consultas sucessivas permitidas. Para abertas, verificar o número de contribuintes e revisar menções a pessoas ou fatos identificáveis.

### Inventário e matriz de risco

O HTML especifica 12 perigos e as matrizes 4×4 e 5×5. Versionar essa metodologia separadamente do COPSOQ e submetê-la à responsável técnica.

- Para cada setor e perigo, usar a maior proporção em vermelho entre as dimensões associadas. Os limites de probabilidade da matriz 4×4 são 10%, 25% e 50%. Na 5×5 são 10%, 20%, 35% e 50%. Insumo protegido ou indisponível exige estado explícito.
- Aplicar severidade base, agravante quando esgotamento ou estresse atinge pelo menos 25% em vermelho e nível mínimo alto para os relatos previstos de violência física ou atenção sexual indesejada. Registrar cálculo antes e depois de exceções.
- O avaliador responde sobre abertas, observação do trabalho por AEP, rodas de conversa, indicadores e evento pontual resolvido. O ajuste de probabilidade é limitado a um nível. Duas fontes confirmatórias podem elevar a probabilidade. A redução exige evento resolvido e comprovado, ausência de confirmação e as condições de AEP e rodas previstas no protótipo. Guardar fontes, respostas e justificativa.
- Setores de cinco a nove participantes recebem alerta de baixa precisão e confirmação obrigatória. Exibir o risco por setor, probabilidade, severidade, nível, evidências, responsável pela avaliação e ações vinculadas.
- Prazos de referência do HTML: monitoramento para risco baixo, até 180 dias para moderado, até 90 dias para alto e início em até 30 dias para crítico. Documentar os parâmetros homologados com a versão do método.

## 8. Cobertura das telas e contrato da API

Publicar o contrato OpenAPI no repositório `api`. Na tabela, `E` equivale a `/v1/empresas/{empresaId}`, `C` a `E/ciclos/{cicloId}` e `V` a `C/relatorios/{relatorioId}/versoes/{versaoId}`. Cada operação especifica ator, escopo, validações, formato de erro, requisitos de privacidade e evento de auditoria.

| Tela ou fluxo | Operações propostas |
|---|---|
| Login e conta | `POST /v1/auth/login`, `/v1/auth/mfa/verificar`, `/v1/auth/renovar`, `/v1/auth/logout`, `/v1/auth/ativar`, `/v1/auth/recuperar`, `/v1/auth/redefinir-senha`. `GET /v1/me` entrega ator, empresas e permissões efetivas. |
| Home da Rumo e equipe | `GET /v1/admin/painel`, `GET/POST /v1/admin/empresas`, `GET/PATCH /v1/admin/empresas/{id}`, `POST /v1/admin/empresas/{id}/bloquear` e `/reativar`. `GET/POST /v1/admin/equipe` e `PATCH /v1/admin/equipe/{id}`. Cards com empresas, plano, assinatura, adesão, datas e pendências. |
| Empresa e campos | `GET/PATCH E`, `GET/PUT E/responsavel-tecnica`. Listar, criar, alterar e desativar setores, campos e opções em `E/setores` e `E/campos-perfil`. Prever consulta de CNPJ por provedor autorizado e preenchimento manual. |
| Usuários e permissões | `GET E/usuarios`, `POST E/convites-usuarios`, `PATCH/DELETE E/usuarios/{id}`, `GET/PUT E/usuarios/{id}/permissoes`. A remoção revoga o vínculo com a empresa. |
| Autorizações à Rumo | `GET/POST E/solicitacoes-acesso`, `POST E/solicitacoes-acesso/{id}/aprovar` e `/recusar`, `GET/POST E/autorizacoes`, `POST E/autorizacoes/{id}/revogar`. |
| Instrumento e método | `GET /v1/instrumentos`, `GET /v1/instrumentos/{versao}`, `GET /v1/instrumentos/{versao}/arquivo`, `GET /v1/metodologias/{versao}`. A carga técnica valida a definição. A tela mostra escalas, opções, itens, dimensões, cortes e abertas da versão usada. |
| Nova avaliação e ciclo | `GET/POST E/ciclos`, `GET/PATCH C`, `PUT C/configuracao-perfil`, `PUT C/populacoes`, `PUT C/revisao-programada`, `POST C/abrir`, `POST C/encerrar`, `GET C/adesao`. |
| Convites e coleta pública | `GET/POST C/lotes-convites`, `POST C/convites/{id}/revogar`, `POST /v1/publico/convites/trocar`, `GET /v1/publico/questionario`, `POST /v1/publico/submissoes`. O link e o QR usam o mesmo convite. A pausa local dispensa associação permanente entre convite e rascunho no banco. |
| Resultados e conclusão | `GET C/resultados`, `C/resultados/filtros`, `C/resultados/comparacao-grupos`, `C/resultados/exposicoes`, `C/resultados/temas-abertos` e `C/resultados/comparacao-ciclos`. `GET/PUT C/conclusao` com autoria e situação de publicação. |
| Inventário | `GET C/inventario`, `PUT C/inventario/matriz`, `GET C/inventario/riscos/{id}`, `PUT C/inventario/riscos/{id}/avaliacao`, `POST C/inventario/exportacoes`. Gerar Word e Excel com supressões e memória de cálculo. |
| Plano de ação | `GET/POST C/acoes`, `GET/PATCH C/acoes/{id}`, `GET C/acoes/cronograma`, `POST C/acoes/sugestoes`, `POST C/acoes/sugestoes/aplicar`. Permitir editar e selecionar sugestões antes de aplicá-las. |
| Evidências e atas | `GET/POST C/evidencias`, `GET C/evidencias/{id}`, `GET C/evidencias/{id}/arquivo`, `POST C/acoes/{id}/pedidos-evidencia`, `POST /v1/publico/pedidos-evidencia/trocar`, `POST /v1/publico/evidencias`. Link externo de uso único, com sete dias por padrão. |
| Relatório técnico | `GET/POST C/relatorios`, `GET/POST C/relatorios/{id}/versoes`, `GET V`, `POST V/rascunho-ia`, `PATCH V/secoes/{id}`, `POST V/secoes/{id}/aprovar`, `POST V/assinar`, `GET V/pdf`. Expor ao cliente apenas o estado até a liberação do conteúdo. |
| Fiscalização | `GET C/pasta-fiscal`, `POST C/pasta-fiscal/dossies`, `GET/POST E/acessos-fiscais`, `POST E/acessos-fiscais/{id}/revogar`, `POST /v1/publico/fiscal/autenticar`. Autorizar somente leitura nos recursos permitidos ao fiscal. |
| Auditoria e tarefas | `GET E/auditoria`, `POST E/auditoria/exportacoes`, `GET E/tarefas/{id}`, `GET E/exportacoes/{id}/arquivo`. Filtrar o CSV por período e área. Revalidar permissão e estado da empresa na entrega do arquivo. |

Definir no contrato os formatos de data, paginação, ordenação, limites de upload, concorrência nas edições e respostas para sessão expirada, permissão insuficiente, ciclo encerrado, duplicidade e resultado protegido. Entregar erros compreensíveis para o frontend e identificadores de diagnóstico sem conteúdo da pesquisa.

## 9. Frontend responsivo e documentos

- **Tema e navegação.** Basear o Bootstrap na barra lateral petróleo `#0C3B46`, destaque laranja `#E8831F`, fundo `#F4F2EE`, títulos em Bricolage Grotesque e corpo em Manrope. Preservar modo escuro, contexto de empresa e ciclo, foco visível, navegação por teclado e menu móvel. Associar rótulos textuais às cores de risco e oferecer tabela equivalente aos gráficos.
- **Resultados.** Mostrar régua de 0 a 100, média, distribuição, denominador válido, comparação por campo, alertas, conclusão escrita e estados de indisponibilidade ou proteção. Na comparação histórica, usar o total da empresa com instrumento e cortes compatíveis. O HTML considera variações inferiores a um ponto estáveis para exibição.
- **Plano e evidências.** Oferecer tabela com perigo, setor, medida, responsável, início, prazo, meta e situação. Derivar atraso e pendência de comprovação. Uma ação informada como concluída precisa de evidência válida para aparecer como comprovada. Permitir anexar documentos, registrar atas e verificar arquivos reais. Sinalizar treinamento como única medida em risco alto ou crítico segundo a metodologia homologada.
- **IA e relatório.** Gerar rascunhos a partir de agregados publicáveis e sínteses desidentificadas. Revisar conclusão, metodologia, resultados por setor e recomendações. Editar uma seção aprovada exige nova aprovação. PDF interno de rascunho deve trazer marca em todas as páginas. A signatária emite a versão final com hash, data, registro, seções aprovadas e referência à apuração. Definir o mecanismo de assinatura com a Rumo antes da emissão em produção. Manter versões anteriores acessíveis a quem tem autorização.
- **Pasta fiscal.** Apresentar os dez itens do HTML: identificação e responsável técnica, metodologia, resultados, inventário, plano, ações comprovadas, participação dos trabalhadores, documentos emitidos, auditoria e revisão programada. Cada item mostra origem, pendência ou evidência. O dossiê consolida versões emitidas e anexos permitidos em PDF selecionável.
- **Amplify estático.** Publicar páginas conhecidas como `/responder/`, `/fiscal/`, `/empresa/` e `/avaliacao/`. Carregar dados privados em tempo de execução pela API Go. Testar abertura de links recebidos por mensagem, recarga direta, tema escuro, telas estreitas e vencimento de credenciais. O pacote publicado contém apenas ativos públicos.

## 10. Sequência de implementação no outro PC

Clonar os três repositórios como pastas irmãs em um mesmo diretório e abrir o diretório pai no Codex. Verificar a presença dos anexos desta seção de referências no clone, inclusive dos três PDFs. Trabalhar por etapa. Em cada entrega, conferir o critério de aceite e identificar os commits correspondentes em cada repositório afetado.

| Etapa | Entrega | Critério de conclusão |
|---|---|---|
| 1. Reproduzir a referência | Conferir versões, arquivos e cobertura do HTML. Executar o verificador Python. | 18/18 casos passam e todas as áreas do HTML estão associadas a uma fase. |
| 2. Subir a base local | Dockerfiles, Compose de integração, migrations iniciais, conexão Go–PostgreSQL, frontend e contrato OpenAPI inicial. | Em instalação limpa, sobem API, app, banco e worker. Migrations e testes de saúde passam. |
| 3. Isolar contas | Implementar empresas, identidade, MFA, papéis, autorização, suspensão e auditoria básica. | Duas empresas isoladas na API e no banco. Bloqueio e reativação pelo admin global com histórico. |
| 4. Calcular e proteger | Importar definição imutável. Portar os testes e o motor para Go. Importar o CSV sintético e implementar a política de publicação. | Python e Go concordam nos 18 casos. Médias e distribuições de referência reproduzidas. Manutenção aparece protegida nas saídas disponíveis. |
| 5. Coletar | Nova avaliação em quatro etapas, congelamento, convites, QR, consentimento, formulário móvel, pausa, retomada, envio único e adesão. | Uma empresa consegue fazer a coleta sem cadastrar trabalhadores. Duas abas com o mesmo convite produzem uma submissão. |
| 6. Apurar e revisar | Painel, filtros, conclusão, exposição, inventário, matrizes e confirmação técnica. | Cada número publicado tem denominador e memória de cálculo reproduzível. Inspecionar também a resposta da API para conferir supressões. |
| 7. Completar a primeira avaliação | Rascunho por IA, revisão, assinatura, PDF, plano tabular, evidências, devolutiva e auditoria de acessos e exportações. | Com massa fictícia, percorrer do convite à emissão. O cliente acessa somente conteúdo liberado. |
| 8. Cobrir os fluxos complementares | Pasta fiscal e dossiê, auditor externo, autorizações por área, envio externo de evidência, cronograma, sugestões, Word/Excel/CSV e comparação histórica. | Cada ação funcional prevista no HTML tem operação real, ator autorizado e teste de aceite. |
| 9. Homologar e publicar | Revisar método com Rosalina, testar carga e navegação, validar assinatura, restaurar backup e implantar em homologação AWS antes de produção. | Avaliação completa reproduzível em homologação e recuperação verificável do banco, relatório e evidências. |

## 11. Testes de aceite

| Cenário | Resultado esperado |
|---|---|
| Uma empresa conhece o ID de um recurso de outra | Leitura, escrita, exportação, tarefa e download são negados. Chaves compostas impedem vínculos cruzados. |
| Empresa suspensa com sessões e links emitidos | As operações passam a respeitar o bloqueio. Reativar mantém histórico e vencimentos das credenciais. |
| Pré-visualização do convite, duas abas, duplo clique ou falha de rede | A pré-visualização preserva o convite. Um único envio é contabilizado. A repetição recebe estado coerente. |
| Inspeção das tabelas, logs e auditoria | Nenhuma relação direta convite–submissão, segredo de convite, corpo das respostas ou lista nominal de trabalhadores nas trilhas de coleta. |
| Quatro respostas válidas na empresa, em um setor ou em uma dimensão | Suprimir o indicador em todas as saídas. Com cinco válidos, testar também inferência por subtração e por consultas permitidas. |
| Importação dos 60 fictícios | Demandas quantitativas (D01) tem média geral 51,46. Satisfação no trabalho (D13) tem média 60,00 e distribuição individual de 65% favorável, 0% atenção e 35% crítica. Manutenção tem quatro respondentes e fica sem linha própria publicável. |
| Exposição, respostas ausentes e abertas | Testar zero, omissão, item 1B, limites e origem múltipla. Alterar um relato para “Não” elimina origens incompatíveis. Os quatro textos abertos permanecem após envio e obedecem às regras de publicação. |
| Matrizes e ações | Cobrir limites das duas matrizes, agravante, nível mínimo, ajuste máximo, baixa precisão e ação concluída sem anexo comprobatório. |
| Relatório e acesso fiscal | Cliente e fiscal não recuperam rascunho interno por URL direta. Somente a responsável técnica designada assina. Retificação preserva PDF anterior. Revogar ou expirar acesso impede novas consultas e entregas de arquivos. |
| Instalação e restauração | Partindo dos clones, subir o ambiente, aplicar migrations e restaurar uma cópia. Conferir um PDF assinado e suas evidências pelos hashes registrados. |

## 12. Implantação e operação AWS

**Desenvolvimento.** Executar Next.js, API Go, worker e PostgreSQL em contêineres. Usar volume persistente para dados locais, recarga de código e variáveis de ambiente documentadas. A mesma imagem Go pode iniciar API e worker com comandos distintos.

**Produção.** Publicar o frontend estático no Amplify. Proposta inicial de uma instância Lightsail com Docker Compose para proxy HTTPS, API, worker e PostgreSQL com volume persistente. Manter a porta do banco na rede privada dos contêineres. Esta topologia concentra API e banco na mesma instância e tem um ponto único de falha. Usar armazenamento privado independente para documentos e cópias de segurança.

**Publicação coordenada.** O CI de `bd` valida migrations. O de `api` executa o verificador Python, a suíte Go e integração com PostgreSQL. O de `app` valida tipos, build estático e jornadas. Publicar imagens com referências imutáveis, executar migrations uma vez por release, verificar saúde e registrar as três revisões homologadas. Para reversão de aplicação, preservar compatibilidade com o esquema já aplicado.

**Recuperação e monitoramento.** Guardar backups criptografados fora da instância. Definir retenção, tempo de recuperação e perda de dados tolerável com a operação. Ensaiar restauração conjunta do banco e dos objetos. Monitorar disco, disponibilidade, conexões, fila, falhas de geração de documentos e idade do último backup. Excluir segredos de convite, respostas, textos livres e conteúdo de anexo dos logs de aplicação e infraestrutura.

**Demonstração final.** Executar o percurso com duas empresas fictícias. A primeira usa os 60 respondentes e chega ao relatório emitido e à pasta fiscal. A segunda tem quatro respondentes, acompanha a coleta e permanece sem indicadores publicáveis. Demonstrar troca de empresa pelo admin global, isolamento da PJ, resposta anônima, bloqueio manual e revogação do acesso fiscal.
