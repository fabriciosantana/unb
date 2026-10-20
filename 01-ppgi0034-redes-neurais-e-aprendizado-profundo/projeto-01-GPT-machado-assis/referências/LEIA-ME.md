# Bibliografia de estudo — GPT com Machado de Assis

Pesquisa realizada em 25 de setembro de 2026 a partir de `../projeto1-rnap-2026_2.pdf`. Esta é uma revisão bibliográfica orientada ao projeto, com roteiro de estudo e fontes verificáveis; não é uma revisão sistemática exaustiva nem o artigo final da disciplina.

## Arquivos

- [Trabalhos relacionados com Machado de Assis](trabalhos-relacionados-machado.md): sete fontes adicionais, comparação de evidências, BibTeX/ABNT próprios e PDF do TCC de Milton Leal.

- [bibliografia.bib](bibliografia.bib): biblioteca BibTeX com autores completos, URLs, identificadores e caminhos dos PDFs.
- [bibliografia-abnt.md](bibliografia-abnt.md): referências formatadas em ABNT NBR 6023:2025.
- [inventario.md](inventario.md): tema, prioridade e situação de cada arquivo.
- [fontes.json](fontes.json): metadados, versões, URLs de download e hashes SHA-256.
- [metodo-da-pesquisa.md](metodo-da-pesquisa.md): busca, critérios, verificação e limitações.
- PDFs nomeados pela chave bibliográfica, por exemplo, `radford2019.pdf`.

O enunciado exige um artigo de **seis páginas em formato IEEE de duas colunas**, código preferencialmente em Colab, identificação das partes reutilizadas e apresentação de cinco minutos. A bibliografia ABNT atende ao pedido de estudo; para o artigo, use o mesmo `.bib` com o estilo do template IEEE. Não é necessário citar toda esta biblioteca no artigo: cite as fontes que fundamentam as decisões e afirmações efetivamente usadas.

## Ordem de leitura sugerida

### 1. Matemática e aprendizado de redes neurais

Comece por **Zhang et al., Dive into Deep Learning** (`zhang2023`): capítulos 2, 4, 5 e 12 da edição online, especialmente álgebra linear, cálculo, autodiferenciação, probabilidade, softmax, entropia cruzada, backpropagation, dropout e otimização. O livro associa explicações a implementações, sendo uma ponte útil para acompanhar o código. Use os títulos das seções para localizar conteúdos caso a numeração mude no PDF. [Sumário oficial](https://d2l.ai/).

Como aprofundamento, **Goodfellow, Bengio e Courville** (`goodfellow2016`), capítulos 2–8 e 11, oferece fundamentos matemáticos, regularização e metodologia prática. A versão gratuita oficial é HTML; não há PDF autorizado no site. É uma referência de base de 2016 e deve ser complementada pelos artigos sobre Transformers. [Livro oficial](https://www.deeplearningbook.org/).

**Meta de aprendizagem proposta:** explicar dimensões de tensores, multiplicação de matrizes, derivada em cadeia, logits, softmax, verossimilhança, gradiente e atualização de pesos; implementar e verificar um pequeno classificador antes de estudar atenção.

### 2. Modelagem de linguagem e preparação do texto

Leia **Jurafsky e Martin** (`jurafsky2026`), especialmente os capítulos intitulados *Words and Tokens*, *N-gram Language Models*, *Embeddings*, *Neural Networks* e *Transformers and Pretraining*. O portal consultado identifica um manuscrito de terceira edição de agosto de 2026. O arquivo local é um snapshot: consulte a observação de integridade no inventário. [Portal e sumário](https://web.stanford.edu/~jurafsky/slp3/).

O objetivo de treinamento é prever o próximo token a partir do prefixo. Para uma sequência, a probabilidade conjunta se decompõe em probabilidades condicionais. A perda média é a log-verossimilhança negativa; com logaritmo natural, perplexidade é sua exponencial. Esses conceitos aparecem no capítulo de modelos de linguagem de Jurafsky e Martin e na seção *Approach* de **Radford et al.** (`radford2019`). [Relatório GPT-2](https://cdn.openai.com/better-language-models/language-models.pdf).

**Sennrich, Haddow e Birch** (`sennrich2016`) explica segmentação em subpalavras por BPE em tradução. **Kudo e Richardson** (`kudo2018`) apresenta SentencePiece como ferramenta de tokenização a partir de texto bruto. São contribuições distintas: SentencePiece é uma implementação/framework com escolhas de modelos; não é sinônimo de BPE. O GPT-2 utiliza uma adaptação de BPE em bytes, descrita por Radford na seção *Input Representation*. [BPE](https://aclanthology.org/P16-1162/), [SentencePiece](https://aclanthology.org/D18-2012/).

**Decisão proposta para o projeto:** começar com caracteres, como no exemplo de Shakespeare do nanoGPT, e considerar BPE como comparação adicional. Se treinar um tokenizador próprio, ajuste-o somente no conjunto de treino. Registre vocabulário, normalização Unicode, tratamento de acentos, quebras de linha e delimitadores entre obras. Comparações de perplexidade por token exigem a mesma tokenização; quando ela muda, prefira apresentar resultados separadamente ou normalizar a log-verossimilhança pela mesma unidade textual, explicitando o cálculo. Fundamento: capítulos de tokenização/modelagem de linguagem de Jurafsky e Martin; [exemplo oficial nanoGPT](https://github.com/karpathy/nanoGPT).

### 3. Transformer, GPT-2 e implementação

**Vaswani et al.** (`vaswani2017`) é leitura explicitamente exigida. Priorize a seção *Model Architecture*: atenção escalada por produto escalar, múltiplas cabeças, redes feed-forward, conexões residuais e informação posicional. O artigo original apresenta um Transformer encoder–decoder para tradução; é preciso identificar quais componentes o GPT utiliza. [Artigo original](https://arxiv.org/abs/1706.03762).

**Radford et al.** (`radford2019`) é a referência arquitetural mais diretamente ligada ao objetivo: modelo autorregressivo, representação em bytes, organização dos blocos e experimentos do GPT-2. Estude *Approach*, *Input Representation* e *Model*. Compare essas seções com `model.py`: máscara causal, embeddings de token e posição, conexões residuais e normalização. [Relatório técnico](https://cdn.openai.com/better-language-models/language-models.pdf).

**Karpathy** (`karpathyTutorial`, `karpathyNanoGPT`) fornece o tutorial e código exigidos. Assista ao vídeo acompanhando a construção do modelo. No repositório, estude `data/shakespeare_char/prepare.py`, `model.py`, `train.py` e `sample.py`, e registre o commit efetivamente utilizado. O README consultado declara nanoGPT antigo/depreciado e sugere nanochat; **o enunciado continua especificando nanoGPT**, portanto a sugestão do repositório não altera a base exigida. [Tutorial](https://www.youtube.com/watch?v=kCc8FmEb1nY), [repositório](https://github.com/karpathy/nanoGPT).

**Brown et al.** (`brown2020`), também exigido, situa GPT-3, escala e aprendizado em contexto. Priorize introdução, abordagem e limitações. Few-shot no prompt não é o mesmo que atualizar pesos por fine-tuning. Os resultados em modelos muito maiores não demonstram que um modelo pequeno treinado apenas em Machado terá as mesmas capacidades. [GPT-3](https://arxiv.org/abs/2005.14165).

Leituras para explicar operações específicas: **Ba, Kiros e Hinton** (`ba2016`) para LayerNorm; **Hendrycks e Gimpel** (`hendrycks2016`) para GELU. São fontes originais para essas operações, mas não precisam ocupar espaço no artigo se tais componentes não forem discutidos. [LayerNorm](https://arxiv.org/abs/1607.06450), [GELU](https://arxiv.org/abs/1606.08415).

### 4. Treinamento e controle de sobreajuste

**Kingma e Ba** (`kingma2014`) fundamenta Adam; **Loshchilov e Hutter** (`loshchilov2017`) fundamenta AdamW e distingue decaimento de pesos desacoplado da penalização L2 em otimizadores adaptativos. **Srivastava et al.** (`srivastava2014`) explica dropout como regularização. As chaves arXiv usam o ano da submissão inicial: Adam é frequentemente citado como ICLR 2015 e AdamW como ICLR 2019; a biblioteca explicita que está referenciando os depósitos. [Adam](https://arxiv.org/abs/1412.6980), [AdamW](https://arxiv.org/abs/1711.05101), [Dropout](https://jmlr.org/papers/v15/srivastava14a.html).

**Aplicação proposta:** acompanhar perdas de treino e validação; selecionar checkpoint na validação; registrar taxa de aprendizado, scheduler, batch efetivo, contexto, clipping, dropout e weight decay. O livro D2L, capítulos de otimização/generalização, e o código `train.py` fornecem a base prática. Compare poucas configurações com orçamento declarado, mantendo constantes os fatores que não estiverem sendo estudados.

Para dimensionamento, leia **Kaplan et al.** (`kaplan2020`) e **Hoffmann et al.** (`hoffmann2022`). Ambos estudam relações entre perda, tamanho, dados e computação; Hoffmann revisita a alocação de orçamento e recomenda proporcionalmente mais dados do que o trabalho anterior. Essa diferença aparece explicitamente na introdução de Hoffmann. São resultados obtidos em regimes de grande escala: use-os para motivar a importância de dados e orçamento, não para impor uma fórmula universal ao corpus de Machado. [Kaplan](https://arxiv.org/abs/2001.08361), [Hoffmann](https://arxiv.org/abs/2203.15556).

### 5. Corpus, avaliação e comparações

A coleção **Machado de Assis — MEC/NUPILL** (`mecMachado`) e a notícia institucional da **ABL** (`abl2020`) são referências de proveniência. O portal organiza obras por gênero; a tarefa de obter os textos e comprovar a cobertura do corpus ainda pertence à implementação. Não se deve dizer “obra completa” apenas porque se concatenaram alguns romances. [Coleção MEC](https://machado.mec.gov.br/), [lista de obras](https://machado.mec.gov.br/obra-completa-lista?order=alpha&start=0), [ABL](https://www.academia.org.br/boletins/machado-de-assis-gratuito).

**Lee et al.** (`lee2022`) investiga duplicação em corpora, memorização e sobreposição entre treino e avaliação. Leia introdução, métodos de deduplicação e experimentos. Seus resultados justificam investigar o problema, mas suas porcentagens não podem ser atribuídas ao corpus de Machado sem medição local. [Artigo ACL](https://aclanthology.org/2022.acl-long.577/).

**Protocolo proposto para este trabalho:**

1. Manter inventário de obra, gênero, edição, URL, data de coleta, hash e tamanho; preservar uma versão bruta e outra limpa. Separar texto autoral de prefácios de terceiros, cabeçalhos e artefatos de extração.
2. Remover duplicatas exatas e investigar trechos repetidos entre edições. Definir treino/validação/teste antes de gerar janelas sobrepostas, evitando janelas do mesmo trecho em conjuntos diferentes.
3. Preferir separação por obra para estudar generalização entre obras; registrar que isso também pode produzir diferenças de gênero e época. Se dividir por capítulos ou blocos, declarar que a pergunta experimental é diferente e impedir sobreposição.
4. Comparar um baseline simples de linguagem com um GPT pequeno; depois variar uma dimensão, como profundidade, contexto ou regularização. O baseline pode ser bigrama, cuja teoria está no capítulo *N-gram Language Models*.
5. Apresentar perda e perplexidade em teste, parâmetros, tempo, memória e quantidade de tokens processados. Usar as mesmas divisões e protocolo; repetir sementes quando o orçamento permitir, relatando média e dispersão. Não usar o teste para escolher configurações.
6. Gerar amostras com prompts e parâmetros fixados antecipadamente. Registrar casos bons e falhos, repetição, coerência e semelhança literal ao treino. Se a avaliação qualitativa for feita só pelo autor, declará-la exploratória.

As escolhas acima são recomendações metodológicas adaptadas ao projeto, apoiadas em Lee, nos capítulos de avaliação/modelagem de linguagem de Jurafsky e Martin e em metodologia prática de Goodfellow. Não são exigências adicionais do professor nem resultados já obtidos.

**Holtzman et al.** (`holtzman2019`) é a leitura principal sobre geração: compara estratégias de decodificação e propõe nucleus/top-p sampling. O estudo mostra por que maximizar probabilidade durante a geração não basta para produzir bons textos abertos. Compare temperatura e top-k; top-p é opcional e requer verificar/implementar suporte no código. Não conclua que menor perplexidade resolve qualidade literária. [Artigo, resumo e seção de nucleus sampling](https://arxiv.org/abs/1904.09751).

### 6. Extensão para perguntas no universo de Machado

**Lewis et al.** (`lewis2020rag`) fundamenta combinar recuperação de passagens com geração. Leia resumo, introdução e formulação do modelo. O RAG original combina recuperação densa com modelo seq2seq e treinamento conjunto; um protótipo que apenas fornece trechos ao GPT é uma adaptação dessa ideia, não reprodução integral do artigo. [RAG](https://arxiv.org/abs/2005.11401).

**Extensão proposta:** indexar passagens com título e localização; recuperar trechos para uma pergunta; gerar resposta condicionada à evidência; mostrar a fonte e permitir resposta de insuficiência. Avaliar recuperação e resposta separadamente, com perguntas e trechos de referência preparados fora do ajuste. A proposta pode ser discutida no artigo sem afirmar que foi implementada.

**Gururangan et al.** (`gururangan2020`) discute continuação do pré-treinamento em domínio/tarefa; seus experimentos não são uma avaliação de GPT treinado em literatura brasileira. **Hu et al.** (`hu2021`) apresenta LoRA como adaptação eficiente de parâmetros; isso só se torna central se houver adaptação de um modelo existente. **Ouyang et al.** (`ouyang2022`) distingue treinamento para seguir instruções e feedback humano do simples treinamento de linguagem. RLHF não é requisito deste projeto. [Adaptação de domínio](https://aclanthology.org/2020.acl-main.740/), [LoRA](https://arxiv.org/abs/2106.09685), [Instruções](https://arxiv.org/abs/2203.02155).

**Zhao et al.** (`zhao2023`) é um panorama para consulta e expansão de vocabulário, abrangendo pré-treinamento, adaptação, uso e avaliação. É uma revisão extensa e evolutiva; a versão consultada está registrada. Priorize as fontes originais acima para justificar métodos específicos. [Survey](https://arxiv.org/abs/2303.18223).

## Como aproveitar no artigo de seis páginas

| Parte do artigo | Conteúdo e evidência | Referências candidatas |
|---|---|---|
| Introdução | Problema, domínio literário, objetivo e contribuição delimitada | `mecMachado`, `radford2019`, `brown2020` |
| Fundamentos/trabalhos relacionados | Modelo causal, atenção, tokenização; apenas o necessário para entender o experimento | `vaswani2017`, `radford2019`, `sennrich2016` |
| Dados e método | Obras, limpeza, deduplicação, divisão, arquitetura, treinamento e procedência do código | `mecMachado`, `lee2022`, `karpathyNanoGPT`, `loshchilov2017` |
| Resultados e discussão | Tabelas e curvas próprias, comparação controlada, amostras e limitações | `jurafsky2026`, `holtzman2019`; resultados precisam vir de seus experimentos |
| Conclusão/extensão | O que foi demonstrado, o que permanece limitado e proposta de QA | `lewis2020rag`; `hu2021` ou `gururangan2020` somente se pertinentes |

A distribuição exata de espaço é uma decisão de redação. Preserve espaço para resultados e discussão em vez de transformar o artigo em uma revisão extensa. O [IEEE Author Center](https://conferences.ieeeauthorcenter.ieee.org/write-your-paper/authoring-tools-and-templates/) (`ieeeTemplates`) fornece os modelos. Em um template LaTeX clássico, o uso costuma ser:

```tex
\bibliographystyle{IEEEtran}
\bibliography{referências/bibliografia}
```

O caminho acima supõe que o `.tex` está no diretório do projeto. Ajuste conforme a organização local. Se o ambiente TeX tiver dificuldade com acentos no caminho, copie o `.bib` para o diretório do artigo com nome ASCII. Não misture `biblatex` e o fluxo BibTeX tradicional no mesmo documento.

O guia **UFU** (`ufu2025`) apoia a lista ABNT; a norma correspondente está registrada como `abnt2025`. O guia é material didático, não substitui o texto normativo. Ele conserva uma menção antiga à norma de citações, portanto foi usado apenas para referências. [UFU](https://bibliotecas.ufu.br/en/node/3660), [normalização UFES](https://biblioteca.ufes.br/normalizacao).

## Alcance e limitações

Esta biblioteca cobre a teoria necessária para uma implementação e avaliação introdutórias do projeto e oferece caminhos de aprofundamento. Não promete esgotar a teoria de LLMs. A busca privilegia fontes originais, livros dos autores e documentação oficial; muitos experimentos de referência usam inglês e escalas muito superiores às deste trabalho. A transferência dessas conclusões para português literário é uma hipótese a avaliar.

Foram conferidos metadados, resumos e trechos pertinentes, com inspeção parcial de conteúdo; **não se declara leitura integral de todos os PDFs**. O download e a aprovação estrutural não certificam resultados científicos. Nenhuma leitura foi marcada como realizada pelo estudante. A curadoria, organização e redação deste roteiro tiveram assistência de IA com a skill ARS-Codex; todas as decisões experimentais e a interpretação dos resultados devem ser assumidas pelo autor do trabalho.
