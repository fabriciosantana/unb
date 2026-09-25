# Registro da pesquisa bibliográfica

Data: 25 set. 2026. Fluxo ARS-Codex: `deep-research`, modo `lit-review`, adaptado ao produto solicitado (bibliografia ABNT/BibTeX e PDFs). Escopo obtido do enunciado local, lido integralmente por extração textual. Não foi necessário formular uma nova pergunta de pesquisa: o objetivo é reunir fundamentos para executar o projeto definido pelo professor.

## Estratégia e critérios

Busca orientada por tópicos, sem restrição inicial de ano, com inclusão de trabalhos seminais e livros atualizados. Idiomas: português e inglês. Fontes consultadas: arXiv, ACL Anthology, JMLR, páginas oficiais dos autores/livros, OpenAI, GitHub de Karpathy, MEC/NUPILL, ABL, IEEE e bibliotecas universitárias. A busca foi encerrada após cobertura dos tópicos do enunciado e das lacunas metodológicas identificadas; isso não prova saturação de toda a literatura.

Incluir: fonte original ou institucional com relação direta a matemática básica, modelos de linguagem, tokenização, arquitetura, treinamento, avaliação, corpus ou extensão de QA. Aceitar livros, artigos, preprints, relatórios técnicos e recursos oficiais, distinguindo seus papéis. Preferir PDFs publicados pelos autores, repositórios científicos ou instituições. Excluir: tutoriais não oficiais redundantes, aplicações sem relação direta, cópias sem proveniência e referências sem existência confirmada.

## Consultas e encadeamento

| Bloco | Consulta ou rota executada | Resultado usado |
|---|---|---|
| Enunciado | Extração de `projeto1-rnap-2026_2.pdf` | nanoGPT, Vaswani, GPT-3, tutorial Karpathy, artigo IEEE, corpus Machado |
| Arquitetura | `site.arxiv.org Attention Is All You Need 1706.03762`; `site.arxiv.org Language Models are Few-Shot Learners 2005.14165` | Depósitos oficiais dos dois artigos exigidos |
| GPT-2/código | `site.openai.com language models unsupervised multitask learners GPT-2 pdf`; `site.github.com/karpathy/nanoGPT README` | Relatório GPT-2 e código-base |
| Livros | Acesso direto a deeplearningbook.org, d2l.ai e página SLP3 Stanford | Fundamentos, matemática, PLN e avaliação |
| Tokenização e dados | Acesso direto a ACL P16-1162, D18-2012 e 2022.acl-long.577 | BPE, SentencePiece e deduplicação |
| Componentes e treino | Acesso direto aos depósitos arXiv 1607.06450, 1412.6980, 1711.05101 e 1606.08415; JMLR srivastava14a | LayerNorm, Adam, AdamW, GELU e dropout |
| Avaliação/escala | Acesso direto a 1904.09751, 2001.08361 e 2203.15556 | Decodificação e limites de extrapolação de escala |
| Extensões | Acesso direto a 2005.11401, 2106.09685, 2203.02155 e ACL 2020.acl-main.740 | RAG, LoRA, instruções e adaptação de domínio |
| Panorama | Acesso direto a 2303.18223 | Survey como consulta complementar |
| Corpus e formatação | Consulta institucional delegada, com MEC, ABL, BBM/USP, IEEE, UFU e UFES | Proveniência das obras, modelo de artigo e atualização ABNT |

A página ACL 2020.acl-main.703 (BART) foi inspecionada, mas excluída da biblioteca final por ser arquitetura seq2seq fora do núcleo GPT-2; o artigo RAG basta para contextualizar a extensão. BBM/USP foi identificada como fonte alternativa para conferir edições, mas não adicionada como requisito teórico. Resultados secundários de buscadores não foram usados como evidência quando existia fonte primária.

Não foram coletados totais de resultados dos índices nem executada exportação exaustiva de bases. Por isso, não se apresenta fluxograma PRISMA, contagem fictícia de registros triados ou alegação de revisão sistemática. Os itens efetivamente incluídos estão em `fontes.json`.

## Verificação e decisões bibliográficas

- Metadados dos artigos arXiv foram obtidos das páginas oficiais; entradas ACL foram complementadas pelo BibTeX oficial. O coletor não usa clientes Semantic Scholar/OpenAlex/Crossref nem envia o enunciado a serviços externos.
- Artigos arXiv usam ano da submissão inicial e versão consultada em nota. Isso evita combinar ano de anais com volume/páginas não verificados. Um depósito arXiv não é apresentado, por si só, como comprovação de revisão por pares.
- Versões arXiv e versões publicadas do mesmo trabalho não foram contadas como fontes distintas. Livros online evolutivos têm data de acesso e snapshot local.
- Links de portais sem data editorial confirmada ficam sem ano no BibTeX e com `[s. d.]` na lista ABNT. Não se inventou ano de publicação a partir da data de acesso.
- PDFs tiveram assinatura `%PDF-`, contagem de páginas e hash conferidos; sidecars da ferramenta `pdf_read_preflight.py` registram a verificação estrutural ARS. Erros e avisos não são convertidos em PASS.
- A inspeção temática usou resumos, introduções e seções selecionadas. Não houve auditoria independente de todas as afirmações dos artigos, de retratações ou de conflitos de interesse. Relatórios de empresas e textos dos desenvolvedores são identificados como tais; sua origem não garante generalização.
- A curadoria temática e sua revisão foram feitas no contexto principal; um subagente pesquisou corpus e normas. Isso não constitui revisão científica cega ou validação entre famílias de modelos.

## Qualidade e cobertura

Livros servem à aprendizagem e organização dos conceitos; artigos originais fundamentam operações e métodos; repositório e vídeo documentam a implementação; portais institucionais fundamentam proveniência e formato. A biblioteca é predominantemente computacional e de métodos, de modo deliberado, por causa do objetivo do projeto. Uma análise crítica da obra de Machado ou de sua recepção literária demandaria outra bibliografia; nenhuma qualidade estética ou compreensão literária é inferida apenas de perplexidade.

Há evidência em escalas e domínios diferentes. Kaplan/Hoffmann oferecem recomendações de alocação de computação distintas; diferenças de regimes experimentais impedem escolher uma fórmula por autoridade. GPT-3 documenta capacidades de modelos grandes; não garante comportamento de um GPT pequeno. LoRA trata eficiência de adaptação; RAG trata acesso a passagens; ambos podem ser combinados, mas resolvem problemas diferentes. Essas são limitações de aplicabilidade que o roteiro torna explícitas.

## Reprodução dos artefatos

Os scripts `coletar_fontes.py` e `finalizar_bibliografia.py` registram a seleção e a transformação dos metadados. Dependências utilizadas: Python, requests, pypdf e bibtexparser 2; o finalizador referencia o caminho local da skill ARS instalada. Eles são auxiliares desta coleta, não instaladores portáteis. Antes de repetir a coleta em data futura, preserve `fontes.json`, pois URLs sem versão fixa podem entregar revisões novas. A lista `fontes.json` final e os hashes representam esta entrega.

O material em ABNT foi produzido segundo a NBR 6023:2025, consultando os exemplos públicos da UFU e a confirmação institucional da edição. O texto integral da norma não foi redistribuído. Para o artigo da disciplina, prevalece o formato IEEE solicitado no enunciado.
