# Entrega — Projeto 1 RNAP: Machado de Assis

## Ordem sugerida para avaliação

1. [`notebooks/01_construcao_auditoria_corpus.ipynb`](../notebooks/01_construcao_auditoria_corpus.ipynb) — inventário e montagem do corpus de trabalho.
2. [`notebooks/02_preparacao_dados_modelagem.ipynb`](../notebooks/02_preparacao_dados_modelagem.ipynb) — limpeza, deduplicação, divisão por documento e geração dos JSONL.
3. [`notebooks/03_baseline_gpt_caractere_nanogpt.ipynb`](../notebooks/03_baseline_gpt_caractere_nanogpt.ipynb) — baseline (6 camadas, 6 cabeças, dimensão 384).
4. [`notebooks/04_comparativo_gpt_caractere_reduzido.ipynb`](../notebooks/04_comparativo_gpt_caractere_reduzido.ipynb) — condição reduzida (4/4/256).
5. [`latex/ARTIGO_PROJETO1_RASCUNHO.tex`](../latex/ARTIGO_PROJETO1_RASCUNHO.tex) e PDF compilado em [`latex/out/`](../latex/out/) — relatório IEEE.
6. [`ROTEIRO_APRESENTACAO_5_MIN.md`](ROTEIRO_APRESENTACAO_5_MIN.md) — apoio ao seminário oral.

## Execução dos notebooks

Os resultados históricos dos notebooks 03 e 04 foram obtidos no Google Colab com GPU. Para a nova rodada, use as versões atualizadas: salve cada notebook no seu Drive, selecione GPU e autorize a montagem do Drive na configuração inicial.

- Entrada: `MyDrive/machado-gpt-treinamento-colab/dados/modelagem/{train,validation,test}.jsonl`. Use as mesmas partições locais; os hashes são conferidos. Se faltarem arquivos, o notebook oferece upload e grava os JSONL nessa pasta.
- Saída automática: `MyDrive/machado-gpt-treinamento-colab/novas_execucoes/<experimento>/<identificador>/`. Cada inicialização cria uma pasta exclusiva; os resultados históricos não são alterados.
- Antes do treinamento: cópias dos JSONL, tokenizador, configuração, versão exata do código-base, ambiente e dependências.
- Durante o treinamento: `treinamento.log`, `curvas_perda.csv`, status e `out/ckpt.pt`, atualizado a cada 500 iterações. É preservado o último checkpoint, não todos os estados históricos. Não há retomada automática.
- Depois do treinamento: resultados, amostra, inícios das 6.400 janelas de teste, perdas por lote, figura das curvas e manifesto de artefatos. CPU usa sublotes de oito sem reduzir o total de janelas.
- Salve também o próprio notebook com suas saídas pelo menu do Colab. Os artefatos produzidos pelas células e o arquivo `.ipynb` são itens distintos.

Execute 03 e 04 separadamente. Em uma interrupção, consulte a pasta impressa, o status e o log; reexecutar a primeira célula cria outra execução do zero. A atualização do artigo deve ocorrer somente após conferir os novos resultados de ambos os modelos.

Os notebooks do autor devem ser vinculados aqui antes da entrega final:

- Colab 01 — auditoria do corpus: **inserir link de compartilhamento**.
- Colab 02 — preparação: **inserir link de compartilhamento**.
- Colab 03 — baseline: **inserir link de compartilhamento**.
- Colab 04 — comparativo: **inserir link de compartilhamento**.

## Procedência e autoria do código

- `model.py`, `train.py` e utilitários importados são do repositório [nanoGPT](https://github.com/karpathy/nanoGPT), de Andrej Karpathy, licença MIT. Experimentos fixam o commit `3adf61e154c3fe3fca428ad6bc3818b27a3b8291`.
- A arquitetura/configuração de caracteres é adaptada do exemplo `shakespeare_char` do nanoGPT; não é uma implementação original integral nem reprodução do GPT-2.
- Os notebooks deste projeto integram as etapas de inventário/auditoria, preparação e partição dos dados, serialização do tokenizador, configuração de duas condições, avaliação e exportação. As participações individuais devem ser descritas pelo estudante de acordo com o trabalho efetivamente realizado.
- Dados-fonte, manifesto, auditorias, código e resultados têm seus caminhos registrados no repositório. O corpus é uma amostra de trabalho; conforme esclarecimento do professor, não é necessário reunir todas as obras. Não se reivindica completude bibliográfica.

## Estado de verificação

O sumário versionável dos dois experimentos está em [`../RESULTADOS_EXPERIMENTOS.json`](../RESULTADOS_EXPERIMENTOS.json); os JSONs detalhados ficam dentro das pastas experimentais, ignoradas pelo Git por conterem checkpoints grandes. `../experimentos/gpt_caractere_nanogpt/reevaluacao_baseline_cpu.json` documenta a reavaliação independente que reproduziu, ao arredondamento, a saída Colab do baseline. O ZIP original e logs históricos não foram recuperados. A matrícula 262114527 foi preenchida no artigo. Os links públicos/compartilháveis dos Colabs também precisam ser acrescentados. Não se afirma que a apresentação oral já ocorreu.

Para compilar a partir da raiz do projeto: `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=latex/aux latex/ARTIGO_PROJETO1_RASCUNHO.tex`. A cópia de entrega do PDF fica em `latex/out/`.
