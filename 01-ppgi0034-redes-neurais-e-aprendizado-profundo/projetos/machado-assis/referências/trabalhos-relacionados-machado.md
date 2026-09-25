# Modelos de linguagem treinados com Machado de Assis

Pesquisa complementar de 25 set. 2026, orientada ao enunciado `projeto1-rnap-2026_2.pdf`. Foram procuradas combinações de Machado de Assis, GPT-2, nanoGPT, treinamento, avaliação, Transformer e language model em páginas acadêmicas, GitHub e Hugging Face. A seleção abaixo exige evidência primária e distingue resultados registrados, declarações dos autores e código ainda sem resultados confirmados. Não é revisão sistemática exaustiva. Nenhum treinamento foi reexecutado.

## Correspondência mais direta: TCC de Milton Leal

**LEAL, Milton. Anatomia do GPT: Aspectos matemáticos e computacionais de um grande modelo de linguagem. IME-USP, 2024.** [Repositório e documento original](https://github.com/lealmilton/machado-gpt); [PDF local](leal-anatomia-gpt.pdf). Chave: `leal2024machado`.

O Apêndice A (p. impressas 57–60; páginas 71–74 do PDF) documenta um GPT de 28,5 milhões de parâmetros, tokenização por caracteres e 10.977.697 caracteres provenientes de 116 obras/textos do conjunto Kaggle de luxedo. Apresenta curvas de perda de treino/validação e exemplos de geração. Relata busca de hiperparâmetros de aproximadamente 100 horas e treinamento final de 8 horas em A100 de 40 GB. O corpo do trabalho descreve divisão 90/10; não identifiquei teste independente. É a referência acadêmica de maior aderência encontrada, inclusive para fundamentos e descrição experimental. O conjunto reúne diferentes gêneros e traduções: sua utilização não demonstra, por si, cobertura de todos os livros originais exigidos. O arquivo foi validado estruturalmente; origem, hash e extração estão em `metadados/leal-anatomia-gpt-*`.

## Implementações com resultados registrados

| Fonte e chave BibTeX | Implementação e corpus | Evidência de avaliação | Limite para sua comparação |
|---|---|---|---|
| [JPVercosa — machado-transformer](https://github.com/JPVercosa/machado-transformer), 2023; `jpvercosa2023` | Transformer causal por caracteres, baseado no tutorial de Karpathy indicado no enunciado; corpus Kaggle de Machado; notebook registra 10.814.306 parâmetros. | Saída persistida do notebook: passo 2999, perda de treino 1,3047 e validação 1,4022; divisão 70/30 e amostras geradas. | Sem teste independente identificado. Preparação substitui caracteres; avaliar fidelidade antes de reutilizar. As iterações do laço não equivalem automaticamente a épocas. |
| [HeitorWestphal — machado-lm](https://github.com/HeitorWestphal/machado-lm), 2026; `westphal2026` | GPT do zero, PyTorch e BPE próprio; três romances; 11.408.256 parâmetros, 6 camadas e 6 cabeças, contexto 256. | README e histórico: melhor perda de validação 3,8222, perplexidade 45,7 no passo 1400; 396.035 tokens de treino e 20.706 de validação. | Subconjunto de obras; validação nos últimos 5% do texto e ausência de teste independente identificado. É projeto técnico, não artigo revisado por pares. |
| [arthuraraujo — gpt2-small-machado-de-assis](https://huggingface.co/arthuraraujo/gpt2-small-machado-de-assis), 2025; `araujo2025machado` | Ajuste fino de `pierreguillou/gpt2-small-portuguese`, cerca de 124 milhões de parâmetros; três épocas. | Model card informa perdas de validação 4,2486; 4,1195; 4,0813. | O próprio cartão declara dataset desconhecido e pede mais informações sobre os dados. O nome sugere Machado, mas não comprova composição nem completude. Ajuste fino não equivale a treino do zero. |
| [Paulo Orenstein — laboratório GPT 5, IMPA](https://w3.impa.br/~pauloo/teaching/ml/labs/html/gpt_5/gpt_5/), sem data confirmada; `orensteinGpt5` | Sequência didática constrói Transformer por caracteres com `machado-all.txt`, preparado a partir do corpus Machado do NLTK; modelo final de aproximadamente 14,3 milhões de parâmetros. | Material registra perdas de treino/validação e geração; divisão 90/10. | “GPT 5” é o número da aula, não o modelo GPT-5 da OpenAI. Material didático, sem teste independente identificado. |

As métricas acima pertencem aos experimentos dos autores. Não devem ser ordenadas como um ranking: tokenização, corpus, divisão, tamanho e estágio de treinamento são diferentes.

## Implementação útil para comparação de arquiteturas

[losout0/deeplearning-final](https://github.com/losout0/deeplearning-final), 2025 (`losouto2025`), implementa GPT com atenção agrupada (GQA) e aponta comparação com atenção multihead. Há download, preparação, treinamento e teste: o script de download lista 12 obras do Gutenberg; a preparação concatena texto e divide parágrafos em 80/10/10. O teste calcula perda e perplexidade, entre outras métricas. **Não confirmei resultados numéricos de uma execução completa** nos artefatos acessíveis. Há diferenças de configuração entre treino e teste e caminhos locais que exigiriam ajuste. O repositório [LeviJunior21/Trabalho-AprendizagemProfunda-Transformer](https://github.com/LeviJunior21/Trabalho-AprendizagemProfunda-Transformer) é um fork e não foi contado como estudo independente. Útil para investigar uma extensão, mas não sustenta afirmar que GQA superou MHA.

## Manuscrito com corpus misto e avaliação por obra separada

**SANTOS, João Pedro Rodrigues dos. A Reproducible Pipeline for Architecture Comparison in Low-Resource Language Modelling: A Case Study on xLSTM versus Transformer. Maio de 2026.** [Repositório](https://github.com/Joao-pedrosantos/NaturalLanguageProcessing), arquivo `main.tex`; chave `santos2026pipeline`.

O manuscrito compara xLSTM e Transformer estilo GPT. Descreve 19 romances de seis autores, incluindo seis romances de Machado no treino, e reserva *Memórias Póstumas de Brás Cubas* para avaliação. A tabela GPU relata melhor perplexidade 269,3 para Transformer de 10,2 milhões de parâmetros, contra 287,3 para xLSTM de 10,1 milhões. Também examina tarefas com representações congeladas. É relevante para desenho de comparações e separação por obra, mas o corpus é misto e o manuscrito usa regimes distintos; não transferir seus números ao corpus exclusivamente machadiano. O conjunto reservado é usado como desenvolvimento/seleção de melhor checkpoint, portanto não deve ser chamado de teste final intocado. Não confirmei publicação em periódico/evento ou revisão por pares. A fonte LaTeX foi preservada; não foi localizado PDF autoral no repositório consultado. Há divergências entre instruções de prova de conceito do README e o protocolo do manuscrito, exigindo auditoria antes de reprodução.

## O requisito de reunir todos os livros originais

O enunciado atribui ao aluno a construção do arquivo de treinamento. Os trabalhos encontrados ajudam a definir o processo, mas nenhum foi auditado aqui contra um catálogo completo de livros originais. Nem “116 obras”, nem “machado-all”, nem a existência de PDFs demonstram cumprimento integral.

Proposta metodológica para este projeto:

1. Definir o universo bibliográfico e registrar, por obra, título canônico, gênero, edição, fonte e autoria original. Explicitar tratamento de traduções, coletâneas e publicações póstumas.
2. Baixar e guardar fontes individuais; extrair o texto, preservar Unicode e registrar correções. Separar conteúdo do autor de introduções editoriais, fichas e cabeçalhos.
3. Detectar duplicatas, principalmente textos avulsos que reaparecem em coletâneas. Comparar inventário esperado e obtido e relatar lacunas.
4. Gerar um arquivo mestre UTF-8 com delimitadores de obras e manter mapa de proveniência. Criar derivados de treino, validação e teste sem sobreposição; ajustar tokenizador somente no treino. Definir com clareza se “todos os livros” descreve o corpus mestre, pois reservar obras inteiras para teste implica não usá-las no ajuste de pesos.
5. Registrar perda, perplexidade, custo e amostras com prompts fixos. Comparar configurações sob a mesma tokenização e partições. Para uma extensão de perguntas e respostas, estabelecer avaliação específica: geração estilística não demonstra capacidade factual.

Esses itens são recomendações para o projeto, não resultados obtidos nesta pesquisa. Não foi construído nem treinado um corpus/modelo neste complemento.

## Fontes não consideradas experimentos completos

- [Jibabk/GPT-2-Machado-de-Asssis](https://github.com/Jibabk/GPT-2-Machado-de-Asssis): na versão consultada, coleta de PDFs e extração de textos; não identifiquei treinamento e avaliação completos.
- [bguisard/machadoGPT](https://github.com/bguisard/machadoGPT): preparação de dados, sem evidência suficiente de experimento completo.
- [Eilliar/gpt2-assis](https://github.com/Eilliar/gpt2-assis): documentação/esqueleto insuficiente para confirmar implementação e avaliação.

## Arquivos e rastreabilidade

- [BibTeX complementar](trabalhos-relacionados.bib): sete referências.
- [ABNT complementar](trabalhos-relacionados-abnt.md).
- [PDF do TCC](leal-anatomia-gpt.pdf): documento acadêmico baixado; os demais itens são páginas, repositórios, notebook, cartão de modelo ou manuscrito LaTeX, sem PDF autoral confirmado nesta consulta.
- `metadados/trabalhos-relacionados/`: snapshots de notebook, histórico, README e manuscrito, com commits e hashes em `proveniencia.json`. Não foram baixados pesos de modelos.

Para a seção curta de trabalhos relacionados do artigo IEEE, priorize Leal, JPVercosa e Westphal; use Santos para justificar comparação controlada, deixando explícito o corpus misto. Cite os repositórios como software/documentação, sem apresentá-los como publicações revisadas por pares.
