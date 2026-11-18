# Plano de execução do Rumo Insights

**Referência do planejamento:** 18/11/2026.  
**Objetivo:** permitir que a Rumo e uma empresa cliente conduzam uma avaliação psicossocial completa, da configuração da coleta à devolutiva, à emissão do relatório técnico e ao acompanhamento das ações com evidências.

O plano cobre os três repositórios Git independentes, `api`, `app` e `bd`. O HTML define o escopo funcional. O print de planejamento orienta a primeira entrega. As decisões confirmadas abaixo prevalecem sobre os comportamentos de demonstração. O documento descreve trabalho a implementar.

## 1. Decisões de produto

| Tema | Regra de produto |
|---|---|
| Empresas clientes | Cada pessoa jurídica possui cadastro próprio, usuários administrativos, avaliações, dados e documentos isolados. Um admin global da Rumo pode acessar qualquer empresa e suspender ou reativar seu acesso por inadimplência. A cobrança é externa na primeira versão. |
| Trabalhadores | Participam anonimamente, sem cadastro e sem login permanente. A empresa gera convites individuais em lote e os distribui por seu próprio canal. Cada convite tem um link e um QR Code que representa o mesmo link. |
| Aderência ao HTML | O HTML já contempla códigos individuais de uso único e também um código coletivo. Implementar exclusivamente a modalidade individual. A administradora da empresa precisa de permissão para emitir e revogar convites. No HTML, o modelo de perfil de RH tem apenas leitura na área de ciclo. |
| Unidade de controle | Cada convite permite uma submissão. A plataforma desconhece a identidade de quem recebeu o convite. Distribuir um único convite por pessoa é responsabilidade da empresa. |
| Fiscalização | Manter somente o auditor-fiscal externo, com acesso temporário, revogável, de leitura e restrito à empresa. A responsável técnica da Rumo revisa e assina o relatório. |
| Privacidade | Publicar cada indicador a partir de cinco respondentes válidos, inclusive no total da empresa e em cada recorte. Setores abaixo do mínimo ficam protegidos individualmente, sem agrupamento. Aplicar a regra na tela e em todas as exportações. |
| Apresentação do COPSOQ II-Br | Incluir na primeira entrega os sete domínios como títulos sem pontuação ou cor, as 11 dimensões validadas como resultados principais no painel, relatório e inventário, e as 23 subdimensões da versão curta como detalhe expansível. Comportamentos ofensivos é apresentado pelos quatro tipos separados. |
| Escala de apresentação do COPSOQ II-Br | Exibir escores de 0 a 100. Manter a soma dos itens respondidos na memória técnica para conferência com a tese. |
| Probabilidade no COPSOQ II-Br | A probabilidade usa as subdimensões associadas a cada perigo. A adesão é usada apenas para o alerta de cautela. |
| Apuração imediata no COPSOQ II-Br | Relato de assédio sexual (20), ameaça de violência (21), violência física (22) ou assédio moral (23), em base publicável, aciona alerta, ação obrigatória com prazo de 15 dias e estado “Sob apuração” no inventário. A matriz mantém o nível calculado até revisão após conclusão documentada. |

**Primeira entrega.** Cadastro da PJ e dos acessos, instrumento versionado, nova avaliação em quatro passos, coleta móvel anônima, painel de adesão e prazos, resultados em três níveis com filtros e conclusão, relatório técnico revisado e assinado, inventário, plano de ação tabular com fluxo de apuração imediata, evidências, auditoria e testes automáticos.

**Complementos para cobrir o HTML.** Incluir pasta fiscal completa e dossiê, visão do auditor externo, autorização temporária à consultoria, envio externo de evidências, cronograma, sugestões revisáveis de ações, exportações e comparação entre ciclos. As restrições de acesso devem estar ativas desde a primeira entrega de cada recurso.

**Evoluções posteriores.** Disponibilizar outras versões do COPSOQ, HSE e outros instrumentos após homologação de suas regras. A primeira entrega já utiliza a estrutura descrita na seção 3, com o COPSOQ II-Br curto como único instrumento disponível ao cliente. Pagamentos online, autoatendimento comercial, parceiros com marca própria, referências por segmento, assistente de RH, envio integrado por WhatsApp e canal de denúncias ficam para fases posteriores. Os instrumentos legados continuam no sistema atual enquanto forem utilizados.

## 2. Referências e verificações iniciais

| Fonte | Uso na implementação |
|---|---|
| [Protótipo HTML](../../app/docs/prototipo-rumo-insights.html) | Jornada do trabalhador, navegação administrativa, permissões por área, cadastro, cálculo demonstrativo, inventário, avaliação do perigo, ações, evidências, fiscal, relatório, auditoria e identidade visual. O link relativo pressupõe os três clones em pastas irmãs. |
| [LEIA-ME](LEIA-ME.md) e [definição COPSOQ II-Br](copsoq_ii_br.json) | A revisão mantém sete escalas, 40 itens, 23 subdimensões e quatro perguntas abertas opcionais. Acrescenta o mapeamento dos sete domínios e das 11 dimensões validadas. Para publicação, probabilidade e abrangência da apuração imediata, aplicar as decisões desta revisão do plano. |
| [Casos conhecidos](casos_de_teste.json) e [verificador Python](verificar_calculo.py) | Referência executável para a implementação em Go. Os 21 casos passaram em 18/11/2026. Executar a partir do diretório que contém os três repositórios com `python3 -B api/docs/verificar_calculo.py`. |
| [Respondentes fictícios](respondentes_ficticios.csv) | Massa integrada de 60 participantes. Operação tem 26, Administrativo 18, Comercial 12 e Manutenção quatro. Usar os quatro setores para verificar tanto a classificação quanto a proteção de grupos pequenos. |
| [Questionário brasileiro curto](copsoq_II_curto_versao_adap_brasil.pdf) | Os 40 enunciados do JSON foram encontrados no texto do PDF após normalizar espaços e ligaturas. Conferir opções, introduções e períodos de referência na homologação. No item 17, as opções vão de 0 a 4 e a legenda informa total até 8. O JSON adota máximo 4, coerente com as opções. Registrar a decisão técnica. |
| [Artigo de adaptação cultural](adaptacao_cultural_copsoq_brasil.pdf) e [tese brasileira](tese_de_doutorado_copsoq_brasil_jsg_final.pdf) | Referências para a adaptação brasileira. Na tese de Gonçalves JS (PPG Fisioterapia, UFSCar, 2019), a Tabela 2, pp. 22–23, fundamenta a composição e a Tabela 3, p. 24, traz a consistência interna. A seção de instrumentos, p. 12, descreve a soma dos itens e a exceção dos comportamentos ofensivos. |
| [Manual português do COPSOQ II](https://www.copsoq-network.org/assets/Uploads/COPSOQ-Manual-Portugal2013.pdf#page=8) | Silva et al. descrevem os tercis na escala de 1 a 5. O pacote adota a divisão em terços na escala de 0 a 100, com cortes operacionais de 33,33 e 66,67. |

O HTML mantém dados no navegador, usa data fixa e simula autenticação, geração de documentos e algumas integrações. Na finalização do questionário, os textos abertos preenchidos não são copiados para a resposta persistida. Na visualização do relatório, algumas seções em leitura podem ser renderizadas enquanto o texto da interface promete ocultar o rascunho do cliente. Incluir testes específicos para ambas as situações na plataforma real.

### Comparativo com as versões anteriores

O comparativo de 18/11/2026 usa `337c770` em `api` e `4cfa86c` em `app` como base para os arquivos atualizados da árvore de trabalho.

| Área | Antes | Revisão e efeito para a implementação |
|---|---|---|
| Instrumento | 23 dimensões e agrupamento brasileiro em aberto. | O JSON passa a definir os sete domínios e as 11 dimensões validadas, seus itens de origem, direção, alfa quando aplicável, amplitude de soma e permissão de agregação. As duas revisões declaram `1.0.0`. Registrar o hash e distinguir revisões na importação sem sobrescrever versões usadas em ciclos. |
| Motor e casos | 18 casos. Só as subdimensões tinham cálculo individual. | O Python reutiliza o mesmo cálculo para os dois níveis e devolve soma e pontuação. C18 foi ampliado para verificar o mapeamento. C19 e C20 verificam Burnout e estresse e Demandas no trabalho. C21 verifica a recusa do escore agregado de Comportamentos ofensivos. |
| Resultados e instrumento no HTML | Três agrupamentos visuais com 23 dimensões. | Resultados e comparação por grupo usam domínios e dimensões validadas. O painel abre as subdimensões e a tela do instrumento apresenta o mapeamento e o inclui no download demonstrativo do JSON. O HTML ainda mostra a soma no detalhe. Os contadores de dimensões por faixa, o relatório demonstrativo, a comparação histórica e a matriz ainda usam subdimensões. Os contadores e o relatório devem acompanhar a camada principal em produção. |
| Exposição no HTML | Alerta geral de exposição e piso Alto na matriz para os casos graves previstos. | O HTML mantém o nível calculado, mostra “Sob apuração” e permite incluir a ação obrigatória para os itens 20 e 22. A implementação estende o fluxo aos itens 21 e 23, mostra frequência e origem quando publicáveis e registra a conclusão com evidência antes da revisão do nível. |
| Dados de teste | 60 respondentes no CSV e na demonstração. | O conteúdo do CSV permanece igual após normalizar as quebras de linha. O HTML injeta um relato fictício de violência física em tempo de execução, com origem em cliente. Reproduzir essa variação em cenário de aceite próprio para o alerta. |

### Decisões confirmadas por Rosalina

O retorno de Rosalina incorporado em 18/11/2026 resolve a pergunta original. O painel estreia em três níveis, domínios servem como títulos, Burnout e estresse tem escore próprio, os quatro comportamentos ofensivos aparecem separados e a apresentação usa a escala 0–100. O detalhe de Satisfação no trabalho deve distinguir respostas individuais da média de grupo, conforme a seção 7.

No retorno complementar, Rosalina confirmou o mínimo de cinco respondentes válidos para publicar cada indicador, inclusive no total da empresa, e a proteção individual dos setores que ficarem abaixo do mínimo. Confirmou também que a matriz usa as subdimensões de cada perigo e que a adesão serve apenas para o alerta de cautela. A apuração imediata e a ação obrigatória de 15 dias passam a abranger os quatro tipos de comportamento ofensivo.

**Levantamento anterior.** A cópia local do MySQL legado (`rumo-saudavel-v2/mysql/rumosaudavel.sql`, extraída em 29/10/2026) contém duas aplicações COPSOQ fora dos cadastros identificados como demonstração ou teste, somando 51 participantes com cobertura objetiva completa e também 51 com marcador de conclusão. Em ambas, faltam dados que permitam atribuir os participantes a setores. Nas quatro aplicações de demonstração, o mínimo de cinco protegeria 10 dos 11 recortes setoriais com respondentes em ambas as bases.

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

### Base para múltiplos instrumentos desde a primeira entrega

O áudio de Rosalina de 18/11/2026 pede que cálculo, dimensões, riscos e apresentação acompanhem o questionário aplicado. Implementar a primeira versão pelo mesmo caminho que receberá um segundo instrumento. As regras do COPSOQ II-Br curto entram como a primeira definição e metodologia. Coleta, proteção da publicação, inventário, documentos e auditoria compartilham o fluxo da plataforma.

| Área | Estruturar na primeira entrega |
|---|---|
| Identidade e versionamento | Dar a cada instrumento um código estável. Distinguir a revisão imutável do conteúdo, identificada internamente e conferida por hash, da versão do formato JSON. Códigos de itens e indicadores são locais à definição do instrumento. No rascunho, o ciclo recebe uma revisão disponível e uma metodologia compatível. Fixar ambas ao abrir a coleta. Leitura, submissão, apuração e emissão recuperam as versões do ciclo. Mudanças publicadas servem a novos ciclos. |
| Definição e importação | Importar o COPSOQ II-Br curto por uma rotina técnica e preservar o arquivo de referência. Definir no contrato de importação os blocos e sua ordem, itens, opções e escores, obrigatoriedade, condições de apresentação já usadas na coleta, dimensões, agrupamentos, fórmula com parâmetros, tratamento de faltantes, faixas e rótulos. Validar antes de disponibilizar a revisão, incluindo códigos únicos no respectivo escopo, referências entre itens e indicadores e suporte às regras declaradas. Informar claramente qualquer regra não suportada. |
| Motor de apuração | Separar validação de respostas, cálculo do indicador, agregação, classificação e publicação. A definição identifica a função Go e a versão da regra de cada indicador. Começar pelas operações do COPSOQ II-Br curto, incluindo a soma de itens, o escore normalizado e a ocorrência por item. Registrar a versão do motor na apuração e preservar estados distintos para valor zero, dado indisponível e dado protegido. Uma correção de cálculo que afete um ciclo já apurado gera nova apuração rastreável e preserva a anterior. |
| Inventário, alertas e ações | Vincular os indicadores à metodologia e aos perigos por mapeamento versionado. A metodologia fornece matriz, agravantes, gatilhos, prazos e tipo de ação. No COPSOQ II-Br curto, a apuração imediata é configurada para os quatro tipos de exposição dos itens 20 a 23. Os gatilhos são definidos pela combinação de instrumento e metodologia do ciclo. |
| Formulários e resultados | A API entrega a estrutura do formulário e os metadados de cada medida publicável, como agrupamento, ordem, rótulo, unidade, escala, faixa e denominador, quando aplicáveis. Reutilizar essa estrutura no app, relatório e exportações. A quantidade de páginas, a hierarquia em três níveis e a régua de 0 a 100 são dados da configuração do COPSOQ II-Br curto. A comparação entre ciclos exige equivalência explícita entre os indicadores, seus cálculos, unidades e cortes. |

A primeira entrega inclui a importação técnica, a definição real do COPSOQ II-Br curto e uma definição fictícia pequena para teste. Disponibilizar um segundo instrumento real exige sua referência, casos de cálculo conhecidos, metodologia compatível e revisão da responsável técnica. Se o método couber nas operações existentes, carregar sua configuração é suficiente. Uma regra inédita entra como função Go testada no motor. A interface de gestão do catálogo e eventual leitura de documentos por IA ficam para a etapa de expansão. Se essa automação for aprovada, a IA prepara um rascunho de configuração com referências e casos de teste. A aprovação técnica libera a definição para o cálculo reproduzível em Go.

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

1. **Criar em quatro passos.** Selecionar ou cadastrar empresa e responsável técnica. Configurar setores, perfil e quantitativos. Definir período e próxima revisão. Mostrar no rascunho o instrumento e a metodologia que serão aplicados. Na primeira entrega, a API atribui o COPSOQ II-Br curto como opção disponível. Conferir os dados, abrir a avaliação e gerar convites. Salvar o progresso de configuração como rascunho.
2. **Congelar a configuração.** Fixar no ciclo as revisões aprovadas do instrumento e da metodologia, textos de participação, opções de perfil e efetivos. Validar a compatibilidade antes de abrir a coleta. Alterações cadastrais posteriores preservam o histórico.
3. **Distribuir convites.** A empresa informa a quantidade. A API gera segredos criptograficamente aleatórios, guarda hashes únicos e entrega os links e QR Codes na emissão. Permitir copiar, imprimir ou baixar o lote e revogar convites disponíveis. Gerar o QR localmente para preservar o segredo. A plataforma dispensa lista nominal de destinatários.
4. **Apresentar a pesquisa.** Mostrar empresa, período, responsável técnica e condições de participação voluntária. Uma pré-visualização do link não consome o convite. Trocar o segredo por credencial de escopo limitado, retirá-lo da URL e impedir seu registro em logs, métricas ou cabeçalhos de referência.
5. **Responder pelo celular.** Renderizar perfil e páginas do instrumento congelado. O COPSOQ II-Br curto tem sete páginas de itens fechados, múltiplas origens quando houver relato e uma página de abertas opcionais. Incluir progresso, voltar, pausar e retomar. Setor participa da configuração obrigatória. O trabalhador pode escolher “Prefiro não informar”. Proposta inicial de retomada no mesmo navegador com rascunho protegido, prazo de expiração e limpeza ao finalizar.
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
| Instrumento e método | `instrumentos`, `instrumento_versoes`, `metodologia_versoes` | O instrumento tem código estável. Cada revisão tem identificador interno, versão declarada, versão do formato, JSON validado, hash, fonte, aprovação e vigência. O ciclo referencia as revisões imutáveis de instrumento e metodologia. A carga valida a compatibilidade e as referências entre as duas. |
| Convites públicos | `lotes_convites`, `convites` | Ciclo tem vários lotes e cada lote vários convites. Hash único por convite, estado e expiração. Manter o controle de distribuição independente das respostas. |
| Respostas anônimas | `submissoes`, `respostas_itens`, `respostas_origens`, `respostas_perfil`, `respostas_abertas` | Submissão pertence ao ciclo. Uma resposta por item e submissão, múltiplas origens de exposição, perfil autodeclarado e abertas opcionais. Validar contra o instrumento daquele ciclo. |
| Qualidade e apuração | `revisoes_qualidade`, `apuracoes`, `indicadores_agregados` | Decisão humana de qualidade com motivo. Apuração identifica ciclo, versão do motor, conjunto de entradas e política de publicação. Registrar agregados usados nas emissões. |
| Inventário | `perigos`, `perigo_dimensoes`, `inventarios`, `riscos_inventario`, `avaliacoes_risco` | Perigos podem depender de vários indicadores da revisão do instrumento vinculada à metodologia. Vincular o mapeamento à revisão da metodologia. Cada risco referencia setor, perigo e inventário. Persistir memória de cálculo, níveis, ajustes, fontes, avaliador e justificativa. Guardar o estado de apuração do relato e a evidência da conclusão. |
| Plano de ação | `acoes`, `acao_riscos`, `historico_acoes` | Uma ação pode tratar vários riscos e setores ou ter alcance de empresa inteira. Guardar tipo de medida, responsável, prazo, meta, situação e origem. Para ação obrigatória de apuração, guardar a referência ao alerta e impedir duplicação por ciclo e tipo de relato. |
| Evidências e arquivos | `arquivos`, `evidencias`, `evidencia_acoes`, `pedidos_evidencia` | O arquivo guarda chave privada, tipo, tamanho, hash e estado de processamento. Evidências documentam ações, participação, atas ou devolutiva. O pedido externo refere-se a uma ação. |
| Relatórios | `relatorios`, `versoes_relatorio`, `secoes_relatorio`, `assinaturas_relatorio` | Uma avaliação tem relatório com versões. Cada versão referencia apuração, seções, aprovações e PDF. Seção de conclusão pode servir à página de resultados quando publicada. Retificação gera nova versão. |
| Acessos especiais | `solicitacoes_acesso_rumo`, `autorizacoes_rumo`, `acessos_fiscais` | Guardar pedido, decisão e validade de autorização por área. Acesso fiscal tem escopo, expiração, revogação, identificação do acesso externo e segredo persistido por hash. |
| Auditoria e operação | `eventos_auditoria`, `tarefas`, `exportacoes` | Evento administrativo identifica empresa, ator, papel, operação, recurso e data. Restringir modificações na trilha. Exportação referencia solicitante, período ou apuração, tarefa e arquivo. |

Indexar `(empresa_id, ciclo_id)`, eventos por empresa e data, ações por prazo e estado, convites por hash e tarefas por próxima tentativa. Impedir assinaturas finais concorrentes e relações cruzadas entre empresas. Testar migrations com base vazia e durante atualização de uma base anterior. Usar massa fictícia exclusivamente em desenvolvimento e testes.

## 7. Cálculo, publicação e inventário

### Motor de cálculo em Go e regras do COPSOQ II-Br curto

As fórmulas, cortes e exemplos a seguir são da configuração inicial. O motor obtém essas regras e seus parâmetros das revisões vinculadas ao ciclo, conforme a seção 3.

1. Normalizar cada item respondido pelo máximo da própria escala. A pontuação é a média das proporções multiplicada por 100. Usar o mesmo motor para a dimensão validada e para a subdimensão. Calcular a dimensão validada diretamente de seus itens, sem fazer média dos escores das subdimensões. O valor do item 1B já está invertido na definição.
2. Calcular apenas com pelo menos metade dos itens respondidos. Zero é resposta válida. Ausência permanece ausência. Manter essa regra no motor mesmo se a jornada móvel exigir todos os itens fechados antes do envio.
3. Arredondar para duas casas antes de classificar. Para risco, até 33,33 é favorável, de 33,34 a 66,67 é atenção e acima disso é crítico. Para proteção, até 33,33 é crítico, de 33,34 a 66,66 é atenção e a partir de 66,67 é favorável. Obter os valores da definição. Conferir o arredondamento em Go com a referência Python.
4. Para cada grupo, calcular a média dos escores individuais válidos e a distribuição percentual das classificações individuais. Informar o denominador válido quando publicável. Explicar que Satisfação no trabalho (V06/D13) só assume 0, 33,33, 66,67 ou 100 na classificação individual. A distribuição individual tem 0% em atenção e a média de grupo pode cair nessa faixa.
5. Burnout e estresse (V10, α = 0,87) reúne os itens 18A, 18B, 19A e 19B. No C19, respostas 3, 3, 2 e 2 somam 10 de 16 e resultam em 62,50 na faixa de atenção. Preservar a soma observada e os itens usados para auditoria. V06 e V09 têm um único item e alfa inaplicável.
6. Comportamentos ofensivos (V11, α = 0,54) tem escore agregado indisponível por regra do instrumento. Mostrar frequência e origem publicáveis para assédio sexual (20, atenção sexual indesejada no enunciado), ameaças de violência (21), violência física (22) e assédio moral (23, bullying no enunciado). Qualquer frequência diferente de “Não” é relato. Preservar as múltiplas origens.
7. Calcular adesão como finalizados divididos pelo efetivo do recorte. Denominador desconhecido ou zero gera indisponibilidade. Abaixo de 50%, emitir apenas alerta de cautela. Respostas idênticas nos 40 itens geram revisão humana e permanecem na base.
8. Guardar AB1, AB2, AB3 e OBS como abertas opcionais, fora da pontuação. Remover identificadores e publicar somente sínteses seguras. Registrar o tratamento das três perguntas adicionais da plataforma e do comentário livre.

### Política de publicação

Preservar a revisão `1.0.0` do pacote e a suíte de 21 casos como referência do cálculo. A referência mede participantes do recorte antes de descartar escores indisponíveis e permite resultado geral sem mínimo. A API aplica a política versionada aprovada por Rosalina, com pelo menos cinco respondentes válidos por indicador, inclusive no resultado geral. Com oito submissões e quatro escores válidos, suprimir aquele indicador. Outro indicador da mesma empresa pode atender ao mínimo e ser publicado. Abaixo do mínimo total, a empresa acompanha a coleta.

Aplicar a política de publicação da plataforma a todos os instrumentos, independentemente da estratégia de cálculo. Aplicar antes de serializar respostas HTTP, gerar arquivos ou fornecer insumos à IA. Ela cobre painel, alertas, filtros, origens de exposição, temas das abertas, inventário, matriz, dossiê e exportações. Permitir até três filtros combinados. Setores protegidos ficam sem resultado próprio e sem agrupamento, inclusive em “Outros”. Podem contribuir para o total da empresa quando publicável. Nas comparações, suprimir células complementares quando a subtração do total permitir reconstituir um resultado protegido. O agrupamento em “Outros” se aplica apenas a categorias de outros campos, sujeito à mesma proteção. Testar inferência por consultas sucessivas permitidas. Para abertas, verificar o número de contribuintes e revisar menções a pessoas ou fatos identificáveis.

### Inventário e matriz de risco

O HTML especifica 12 perigos e as matrizes 4×4 e 5×5. Exibir as dimensões validadas como resultados do COPSOQ vinculados ao inventário, com as subdimensões disponíveis para rastrear o cálculo. Versionar a matriz separadamente do instrumento e homologar o mapeamento dos indicadores para perigos.

- Para cada perigo, calcular a probabilidade base pela maior proporção em vermelho entre as subdimensões associadas. Os limites de probabilidade da matriz 4×4 são 10%, 25% e 50%. Na 5×5 são 10%, 20%, 35% e 50%. A adesão abaixo de 50% gera alerta de cautela sem efeito na probabilidade. Insumo protegido ou indisponível exige estado explícito.
- Aplicar a severidade base e o agravante demonstrado quando esgotamento ou estresse atinge pelo menos 25% em vermelho, sujeitos à homologação da matriz. Relatos dos itens 20 a 23 acionam o fluxo abaixo e o nível calculado permanece vigente durante a apuração. Registrar a memória de cálculo e as revisões justificadas.
- O avaliador responde sobre abertas, observação do trabalho por AEP, rodas de conversa, indicadores e evento pontual resolvido. O ajuste de probabilidade é limitado a um nível. Duas fontes confirmatórias podem elevar a probabilidade. A redução exige evento resolvido e comprovado, ausência de confirmação e as condições de AEP e rodas previstas no protótipo. Guardar fontes, respostas e justificativa.
- Setores de cinco a nove participantes recebem alerta de baixa precisão e confirmação obrigatória. Exibir o risco por setor, probabilidade, severidade, nível, evidências, responsável pela avaliação e ações vinculadas.
- Prazos de referência do HTML: monitoramento para risco baixo, até 180 dias para moderado, até 90 dias para alto e início em até 30 dias para crítico. Documentar os parâmetros homologados com a versão do método.

### Apuração imediata de relatos

1. Na área de resultados, emitir alerta identificado como geral da empresa quando houver ao menos um relato em base publicável do respectivo indicador. O fluxo vale para assédio sexual (20), ameaças de violência (21), violência física (22) e assédio moral (23). O mínimo de cinco refere-se aos respondentes válidos do indicador. Mostrar tipo, frequência e origem no nível de detalhe permitido pela política de publicação. Preservar o anonimato em recortes, detalhes e arquivos.
2. Oferecer à pessoa autorizada a inclusão da ação obrigatória em um clique, com prazo de 15 dias, indicador “Apuração concluída e registrada, com medidas adotadas” e origem “Obrigatória por alerta de apuração imediata”. Evidenciar pendência até o registro da ação. Tratar repetições como a mesma ação e auditar sua inclusão e conclusão.
3. No inventário, marcar o perigo como “Sob apuração” em qualquer faixa calculada. O item 20 se vincula a Assédio sexual, os itens 21 e 22 a Eventos violentos e o item 23 a Assédio moral. Cada tipo tem sua própria ação, inclusive quando compartilha o mesmo perigo. Manter o estado e o nível enquanto houver apuração aberta para o perigo. Após conclusão registrada com evidência anexada, permitir avaliação técnica do nível e registrar a justificativa.
4. A interface orienta o uso dos relatos para apuração e informa a vedação de embasar medida disciplinar em dados anônimos ainda não apurados.

## 8. Cobertura das telas e contrato da API

Publicar o contrato OpenAPI no repositório `api`. Na tabela, `E` equivale a `/v1/empresas/{empresaId}`, `C` a `E/ciclos/{cicloId}` e `V` a `C/relatorios/{relatorioId}/versoes/{versaoId}`. Cada operação especifica ator, escopo, validações, formato de erro, requisitos de privacidade e evento de auditoria.

| Tela ou fluxo | Operações propostas |
|---|---|
| Login e conta | `POST /v1/auth/login`, `/v1/auth/mfa/verificar`, `/v1/auth/renovar`, `/v1/auth/logout`, `/v1/auth/ativar`, `/v1/auth/recuperar`, `/v1/auth/redefinir-senha`. `GET /v1/me` entrega ator, empresas e permissões efetivas. |
| Home da Rumo e equipe | `GET /v1/admin/painel`, `GET/POST /v1/admin/empresas`, `GET/PATCH /v1/admin/empresas/{id}`, `POST /v1/admin/empresas/{id}/bloquear` e `/reativar`. `GET/POST /v1/admin/equipe` e `PATCH /v1/admin/equipe/{id}`. Cards com empresas, plano, assinatura, adesão, datas e pendências. |
| Empresa e campos | `GET/PATCH E`, `GET/PUT E/responsavel-tecnica`. Listar, criar, alterar e desativar setores, campos e opções em `E/setores` e `E/campos-perfil`. Prever consulta de CNPJ por provedor autorizado e preenchimento manual. |
| Usuários e permissões | `GET E/usuarios`, `POST E/convites-usuarios`, `PATCH/DELETE E/usuarios/{id}`, `GET/PUT E/usuarios/{id}/permissoes`. A remoção revoga o vínculo com a empresa. |
| Autorizações à Rumo | `GET/POST E/solicitacoes-acesso`, `POST E/solicitacoes-acesso/{id}/aprovar` e `/recusar`, `GET/POST E/autorizacoes`, `POST E/autorizacoes/{id}/revogar`. |
| Instrumento e método | `GET /v1/instrumentos`, `GET /v1/instrumentos/{codigo}/versoes/{versaoId}`, `GET /v1/instrumentos/{codigo}/versoes/{versaoId}/arquivo`, `GET /v1/metodologias/{versaoId}`. A carga técnica valida a definição. A tela mostra escalas, opções, itens, agrupamentos, cortes e abertas da revisão usada. |
| Nova avaliação e ciclo | `GET/POST E/ciclos`, `GET/PATCH C`, `PUT C/configuracao-perfil`, `PUT C/populacoes`, `PUT C/revisao-programada`, `POST C/abrir`, `POST C/encerrar`, `GET C/adesao`. O contrato do ciclo identifica as revisões de instrumento e metodologia. A abertura valida o par e fixa a configuração para o restante da coleta. |
| Convites e coleta pública | `GET/POST C/lotes-convites`, `POST C/convites/{id}/revogar`, `POST /v1/publico/convites/trocar`, `GET /v1/publico/questionario`, `POST /v1/publico/submissoes`. O servidor entrega o formulário e valida a submissão pela revisão do ciclo. O link e o QR usam o mesmo convite. A pausa local dispensa associação permanente entre convite e rascunho no banco. |
| Resultados e conclusão | `GET C/resultados`, `C/resultados/filtros`, `C/resultados/comparacao-grupos`, `C/resultados/exposicoes`, `C/resultados/temas-abertos` e `C/resultados/comparacao-ciclos`. Retornar revisão de origem, indicadores, agrupamentos e alertas aplicáveis conforme a política de publicação. `GET/PUT C/conclusao` com autoria e situação de publicação. |
| Inventário | `GET C/inventario`, `PUT C/inventario/matriz`, `GET C/inventario/riscos/{id}`, `PUT C/inventario/riscos/{id}/avaliacao`, `POST C/inventario/exportacoes`. Gerar Word e Excel com dimensões vinculadas, estado de apuração, supressões e memória de cálculo publicável. |
| Plano de ação | `GET/POST C/acoes`, `GET/PATCH C/acoes/{id}`, `GET C/acoes/cronograma`, `POST C/acoes/sugestoes`, `POST C/acoes/sugestoes/aplicar`. Permitir editar e selecionar sugestões antes de aplicá-las. A operação de inclusão por alerta recebe a referência do alerta, valida a regra no servidor e reutiliza a ação existente em reenvios. |
| Evidências e atas | `GET/POST C/evidencias`, `GET C/evidencias/{id}`, `GET C/evidencias/{id}/arquivo`, `POST C/acoes/{id}/pedidos-evidencia`, `POST /v1/publico/pedidos-evidencia/trocar`, `POST /v1/publico/evidencias`. Link externo de uso único, com sete dias por padrão. |
| Relatório técnico | `GET/POST C/relatorios`, `GET/POST C/relatorios/{id}/versoes`, `GET V`, `POST V/rascunho-ia`, `PATCH V/secoes/{id}`, `POST V/secoes/{id}/aprovar`, `POST V/assinar`, `GET V/pdf`. Expor ao cliente apenas o estado até a liberação do conteúdo. |
| Fiscalização | `GET C/pasta-fiscal`, `POST C/pasta-fiscal/dossies`, `GET/POST E/acessos-fiscais`, `POST E/acessos-fiscais/{id}/revogar`, `POST /v1/publico/fiscal/autenticar`. Autorizar somente leitura nos recursos permitidos ao fiscal. |
| Auditoria e tarefas | `GET E/auditoria`, `POST E/auditoria/exportacoes`, `GET E/tarefas/{id}`, `GET E/exportacoes/{id}/arquivo`. Filtrar o CSV por período e área. Revalidar permissão e estado da empresa na entrega do arquivo. |

Definir no contrato os formatos de data, paginação, ordenação, limites de upload, concorrência nas edições e respostas para sessão expirada, permissão insuficiente, ciclo encerrado, duplicidade e resultado protegido. Entregar erros compreensíveis para o frontend e identificadores de diagnóstico sem conteúdo da pesquisa.

## 9. Frontend responsivo e documentos

- **Tema e navegação.** Basear o Bootstrap na barra lateral petróleo `#0C3B46`, destaque laranja `#E8831F`, fundo `#F4F2EE`, títulos em Bricolage Grotesque e corpo em Manrope. Preservar modo escuro, contexto de empresa e ciclo, foco visível, navegação por teclado e menu móvel. Associar rótulos textuais às cores de risco e oferecer tabela equivalente aos gráficos.
- **Resultados.** Renderizar agrupamentos, indicadores, escala, faixas e detalhes conforme os metadados do ciclo. No COPSOQ II-Br curto, exibir os sete domínios, o detalhe expansível e escores de 0 a 100 onde aplicáveis. Mostrar média, distribuição, denominador válido, comparação por campo, alertas, conclusão e estados de indisponibilidade ou proteção conforme o tipo de resultado. A comparação histórica usa o total da empresa e apresenta apenas indicadores com equivalência definida. Para o COPSOQ II-Br curto, o HTML considera variações inferiores a um ponto estáveis para exibição.
- **Plano e evidências.** Oferecer tabela com perigo, setor, medida, responsável, início, prazo, meta e situação. Derivar atraso e pendência de comprovação. Uma ação informada como concluída precisa de evidência válida para aparecer como comprovada. Permitir anexar documentos, registrar atas e verificar arquivos reais. Sinalizar treinamento como única medida em risco alto ou crítico segundo a metodologia homologada.
- **IA e relatório.** Gerar rascunhos a partir de agregados publicáveis e sínteses desidentificadas. Revisar conclusão, metodologia, resultados por setor e recomendações. Documentar instrumento, revisão, metodologia e regras efetivamente usadas na apuração. Para o COPSOQ II-Br curto, usar os resultados validados como nível principal e declarar a escala de 0 a 100, os tercis, as regras de publicação e o tratamento dos relatos. Editar uma seção aprovada exige nova aprovação. PDF interno de rascunho deve trazer marca em todas as páginas. A signatária emite a versão final com hash, data, registro, seções aprovadas e referência à apuração. Definir o mecanismo de assinatura com a Rumo antes da emissão em produção. Manter versões anteriores acessíveis a quem tem autorização.
- **Pasta fiscal.** Apresentar os dez itens do HTML: identificação e responsável técnica, metodologia, resultados, inventário, plano, ações comprovadas, participação dos trabalhadores, documentos emitidos, auditoria e revisão programada. Cada item mostra origem, pendência ou evidência. O dossiê consolida versões emitidas e anexos permitidos em PDF selecionável.
- **Amplify estático.** Publicar páginas conhecidas como `/responder/`, `/fiscal/`, `/empresa/` e `/avaliacao/`. Carregar dados privados em tempo de execução pela API Go. Testar abertura de links recebidos por mensagem, recarga direta, tema escuro, telas estreitas e vencimento de credenciais. O pacote publicado contém apenas ativos públicos.

## 10. Sequência de implementação no outro PC

Clonar os três repositórios como pastas irmãs em um mesmo diretório e abrir o diretório pai no Codex. Verificar a presença dos anexos desta seção de referências no clone, inclusive dos três PDFs. Trabalhar por etapa. Em cada entrega, conferir o critério de aceite e identificar os commits correspondentes em cada repositório afetado.

| Etapa | Entrega | Critério de conclusão |
|---|---|---|
| 1. Reproduzir a referência | Conferir versão declarada, hash, arquivos e cobertura do HTML. Executar o verificador Python. | 21/21 casos passam e as diferenças documentadas entre o HTML e as decisões de produto têm critério de aceite. |
| 2. Subir a base local | Dockerfiles, Compose de integração, migrations iniciais, conexão Go–PostgreSQL, frontend e contrato OpenAPI inicial. | Em instalação limpa, sobem API, app, banco e worker. Migrations e testes de saúde passam. |
| 3. Isolar contas | Implementar empresas, identidade, MFA, papéis, autorização, suspensão e auditoria básica. | Duas empresas isoladas na API e no banco. Bloqueio e reativação pelo admin global com histórico. |
| 4. Calcular e proteger | Implementar importação versionada e estratégias Go. Carregar o COPSOQ II-Br curto, seus 21 casos e o CSV sintético. Validar também uma definição fictícia com outra estrutura e escala. | Python e Go concordam nos 21 casos de referência. A definição fictícia usa a mesma rotina de importação e apuração. Os testes de publicação cobrem o mínimo de cinco no total e por indicador, com Manutenção protegida individualmente. |
| 5. Coletar | Nova avaliação em quatro etapas, congelamento das revisões, convites, QR, consentimento, formulário móvel por definição, pausa, retomada, envio único e adesão. | Uma empresa consegue fazer a coleta sem cadastrar trabalhadores. Duas abas com o mesmo convite produzem uma submissão. A revisão vinculada ao ciclo governa o formulário e a validação. |
| 6. Apurar e revisar | Painel por instrumento, filtros, conclusão, exposição, alerta, inventário, matrizes e confirmação técnica. | Cada número publicado tem denominador e memória de cálculo reproduzível. A API aplica supressões e entrega o estado “Sob apuração” quando aplicável e publicável. |
| 7. Completar a primeira avaliação | Rascunho por IA, revisão, assinatura, PDF, plano tabular, ação obrigatória de apuração, evidências, devolutiva e auditoria de acessos e exportações. | Com massa fictícia, percorrer do convite à emissão e da abertura do alerta à conclusão com evidência. O cliente acessa somente conteúdo liberado. |
| 8. Cobrir os fluxos complementares | Pasta fiscal e dossiê, auditor externo, autorizações por área, envio externo de evidência, cronograma, sugestões, Word/Excel/CSV e comparação histórica. | Cada ação funcional prevista no HTML tem operação real, ator autorizado e teste de aceite. |
| 9. Homologar e publicar | Validar com Rosalina a implementação das regras confirmadas e dos demais parâmetros metodológicos, testar carga e navegação, validar assinatura, restaurar backup e implantar em homologação AWS antes de produção. | Parâmetros homologados registrados por versão. Avaliação completa reproduzível em homologação e recuperação verificável do banco, relatório e evidências. |

## 11. Testes de aceite

| Cenário | Resultado esperado |
|---|---|
| Uma empresa conhece o ID de um recurso de outra | Leitura, escrita, exportação, tarefa e download são negados. Chaves compostas impedem vínculos cruzados. |
| Empresa suspensa com sessões e links emitidos | As operações passam a respeitar o bloqueio. Reativar mantém histórico e vencimentos das credenciais. |
| Pré-visualização do convite, duas abas, duplo clique ou falha de rede | A pré-visualização preserva o convite. Um único envio é contabilizado. A repetição recebe estado coerente. |
| Inspeção das tabelas, logs e auditoria | Nenhuma relação direta convite–submissão, segredo de convite, corpo das respostas ou lista nominal de trabalhadores nas trilhas de coleta. |
| Quatro respostas válidas na empresa, em um setor ou em uma dimensão | Suprimir o indicador em todas as saídas. Incluir cenário com oito submissões e apenas quatro escores válidos para uma dimensão. Com dois setores protegidos, confirmar ausência de agrupamento mesmo se a soma atingir cinco. Testar inferência por subtração e por consultas permitidas. |
| Importação dos 60 fictícios | D01 tem média geral 51,46. V06/D13 tem média 60,00, em atenção, e distribuição individual de 65% favorável, 0% atenção e 35% crítica. V10 tem média 51,56. Manutenção tem quatro respondentes, fica sem resultado próprio e pode contribuir para o total da empresa quando publicável. |
| Hierarquia, cálculo e escala | Os 40 itens e as 23 subdimensões pertencem uma única vez ao mapeamento das 11 dimensões validadas. Os sete títulos ficam sem escore e sem cor. Subdimensões aparecem no detalhe. C19 produz 62,50 e mantém soma 10 na memória interna. V11 mostra os quatro tipos e a operação de cálculo recusa o escore conjunto. Painel e relatório exibem escores na escala 0–100. |
| Segundo instrumento fictício, disponível só em teste | Usar uma estrutura de blocos diferente e uma soma como escore publicado, com escala, cortes e mapeamento próprios. Percorrer importação, ciclo, formulário, submissão, cálculo, publicação, inventário, relatório e exportação pelas mesmas operações. Conferir valores conhecidos e proteção de recortes. Reutilizar o código local 20 com outro significado e verificar que ele segue o mapeamento do instrumento fictício. |
| Nova revisão e comparação histórica | Abrir um ciclo, publicar nova revisão com escala ou corte diferente e abrir outro ciclo. O primeiro continua com o formulário, cálculo, inventário e documento da revisão vinculada. A comparação histórica só inclui indicadores com equivalência definida. Rejeitar código de indicador inexistente no mapeamento, método incompatível e estratégia de cálculo desconhecida na validação da definição. |
| Exposição, respostas ausentes e abertas | Testar zero, omissão, item 1B, limites e origem múltipla. Alterar um relato para “Não” elimina origens incompatíveis. Os quatro textos abertos permanecem após envio e obedecem às regras de publicação. |
| Matrizes e ações | Verificar que a probabilidade segue as subdimensões associadas, inclusive quando a dimensão validada teria proporção em vermelho diferente. Variar a adesão em torno de 50% mantendo os escores e confirmar que apenas o alerta de cautela muda. Cobrir limites das matrizes, agravante, ajuste máximo, baixa precisão e ação concluída sem anexo comprobatório. |
| Apuração imediata | Testar isoladamente os itens 20, 21, 22 e 23 com um relato e base suficiente. Confirmar alerta com agregados permitidos, ação obrigatória de 15 dias e perigo “Sob apuração” com nível preservado. Repetir o clique e confirmar uma ação por tipo no ciclo, com indicador, origem e auditoria. Testar os itens 21 e 22 juntos e a conclusão com evidência de apenas um dos tipos. Cobrir supressão do alerta em base protegida. |
| Relatório e acesso fiscal | Cliente e fiscal não recuperam rascunho interno por URL direta. Somente a responsável técnica designada assina. Retificação preserva PDF anterior. Revogar ou expirar acesso impede novas consultas e entregas de arquivos. |
| Instalação e restauração | Partindo dos clones, subir o ambiente, aplicar migrations e restaurar uma cópia. Conferir um PDF assinado e suas evidências pelos hashes registrados. |

## 12. Implantação e operação AWS

**Desenvolvimento.** Executar Next.js, API Go, worker e PostgreSQL em contêineres. Usar volume persistente para dados locais, recarga de código e variáveis de ambiente documentadas. A mesma imagem Go pode iniciar API e worker com comandos distintos.

**Produção.** Publicar o frontend estático no Amplify. Proposta inicial de uma instância Lightsail com Docker Compose para proxy HTTPS, API, worker e PostgreSQL com volume persistente. Manter a porta do banco na rede privada dos contêineres. Esta topologia concentra API e banco na mesma instância e tem um ponto único de falha. Usar armazenamento privado independente para documentos e cópias de segurança.

**Publicação coordenada.** O CI de `bd` valida migrations. O de `api` executa o verificador Python, a suíte Go e integração com PostgreSQL. O de `app` valida tipos, build estático e jornadas. Publicar imagens com referências imutáveis, executar migrations uma vez por release, verificar saúde e registrar as três revisões homologadas. Para reversão de aplicação, preservar compatibilidade com o esquema já aplicado.

**Recuperação e monitoramento.** Guardar backups criptografados fora da instância. Definir retenção, tempo de recuperação e perda de dados tolerável com a operação. Ensaiar restauração conjunta do banco e dos objetos. Monitorar disco, disponibilidade, conexões, fila, falhas de geração de documentos e idade do último backup. Excluir segredos de convite, respostas, textos livres e conteúdo de anexo dos logs de aplicação e infraestrutura.

**Demonstração final.** Executar o percurso com duas empresas fictícias. A primeira usa os 60 respondentes e chega ao relatório emitido e à pasta fiscal. A segunda tem quatro respondentes, acompanha a coleta e permanece sem indicadores publicáveis. Demonstrar troca de empresa pelo admin global, isolamento da PJ, resposta anônima, bloqueio manual e revogação do acesso fiscal.
