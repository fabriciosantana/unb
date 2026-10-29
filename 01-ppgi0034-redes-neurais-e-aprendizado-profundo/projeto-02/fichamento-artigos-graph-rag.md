# Fichamento: grafos de conhecimento e RAG para pronunciamentos do Senado

**Projeto:** RNAP — Projeto 2, 2026/2  
**Corpus de interesse:** pronunciamentos do Senado Federal  
**Escopo:** quatro artigos selecionados sobre raciocínio em grafos, construção de GraphRAG, avaliação e recuperação guiada pela consulta.

## Síntese executiva

Os quatro trabalhos cobrem partes diferentes de um sistema de RAG com grafo. Youtu-GraphRAG propõe uma arquitetura integrada para extrair e organizar conhecimento e depois recuperar evidências; QAFD-RAG propõe uma estratégia de recuperação em grafo condicionada à pergunta; VoG acrescenta verificação iterativa durante o raciocínio; GraphRAG-Bench ajuda a definir quando e como comparar sistemas com e sem grafo.

Para o projeto do Senado, a contribuição mais diretamente testável é a recuperação sensível à pergunta do QAFD-RAG, desde que o grafo preserve ligações entre cada fato extraído e o pronunciamento, autor, data e trecho de origem. Youtu-GraphRAG é uma referência forte para desenhar a construção do grafo, e VoG inspira verificação de cadeias de evidência. GraphRAG-Bench é especialmente útil para formular uma avaliação que inclua perguntas simples, multi-hop, síntese e abstinência. Nenhum dos artigos, por si só, demonstra que seus ganhos se transferem a pronunciamentos parlamentares em português.

## 1. VoG: verificação passo a passo sobre grafos

**Referência:** Zhao, Wenxin et al. (2026). “VoG: Enhancing LLM Reasoning through Stepwise Verification on Knowledge Graphs.” ICLR 2026. [Texto publicado](https://proceedings.iclr.cc/paper_files/paper/2026/file/ab1ee157f7804a13f980414b644a9460-Paper-Conference.pdf).

### Problema e objetivo

Os autores tratam de erros que se acumulam quando um LLM percorre várias relações de um grafo para responder uma pergunta. A proposta combina planejamento, recuperação de fatos, verificação de cada etapa e revisão do plano, em vez de deixar toda a cadeia de raciocínio sem checagem intermediária.

### Método

VoG coordena três agentes LLM: um agente de planejamento, um de recuperação e um de verificação/revisão. O plano orienta a busca no grafo; as etapas são verificadas à medida que se avança; e um seletor baseado em bandit multi-armado adapta quais evidências e partes do histórico entram no contexto. A avaliação principal usa os conjuntos CWQ, WebQSP e WebQuestions com grafos de conhecimento e diferentes backbones LLM.

### Resultados reportados

Nos resultados principais, VoG supera as linhas de base comparadas em EM/F1 nos três conjuntos usados. Por exemplo, com Qwen2.5-7B, reporta 53,3/45,6 em CWQ, 67,3/55,1 em WebQSP e 52,8/45,2 em WebQuestions. O artigo também avalia outras configurações e informa resultados em Wikidata e conjuntos biomédicos. Esses números são evidência de desempenho nos cenários avaliados pelos autores, não uma previsão de desempenho no corpus do Senado.

### Contribuição para o projeto

- Inspira uma etapa de verificação de cada relação ou afirmação usada para compor uma resposta multi-documento.
- Sugere que a resposta mantenha uma trilha explícita: pergunta → subpergunta → evidência recuperada → conclusão.
- Pode orientar uma ablação: RAG sem verificação, recuperação em grafo sem verificação e sistema com verificação/revisão.

### Limitações e leitura crítica

**Reconhecidas pelos autores:** VoG assume um grafo confiável e suficientemente completo; um verificador LLM congelado pode deixar passar inconsistências sutis; e o seletor de contexto usa sinais relativamente básicos. Os autores discutem essas limitações na seção H.

**Inferência para o Senado:** pronunciamentos têm atribuição, data e contexto institucional importantes. Um grafo de entidades e relações sem modelagem explícita de quem disse o quê, quando e em qual sessão pode verificar uma relação semanticamente plausível, mas atribuí-la ao senador ou período errado. O grafo deve guardar proveniência até o trecho literal; a verificação do modelo não substitui essa evidência.

**Adequação:** alta como inspiração para verificação e avaliação de raciocínio multi-hop; média como implementação direta, pois o domínio e os grafos usados no artigo não são pronunciamentos legislativos.

## 2. Youtu-GraphRAG: construção e recuperação integradas

**Referência:** Dong, Junnan et al. (2026). “Youtu-GraphRAG: Vertically Unified Agents for Graph Retrieval-Augmented Complex Reasoning.” ICLR 2026. [Texto publicado](https://proceedings.iclr.cc/paper_files/paper/2026/file/e8618f2038b0209705e4d5e3cd496e1d-Paper-Conference.pdf).

### Problema e objetivo

O artigo argumenta que muitos sistemas otimizam separadamente a construção do grafo e a recuperação, embora o desempenho em perguntas complexas dependa da interação entre essas etapas. A proposta é integrar extração, organização hierárquica e recuperação agentiva.

### Método

O pipeline usa um esquema inicial para restringir os tipos de entidades, relações e atributos extraídos dos trechos. Depois, detecta comunidades combinando estrutura do grafo e similaridade semântica, organiza o conhecimento em uma árvore hierárquica e usa agentes para decompor perguntas complexas e consultar o grafo por caminhos/subperguntas. O artigo avalia seis benchmarks, entre eles perguntas multi-hop, dados anônimos e GraphRAG-Bench.

### Resultados reportados

Com DeepSeek-V3-0324, o artigo reporta acurácia top-20 de 86,5% em HotpotQA, 85,5% em 2Wiki e 53,6% em MuSiQue no modo aberto; no modo de rejeição, os valores correspondentes são 81,2%, 77,6% e 47,5%. Os resultados comparativos favorecem Youtu-GraphRAG em grande parte dos cenários avaliados, e os autores também reportam melhor relação entre custo de tokens de construção e desempenho. Trata-se de resultado dos benchmarks e modelos do artigo; não garante a mesma vantagem em português ou em um corpus político.

### Contribuição para o projeto

- O esquema inicial pode ser adaptado para classes relevantes: parlamentar, partido, comissão, projeto de lei, política pública, órgão, evento e pronunciamento; além de relações e atributos temporais.
- A hierarquia de comunidades pode ajudar a recuperar contexto temático mais amplo quando a pergunta pede síntese de vários pronunciamentos.
- A decomposição agentiva pode converter perguntas como “como mudou a posição de X sobre Y?” em subconsultas temporais e por tema.
- A comparação entre modo aberto e modo de rejeição inspira uma avaliação de respostas fundamentadas versus respostas que devem se abster quando faltam evidências.

### Limitações e leitura crítica

O artigo testa diversos conjuntos, mas a validação reportada não é uma avaliação específica de pronunciamentos legislativos brasileiros. Um de seus conjuntos anônimos foi construído a partir de romances clássicos, com perguntas geradas por modelo a partir de modelos de perguntas de outros benchmarks; essa composição é diferente de perguntas reais sobre discurso político. A alegação de transferência para novas distribuições deve, portanto, ser tratada como hipótese a validar no Senado.

**Inferência para o Senado:** extração guiada por esquema pode reduzir a variedade de rótulos, mas um esquema excessivamente rígido tende a omitir relações novas, posições ambíguas ou mudanças de sentido. É necessário inspecionar extrações e medir precisão/recall de entidades e relações. A árvore de comunidades deve complementar, não substituir, os trechos originais e suas referências.

**Adequação:** alta para desenho da etapa de ingestão e organização; média para adoção integral, dado o custo de extração agentiva e a necessidade de adaptar o esquema, idioma e critérios de proveniência.

## 3. GraphRAG-Bench: quando grafos ajudam e como avaliar

**Referência:** Xiang, Zhishang et al. (2026). “When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation.” ICLR 2026. [Texto integral](https://arxiv.org/html/2506.05690) · [Registro nos anais da ICLR](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6c9e01d6cefbbf4cdd265032550e767f-Abstract-Conference.html).

### Problema e objetivo

Os autores observam que avaliações anteriores cobrem de forma limitada a variedade de tarefas e a complexidade do raciocínio em RAG. Propõem GraphRAG-Bench para avaliar o pipeline completo, desde construção do grafo e recuperação até a geração, em quatro categorias: recuperação factual, raciocínio complexo, sumarização contextual e geração criativa.

### Método

O benchmark inclui corpora com diferentes densidades de informação, incluindo um conjunto médico e um conjunto novo construído pelos autores. Comparam sete frameworks GraphRAG e sistemas RAG convencionais, preservando as configurações padrão dos frameworks. Usam métricas diferentes por tarefa, como acurácia, ROUGE, cobertura de evidências, relevância do contexto e fidelidade. Essa escolha permite avaliar não apenas a resposta final, mas também a qualidade e a abrangência do contexto recuperado.

### Resultados reportados

Os resultados revelam uma troca entre precisão e cobertura. RAG convencional com reranking tem forte recall de evidências em perguntas factuais simples no conjunto novo (83,21%). Em tarefas de raciocínio de nível mais complexo, HippoRAG alcança recall de evidência de 87,91–90,95%, enquanto HippoRAG2 obtém alta relevância contextual (85,75–87,82%). O artigo conclui que grafos tendem a ser mais úteis quando a pergunta exige conectar segmentos distantes; em perguntas factuais simples, caminhos de grafo podem adicionar conteúdo redundante. Para tarefas de síntese ampla, maior cobertura também pode vir acompanhada de redundância.

### Contribuição para o projeto

Este é o artigo mais útil para justificar e estruturar a avaliação do projeto. Uma avaliação dos pronunciamentos pode estratificar perguntas por necessidade de raciocínio:

1. **Fato localizado:** nome, data, partido ou conteúdo de um pronunciamento.
2. **Ligação multi-hop:** relação entre parlamentar, tema, projeto, comissão ou evento em documentos diferentes.
3. **Síntese contextual:** comparação de posições ao longo do tempo ou entre parlamentares.
4. **Pergunta sem evidência suficiente:** medir se o sistema reconhece a insuficiência e se abstém.

Além das métricas de resposta, registrar evidências recuperadas, cobertura dos trechos necessários, precisão/relevância do contexto, fidelidade das afirmações às fontes, latência e custo. A comparação principal deve manter o mesmo LLM e orçamento de contexto para RAG vetorial e GraphRAG.

### Limitações e leitura crítica

O benchmark é um instrumento de comparação e não um método único para implementar GraphRAG. Os resultados dependem dos corpora, das configurações dos sistemas e do avaliador generativo adotados no artigo. O uso de avaliação baseada em LLM requer validação humana em uma amostra, sobretudo para atribuição de fala, temporalidade e nuances políticas. O próprio resultado do benchmark recomenda evitar a hipótese de que grafos sempre melhoram recuperação.

**Adequação:** muito alta para definir pergunta de pesquisa, baselines, categorias de consulta e métricas; média para reutilizar diretamente os dados e os resultados como evidência do domínio do Senado.

## 4. QAFD-RAG: difusão no grafo guiada pela pergunta

**Referência:** Zhou, Zhuoping et al. (2026). “Query-Aware Flow Diffusion for Graph-Based RAG with Retrieval Guarantees.” ICLR 2026. [Texto publicado](https://proceedings.iclr.cc/paper_files/paper/2026/file/584f32ccf76d73b85fa2053e795df697-Paper-Conference.pdf).

### Problema e objetivo

O artigo aborda recuperadores que expandem vizinhanças ou comunidades de modo pouco sensível à pergunta. QAFD-RAG busca adaptar a travessia do grafo ao conteúdo da consulta, priorizando caminhos relevantes e reduzindo a expansão para regiões semanticamente próximas, mas irrelevantes.

### Método

O sistema tem uma etapa de indexação, que divide documentos em trechos e extrai entidades e relações com LLM, e uma etapa de consulta. Na consulta, extrai palavras-chave, seleciona nós-semente por similaridade semântica e propaga fluxo no grafo usando pesos de aresta condicionados à pergunta. A otimização é resolvida por um algoritmo push–relabel. Os autores apresentam garantias de recuperação sob hipóteses estatísticas sobre separação entre sinal e ruído, conectividade das entidades relevantes e qualidade dos embeddings.

### Resultados reportados

O artigo avalia tarefas de QA multi-hop e text-to-SQL, entre outras. Em multi-hop QA, QAFD-RAG lidera algumas comparações, como HotpotQA e MuSiQue, enquanto HippoRAG é melhor em 2WikiMultiHopQA. Portanto, o próprio artigo mostra que a vantagem depende do benchmark. As garantias teóricas também são condicionais às hipóteses sobre grafo e embeddings; não significam recuperação perfeita em qualquer coleção.

### Contribuição para o projeto

- É uma opção concreta para testar se a pergunta pode guiar a expansão do grafo em torno de pessoas, temas, instituições e pronunciamentos relacionados.
- Permite formular uma comparação controlada entre busca vetorial, recuperação por vizinhança simples e difusão guiada por consulta.
- A noção de sementes semânticas e caminhos ponderados oferece uma trilha de recuperação que pode ser inspecionada e associada aos trechos citáveis.

### Limitações e leitura crítica

**Reconhecidas pelos autores:** embeddings pré-treinados podem ter desempenho inferior em domínios especializados; difusão baseada em embedding tem dificuldade com negação lógica explícita. Essas limitações são apresentadas na conclusão.

**Inferência para o Senado:** perguntas sobre “quem criticou”, “quem apoiou” ou “qual posição mudou” exigem modelar polaridade, atribuição e tempo. Similaridade entre termos não basta: “apoiou” e “criticou” podem aparecer nos mesmos trechos e ser semanticamente próximos. Relações devem manter sinal, sujeito, objeto, data e evidência textual, com avaliação específica para negação e mudança temporal.

**Adequação:** alta como método candidato para a recuperação; deve ser comparado com RAG vetorial e com uma variante híbrida que use metadados e evidência textual. O componente de extração não resolve sozinho a representação de posições parlamentares.

## Comparação transversal

| Artigo | Parte do sistema que mais informa | Uso recomendado no projeto | Risco central ao transferir |
|---|---|---|---|
| VoG | Raciocínio e verificação | Verificar cada passo e exigir evidência por afirmação | Grafo incompleto ou verificador que não detecta erro sutil |
| Youtu-GraphRAG | Extração, organização e recuperação | Guiar esquema e estudar hierarquias/comunidades | Esquema rígido, custo e transferência não comprovada ao Senado |
| GraphRAG-Bench | Avaliação ponta a ponta | Estratificar perguntas e medir resposta e evidência | Métricas automáticas podem não capturar atribuição e nuance política |
| QAFD-RAG | Recuperação no grafo | Método principal candidato para experimento de recuperação | Embeddings não representam bem negação, posição e temporalidade |

### O que os artigos sugerem em conjunto

1. **Comparar por tipo de pergunta.** A vantagem do grafo deve ser testada especialmente em questões que conectam documentos, e não presumida para consultas simples.
2. **Separar recuperação de geração.** Medir se a evidência necessária foi encontrada antes de atribuir erros apenas ao LLM que redige a resposta.
3. **Preservar proveniência.** Cada nó/aresta extraído deve apontar ao trecho original, identificador do pronunciamento, parlamentar e data. Essa é uma recomendação de desenho para o corpus, não um resultado experimental dos quatro artigos.
4. **Avaliar abstenção e contradição.** Perguntas sem evidência devem testar se o sistema evita completar lacunas com conhecimento paramétrico; posições contraditórias ou mutáveis precisam ser representadas com tempo e fonte.
5. **Controlar orçamento e modelo.** Comparar baselines com o mesmo modelo de geração, corpus, contexto máximo e conjunto de perguntas; contabilizar custo de construção e consulta.

## Caminho recomendado para o projeto

Uma pergunta de pesquisa viável seria: **“Em que tipos de perguntas sobre pronunciamentos do Senado, a recuperação aumentada por grafo melhora a cobertura e a fidelidade das evidências em relação ao RAG vetorial, mantendo a atribuição correta de parlamentar e período?”**

Proponho um experimento em três níveis:

1. **Baseline RAG:** busca híbrida ou vetorial sobre os trechos dos pronunciamentos, com metadados e citações.
2. **GraphRAG sem agente:** grafo de entidades/temas/eventos com relações temporais e arestas ligadas às evidências, usando QAFD-RAG como candidato de recuperação.
3. **GraphRAG com verificação:** mesma recuperação, acrescentando verificação das relações e das citações inspirada em VoG.

Youtu-GraphRAG pode informar o esquema e a organização hierárquica; não é necessário reproduzir todo o framework para testar a hipótese. GraphRAG-Bench informa a criação do conjunto de avaliação, com perguntas simples, multi-hop, síntese comparativa e casos que devem gerar abstenção. A avaliação deve incluir um conjunto anotado por pessoas com resposta esperada, trechos de suporte, entidade parlamentar e intervalo temporal.

**Desfechos principais:** cobertura de evidência necessária, precisão de atribuição, fidelidade da resposta aos trechos, acurácia da resposta e taxa de abstenção apropriada. **Desfechos operacionais:** latência, tokens/custo e esforço de construção do grafo. Para a hipótese de benefício, a métrica decisiva deve ser a qualidade das evidências e da atribuição em perguntas multi-hop, mantendo resultados separados para perguntas simples.

## Referências

- Dong, J. et al. (2026). *Youtu-GraphRAG: Vertically Unified Agents for Graph Retrieval-Augmented Complex Reasoning*. ICLR.
- Xiang, Z. et al. (2026). *When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation*. ICLR.
- Zhao, W. et al. (2026). *VoG: Enhancing LLM Reasoning through Stepwise Verification on Knowledge Graphs*. ICLR.
- Zhou, Z. et al. (2026). *Query-Aware Flow Diffusion for Graph-Based RAG with Retrieval Guarantees*. ICLR.

As chaves BibTeX correspondentes estão em [referencias-projeto2.bib](referencias-projeto2.bib): `dong2026youtu`, `xiang2026graphragbench`, `zhao2026vog` e `zhou2026qafdrag`.
