# Avaliação do Projeto Individual 1 — Machado de Assis

Data: 26 de setembro de 2026.

## Parecer e nota

**Nota atribuída ao estado da entrega antes das implementações registradas ao final: 6,5/10 (parecer histórico, anterior ao esclarecimento do professor sobre a amostra do corpus).**

Trata-se de uma avaliação técnica simulada na perspectiva de um professor da disciplina, baseada exclusivamente nos requisitos de `projeto1-rnap-2026_2.pdf`. Não é a nota oficial do professor. O enunciado não fornece pesos; a distribuição abaixo é uma rubrica explícita deste parecer. Depois deste parecer, o professor esclareceu que não é necessário reunir todas as obras e que uma boa amostra útil ao treinamento e ao aprendizado é suficiente. Portanto, a penalização por não demonstrar cobertura integral e a recomendação 2 abaixo são históricas e não devem ser consideradas pendências atuais. A apresentação oral não foi observada e seus pontos permanecem não demonstrados, sujeitos à avaliação presencial. Sua ausência no diretório não comprova que o estudante não tenha apresentado.

O projeto tem mérito técnico: construção de corpus rastreável, quatro notebooks organizados, uso do nanoGPT em commit fixado, treinamento de duas configurações, checkpoints recuperáveis e uma comparação quantitativa pertinente. Entretanto, o artigo tem três páginas em vez de seis, a abrangência do corpus não satisfaz de maneira comprovada a exigência de todos os conteúdos originais dos livros e os artefatos locais do baseline estão com nomes incompatíveis com seus conteúdos. Há também descrições metodológicas que não correspondem exatamente ao código.

## Requisitos usados e pontuação

| Requisito do enunciado | Peso | Nota | Fundamentação |
|---|---:|---:|---|
| Implementação e treinamento de modelo similar ao GPT-2 com nanoGPT | 2,0 | 2,0 | Dois checkpoints carregados em CPU, com arquiteturas 6/6/384 e 4/4/256 e `iter_num=5000`; notebooks usam a base indicada. |
| Arquivo-texto com todos os conteúdos originais dos livros | 2,0 | 1,1 | Arquivo mestre presente e hash correto, mas o manifesto declara cobertura bibliográfica não comprovada; existem lacunas no cruzamento de obras. |
| Avaliação e comparação dos resultados | 2,0 | 1,2 | Tabela com duas condições e protocolo comum; rastreabilidade do resultado do baseline e descrição do procedimento precisam de reparos. |
| Artigo IEEE de seis páginas com descrição do problema | 1,5 | 0,7 | Problema descrito, PDF em duas colunas; apenas três páginas e autoria/matrícula ainda em branco. |
| Fundamentação nos textos indicados e elaboração orientada pelo tutorial | 1,0 | 0,7 | Vaswani, Brown e tutorial citados; explicação técnica muito breve. Não foi inferido que o estudante assistiu ao vídeo apenas por haver citação. |
| Código com identificação de partes próprias e de terceiros; Colab preferencial | 0,5 | 0,4 | Há commit, origem e atribuição geral; faltam mapeamento claro por componente e instruções consolidadas de entrega. |
| Discussão de extensão para perguntas no universo Machado de Assis | 0,5 | 0,4 | Proposta de recuperação e geração presente; falta explicar melhor a adaptação do gerador atual. |
| Apresentação oral de cinco minutos sobre resultados e extensões | 0,5 | 0,0* | Não observada; nenhum material de apresentação localizado. Pontuação reservada até demonstração. |
| **Total no estado auditado** | **10,0** | **6,5** | **Nota provisória da entrega demonstrável.** |

Os critérios não são duplicados: problemas de conteúdo da avaliação foram contabilizados na comparação; extensão e fundamentação foram avaliadas separadamente da formatação do artigo.

## Evidências conferidas

- Enunciado integral: `projeto1-rnap-2026_2.pdf`.
- Artigo no snapshot inicial: `../latex/ARTIGO_PROJETO1_RASCUNHO.tex` e `../latex/out/ARTIGO_PROJETO1_RASCUNHO.pdf`. A conferência estrutural daquele PDF passou, com três páginas; a tabela de situação posterior registra a versão ampliada.
- Notebooks de construção, preparação, baseline e modelo reduzido, incluindo configuração, exportação e avaliação.
- `dados/manifesto_corpus.json`, `dados/cruzamento_bibliografia_abl.csv`, `dados/modelagem/manifesto_modelagem.json` e código de auditoria/particionamento.
- Arquivo mestre: SHA-256 consistente com o manifesto. Os JSONL têm 181, 30 e 31 documentos; os hashes dos textos correspondem aos registros de cada documento.
- Checkpoints carregados com `torch.load(..., map_location='cpu', weights_only=True)`. Ambos registram iteração 5.000 e configurações compatíveis com as condições descritas.
- JSON válido do modelo reduzido: perda `1.3862289541959762`, perplexidade `3.9997383808602875`, 200 lotes de avaliação de tamanho 32.
- Baseline: os valores de teste `1,2399` e `3,455` constam no artigo e nas saídas fornecidas na conversa, mas o arquivo local chamado `resultados_baseline.json` não é JSON. A auditoria atual não recalculou essas métricas.
- Arquivos e checkpoints foram inspecionados sem novo treinamento. Não houve alteração do artigo, dos notebooks ou dos artefatos experimentais nesta avaliação.

### Inconsistência concreta dos arquivos do baseline

Na pasta `experimentos/gpt_caractere_nanogpt/`:

| Nome atual | Conteúdo observado |
|---|---|
| `amostra_gerada.txt` | Checkpoint binário de 129.363.420 bytes, idêntico por SHA-256 a `out/ckpt.pt`. |
| `config_train_machado_char.py` | Texto literário gerado, começando com “Era uma coisa de Flávio”. |
| `meta.pkl` | Texto da configuração Python, com arquitetura 6/6/384. |
| `resultados_baseline.json` | Serialização pickle do vocabulário; não é JSON UTF-8. |
| `out/ckpt.pt` | Checkpoint PyTorch que foi carregado e inspecionado. |

Isso não prova que o treino esteja errado. Demonstra que a cópia local dos artefatos está organizada incorretamente e que o resultado estruturado do baseline precisa ser recuperado. As confirmações anteriores desta conversa, baseadas apenas em nomes e tamanhos, foram insuficientes.

## Recomendações detalhadas

### 1. Recuperar os artefatos corretos do baseline — prioridade alta

**Por quê:** a avaliação comparativa exigida precisa estar apoiada em resultados acessíveis. A organização atual impede carregar o tokenizer pelo nome esperado e verificar o JSON do baseline.

**Como implementar:** conferir a listagem do ZIP original preservado no Drive e extraí-lo primeiro em um diretório separado. Validar conteúdo e extensão antes de substituir qualquer arquivo. Preservar o checkpoint confirmado.

**O que fazer:** restaurar `amostra_gerada.txt` como texto, `config_train_machado_char.py` como configuração, `meta.pkl` como tokenizer e `resultados_baseline.json` como JSON. Conferir configuração, vocabulário e métricas. Se o JSON original não existir, repetir somente a avaliação do checkpoint existente com os mesmos dados/protocolo, registrando a nova execução como tal. Não fabricar um JSON como se fosse saída original. Critério de conclusão: os quatro arquivos podem ser lidos com seus leitores apropriados e os números da tabela são rastreáveis.

### 2. Documentar a composição e os limites da amostra — recomendação histórica, não pendência

**Por quê (registro do entendimento inicial):** este parecer interpretou que seria necessário comprovar todos os conteúdos originais dos livros. O professor esclareceu posteriormente que a entrega pode usar uma boa amostra útil ao treinamento e ao aprendizado; cobertura exaustiva não é requisito. A auditoria continua útil para descrever composição e limites, mas não para exigir a incorporação de obras ausentes.

**Como implementar:** manter a matriz e o manifesto como documentação de proveniência e representatividade da amostra, sem classificar lacunas bibliográficas como descumprimento. Para qualquer material novo, registrar fonte, edição, componentes e deduplicação.

**O que fazer:** nenhuma expansão ou novo treinamento é necessário por motivo de cobertura integral. Preservar a descrição honesta da amostra e, caso a curadoria seja ampliada voluntariamente, versionar dados e partições e repetir as condições antes de atribuir resultados à nova versão.

### 3. Completar e revisar o artigo IEEE — recomendação histórica sobre conteúdo e identificação

**Por quê (entendimento inicial):** o PDF examinado naquele momento tinha três páginas e campos de identificação pendentes. O professor esclareceu posteriormente que seis páginas é o limite máximo, não uma meta de extensão. A recomendação de preencher páginas foi superada; continuam pertinentes a clareza, a fundamentação e o preenchimento dos dados de identificação.

**Como implementar:** preservar o formato IEEE e revisar a coerência entre método, métricas, resultados e conclusões. Não ampliar o texto apenas para alcançar uma quantidade de páginas.

**O que fazer:** preencher a matrícula, conferir a diagramação e garantir que a versão final esteja dentro do máximo de seis páginas. O PDF atual com cinco páginas está dentro do limite; não há página faltante por esse motivo.

### 4. Corrigir a documentação da seed e do checkpoint — prioridade alta

**Por quê:** os notebooks declaram `SEED=20260925`, mas esse valor não é passado ao subprocesso de treino. No commit fixado, `train.py` usa `1337` em execução de uma GPU. Com `always_save_checkpoint=True`, `ckpt.pt` é sobrescrito nas avaliações; não há garantia de que seja o melhor checkpoint, apesar dessa expressão na introdução dos notebooks. Fonte: [train.py no commit utilizado](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/train.py).

**Como implementar:** descrever o que efetivamente ocorreu, distinguindo preparação, treino, avaliação e geração. Não alterar retroativamente a configuração dos experimentos para aparentar uma execução diferente.

**O que fazer:** registrar preparação `20260925`, treino `1337`, amostragem de teste `20260926` e geração `20260925`, conforme o código disponível. Identificar os pesos como checkpoint da iteração 5.000. A inspeção encontrou o campo de validação em ambos os checkpoints, aproximadamente `1,2470` e `1,3840`; seu nome `best_val_loss` não garante mínimo histórico nesta configuração. Corrigir a narrativa nos notebooks, artigo e relatório. Essa correção documental não exige novo treinamento.

### 5. Especificar o protocolo de comparação e limitar as conclusões — prioridade alta

**Por quê:** o artigo omite detalhes existentes no código. A perda foi estimada em janelas amostradas, não calculada por varredura integral de todos os documentos. Alteraram-se simultaneamente profundidade, número de cabeças e dimensão; isso permite comparar duas configurações, mas não identificar isoladamente o efeito de cada hiperparâmetro.

**Como implementar:** descrever as constantes e as três alterações arquiteturais; explicar a amostragem de 200 lotes de 32 janelas com contexto 256, a inclusão de EOS/UNK e a possibilidade de janelas cruzarem limites de documentos concatenados. Especificar a unidade da perda e a relação `PPL = exp(loss)`.

**O que fazer:** incluir essas informações na metodologia e rotular os resultados como estimativas amostradas de teste. Explicar que o orçamento fixado foi o número de atualizações/exemplos, não tempo ou FLOPs iguais. Limitar conclusões a estas duas execuções. Não afirmar redução medida de tempo/memória apenas por haver menos parâmetros. Registrar que o teste do baseline já era conhecido antes da definição da segunda condição; evitar apresentá-la como seleção totalmente prévia ao teste. Critério de conclusão: outro leitor consegue reproduzir a avaliação e interpretar corretamente os percentuais.

### 6. Definir a convenção de contagem de parâmetros — prioridade média

**Por quê:** a contagem impressa pelo nanoGPT e citada no artigo exclui os embeddings posicionais. Sem essa explicação, “número de parâmetros” parece indicar o total.

**Como implementar:** usar a mesma convenção para ambos e informar a exclusão, ou publicar o total de parâmetros únicos incluindo posições. O compartilhamento entre embeddings de tokens e cabeça de saída deve ser contado uma vez.

**O que fazer:** os tensores locais indicam 10.678.272 e 3.185.664 parâmetros sem posições; incluindo posições, 10.776.576 e 3.251.200. Manter os 10,68 M e 3,19 M com rótulo explícito, ou atualizar tabela e percentuais com os totais. Conferir toda a documentação após a escolha.

### 7. Desenvolver a fundamentação e a análise das amostras — prioridade média

**Por quê:** os artigos exigidos estão citados, mas a explicação permanece breve para demonstrar domínio do modelo e sustentar a análise comparativa. O relatório comenta geração sem mostrar exemplos lado a lado.

**Como implementar:** explicar atenção causal, múltiplas cabeças, posições, bloco feed-forward, normalização, conexões residuais e objetivo autorregressivo, relacionando-os à implementação. Distinguir Transformer encoder–decoder de Vaswani, decoder-only e aprendizagem em contexto discutida em GPT-3.

**O que fazer:** adicionar uma equação de atenção e do objetivo, se úteis à explicação, e dois trechos já gerados com o mesmo prompt “Era ”, temperatura 0,8 e top-k 40. Comentar erros concretos de concordância, repetição e continuidade sem generalizar uma amostra para qualidade literária global. Não é necessário acrescentar uma revisão bibliográfica extensa nem repetir experimentos para cumprir esta recomendação.

### 8. Consolidar autoria do código e acesso à entrega — prioridade média

**Por quê:** o enunciado exige descrições claras do código alheio e próprio e prefere Colab. A atribuição geral é positiva, mas o avaliador deve localizar facilmente cada contribuição e executar a entrega.

**Como implementar:** criar uma seção curta de procedência: `model.py`, `train.py` e configuração inspirada no exemplo de Shakespeare pertencem à base de Karpathy; os notebooks integram preparação, auditoria, partições, avaliação e exportação. Qualificar adaptações e a participação efetiva do estudante.

**O que fazer:** incluir links dos Colabs do autor, ordem 01–04, acesso aos dados e artefatos e instruções de configuração em uma página de entrada. Exportar notebooks executados ou ligar suas versões executadas. O 03 local conserva saídas de teste CPU; o 04 local não contém saídas. Isso não invalida os checkpoints, mas dificulta a inspeção. Não há obrigação de hospedar checkpoints grandes no Git nem de usar Colab como plataforma exclusiva.

### 9. Tornar concreta a proposta de perguntas e respostas — prioridade média

**Por quê:** a seção de extensão atende à direção pedida, mas adicionar passagens ao prompt não estabelece que estes pequenos modelos consigam seguir instruções, citar fontes ou responder perguntas.

**Como implementar:** descrever separadamente indexação por obra/trecho, recuperação, escolha/adaptação do gerador e avaliação da resposta. Explicar a limitação do contexto de 256 caracteres e como seria ampliado ou contornado.

**O que fazer:** apresentar uma pergunta ilustrativa com evidência e resposta esperadas, claramente marcada como proposta; explicar se o gerador seria adaptado com exemplos de perguntas/respostas ou substituído por um modelo instrucional. Indicar verificação de suporte textual e abstenção. O enunciado pede discutir como estender: implementar RAG ou treinar um chatbot não é necessário.

### 10. Preparar e realizar a apresentação oral — requisito pendente de avaliação

**Por quê:** o enunciado exige cinco minutos em sala, destacando melhores resultados e possibilidades futuras. Os arquivos atuais não permitem avaliar a apresentação.

**Como implementar:** preparar um roteiro cronometrado: problema/corpus (45 s), método (60 s), comparação (90 s), limites (45 s) e extensão/conclusão (60 s).

**O que fazer:** ensaiar cinco minutos, explicar por que o baseline obteve menor perda e qual economia paramétrica a variante oferece, mostrar exemplos e reconhecer limites. Slides são um recurso sugerido, não um requisito explícito. A comprovação final depende da apresentação presencial, não apenas da existência de slides.

## O que não é exigido para alcançar a nota máxima

Não se exige atingir perplexidade arbitrária, reproduzir a escala do GPT-2, empregar BPE, realizar fine-tuning, implementar RAG, executar um terceiro modelo, testar múltiplas seeds ou produzir novidade científica. O enunciado pede comparações, mas não define um número obrigatório de modelos; as duas condições existentes constituem uma comparação pertinente. Múltiplas execuções, curvas completas e métricas de custo seriam úteis, mas não são requisitos autônomos do PDF.

A prioridade indicada naquele parecer é histórica e parte de um entendimento depois corrigido sobre corpus e extensão do artigo. Os pontos ainda úteis são descrever fielmente os procedimentos, completar dados de identificação e realizar a apresentação; a amostra é aceitável e o PDF atual respeita o limite de páginas.

## Situação após implementação — 26 de setembro de 2026

Esta seção atualiza o estado das recomendações sem substituir a nota 6,5/10, que se refere ao retrato auditado antes das mudanças e não é uma nova nota oficial.

| Recomendação | Situação | Evidência / pendência |
|---|---|---|
| 1. Artefatos baseline | Parcialmente concluída | Arquivos locais renomeados a partir da inspeção de conteúdo; tokenizer, configuração e amostra restaurados. A reavaliação independente em CPU (200×32 janelas) reproduziu loss 1,239860 e PPL 3,455131, arredondando aos valores do Colab. Registro em `reevaluacao_baseline_cpu.json`; o ZIP original do Drive e logs históricos não foram localizados. Cópia redundante de 129.363.420 bytes foi removida após SHA-256 idêntico ao checkpoint preservado. |
| 2. Cobertura do corpus | Adequada ao escopo esclarecido | Amostra, composição e limites documentados; professor confirmou que não é necessário reunir todas as obras. Não há pendência de completar a lacuna de *Correspondência* nem de repetir os treinamentos por esse motivo. |
| 3. Artigo IEEE | Dentro do limite; identificação pendente | PDF recompilado em duas colunas com cinco páginas em `../latex/out/ARTIGO_PROJETO1_RASCUNHO.pdf`, dentro do máximo de seis páginas esclarecido pelo professor. Nome preenchido; matrícula ainda precisa de confirmação/preenchimento. |
| 4. Seeds e checkpoint | Implementada documentalmente | Notebooks, artigo, relatório e roteiro distinguem seed efetiva do treino (1337 no commit fixado/uma GPU) das seeds de preparação, avaliação e geração; checkpoint identificado como iteração 5000 sem afirmar mínimo histórico de validação. |
| 5. Protocolo comparativo | Implementada documentalmente | Artigo e relatório descrevem as 200 janelas amostradas por 32, contexto 256, unidade em símbolos do vocabulário char-level (incluindo EOS/UNK), amostragem no fluxo concatenado, mudança simultânea de três dimensões e limite do orçamento em atualizações. |
| 6. Parâmetros | Implementada | Artigo/relatório distinguem contagem do log sem posições (10.678.272; 3.185.664) e totais únicos com posições (10.776.576; 3.251.200). |
| 7. Fundamentação/amostras | Implementada no artigo | Atenção causal, objetivo, perplexidade, trechos de saída e erros específicos analisados com limites explícitos. |
| 8. Autoria/acesso | Parcial | Página `LEIA-ME-ENTREGA.md` descreve procedência e ordem dos quatro notebooks. Links de compartilhamento dos Colabs ainda dependem do autor. |
| 9. Extensão QA | Implementada como proposta | Artigo descreve recuperação por obra/trecho, evidência, citação/abstenção e avaliação separada; nenhuma funcionalidade RAG é alegada como implementada. |
| 10. Apresentação | Preparação concluída; realização pendente | `ROTEIRO_APRESENTACAO_5_MIN.md` foi criado. Ensaiar e apresentar em sala continua sendo responsabilidade do estudante e não pode ser atestado aqui. |

Itens dependentes de informação ou ação do estudante: matrícula, links dos Colabs e apresentação oral. A matriz ABL lista “Correspondência, 1932”, mas a ausência do texto na amostra não constitui pendência segundo o esclarecimento do professor. Este arquivo preserva recomendações e pontuações de um estado anterior; para a organização atual, consulte também `MEMORIA_TRABALHO.md` e `AVALIACAO_COBERTURA_CORPUS.md`.
