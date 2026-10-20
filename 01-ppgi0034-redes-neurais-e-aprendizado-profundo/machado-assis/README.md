# Projeto 1 RNAP — Machado de Assis

Este repositório contém os notebooks executados, a preparação auditável de uma amostra de textos de Machado de Assis, duas execuções de um modelo autorregressivo em nível de caractere e o artigo do projeto. Os notebooks versionados no GitHub preservam as saídas da execução no Colab.

## Material para avaliação

- Artigo final: [abrir/baixar PDF no Google Drive](https://drive.google.com/file/d/1F5IyjmACoBWa8HJQLv8BQb8EuwnpjMyx/view?usp=drivesdk) ou [`latex/out/ARTIGO_PROJETO1_FINAL.pdf`](latex/out/ARTIGO_PROJETO1_FINAL.pdf) no repositório.
- Fonte LaTeX: [`latex/ARTIGO_PROJETO1_RASCUNHO.tex`](latex/ARTIGO_PROJETO1_RASCUNHO.tex).
- Sumário de métricas e proveniência: [`RESULTADOS_EXPERIMENTOS.json`](RESULTADOS_EXPERIMENTOS.json).
- Avaliação técnica de fechamento: [`apoio/AVALIACAO_FINAL_FECHAMENTO.md`](apoio/AVALIACAO_FINAL_FECHAMENTO.md).
- Código, dados e notebooks: [pasta do projeto no GitHub](https://github.com/fabriciosantana/unb/tree/main/01-ppgi0034-redes-neurais-e-aprendizado-profundo/projetos/machado-assis).
- Composição e limites do corpus: [`apoio/AVALIACAO_COBERTURA_CORPUS.md`](apoio/AVALIACAO_COBERTURA_CORPUS.md).

## Notebooks executados

Abra as versões commitadas, que incluem as saídas de execução:

1. [01 — auditoria e construção do corpus no Colab](https://colab.research.google.com/github/fabriciosantana/unb/blob/main/01-ppgi0034-redes-neurais-e-aprendizado-profundo/projetos/machado-assis/notebooks/01_construcao_auditoria_corpus.ipynb)
2. [02 — preparação e partição dos dados no Colab](https://colab.research.google.com/github/fabriciosantana/unb/blob/main/01-ppgi0034-redes-neurais-e-aprendizado-profundo/projetos/machado-assis/notebooks/02_preparacao_dados_modelagem.ipynb)
3. [03 — baseline GPT caractere no Colab](https://colab.research.google.com/github/fabriciosantana/unb/blob/main/01-ppgi0034-redes-neurais-e-aprendizado-profundo/projetos/machado-assis/notebooks/03_baseline_gpt_caractere_nanogpt.ipynb)
4. [04 — configuração reduzida no Colab](https://colab.research.google.com/github/fabriciosantana/unb/blob/main/01-ppgi0034-redes-neurais-e-aprendizado-profundo/projetos/machado-assis/notebooks/04_comparativo_gpt_caractere_reduzido.ipynb)

Os notebooks 01 e 02 preparam e persistem os dados no Google Drive. Os notebooks 03 e 04 treinam os modelos. Abrir o notebook não inicia o treinamento; para conferir os resultados, consulte as saídas já salvas. Uma nova execução de 03 ou 04 cria outra pasta de resultados e treina desde o início.

## Resultados principais

As duas condições usam o mesmo corpus e partições, 5.000 atualizações, Tesla T4, PyTorch 2.11.0+cu128 e protocolo de avaliação de 6.400 janelas de teste.

| Condição | Arquitetura (camadas/cabeças/embedding) | Perda (nats/token) | Perplexidade | Parâmetros únicos |
|---|---:|---:|---:|---:|
| Baseline | 6/6/384 | 1,239708 | 3,454606 | 10.776.576 |
| Reduzida | 4/4/256 | 1,386213 | 3,999673 | 3.251.200 |

A configuração reduzida tem 69,8% menos parâmetros únicos e perda amostral maior. É uma comparação descritiva entre duas configurações; camadas, cabeças e dimensão mudam conjuntamente, e cada condição teve uma execução. Uma ocorrência de `½` no teste, ausente do vocabulário de treino, é codificada como `<|unk|>` e incluída na métrica. O corpus é uma amostra de trabalho, não uma coleção completa da obra.

## Artefatos de treinamento no Drive

- [Pasta compartilhada do projeto](https://drive.google.com/drive/folders/1VgfGCoNn-FatGc0q5tSDLwDOgLNgdkGa): contém `dados/`, as execuções e o PDF final.
- [Baseline — execução `20260928T230901Z-62253fb3`](https://drive.google.com/drive/folders/1ErqbAtjN2N0iqyVb9NXiKCVkSuOiW_TH): resultados JSON, log, curvas, checkpoint e amostra gerada.
- [Reduzido — execução `20260928T232621Z-f4c538e9`](https://drive.google.com/drive/folders/1kaZddXelvV4kguyTvsGoMfbNndCjY0FR): resultados JSON, log, curvas, checkpoint e amostra gerada.
- Dados persistidos: `Meu Drive/machado-gpt-treinamento-colab/dados/`.

O Drive informa acesso de leitor para qualquer pessoa com o link na pasta compartilhada, nas duas pastas dos experimentos e no PDF final.

## Ordem de leitura e reprodução

Leia os notebooks na ordem 01 → 02 → 03 → 04. O notebook 01 registra a fonte e os artefatos do corpus; o 02 produz as partições por documento; 03 e 04 treinam e avaliam, respectivamente, baseline e condição reduzida. Os hashes dos dados são conferidos pelos notebooks. A avaliação usa 200 lotes de 32 janelas de contexto 256, sorteados do fluxo de teste; não é uma varredura integral por documento.

Não é necessário repetir os treinamentos para a entrega: os resultados principais, logs e curvas da rodada final já estão preservados no Drive. Para apenas avaliar o material, consulte as saídas commitadas e o artigo.

## Atribuição

`model.py`, `train.py` e utilitários do modelo vêm do [nanoGPT](https://github.com/karpathy/nanoGPT), de Andrej Karpathy, sob licença MIT, no commit `3adf61e154c3fe3fca428ad6bc3818b27a3b8291`. A adaptação do projeto integra auditoria e preparação do corpus, partições, configuração dos experimentos, avaliação e exportação dos artefatos.

## Compilar o artigo

Na raiz do repositório, entre na pasta do projeto e compile:

```bash
cd projetos/machado-assis
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=latex/aux -jobname=ARTIGO_PROJETO1_FINAL \
  latex/ARTIGO_PROJETO1_RASCUNHO.tex
cp latex/aux/ARTIGO_PROJETO1_FINAL.pdf latex/out/ARTIGO_PROJETO1_FINAL.pdf
```

O PDF entregue foi compilado com as referências resolvidas e tem quatro páginas.
