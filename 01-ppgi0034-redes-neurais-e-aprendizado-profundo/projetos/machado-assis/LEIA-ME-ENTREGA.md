# Entrega — Projeto 1 RNAP: Machado de Assis

## Ordem sugerida para avaliação

1. `01_construcao_auditoria_corpus.ipynb` — inventário e montagem do corpus de trabalho.
2. `02_preparacao_dados_modelagem.ipynb` — limpeza, deduplicação, divisão por documento e geração dos JSONL.
3. `03_baseline_gpt_caractere_nanogpt.ipynb` — baseline (6 camadas, 6 cabeças, dimensão 384).
4. `04_comparativo_gpt_caractere_reduzido.ipynb` — condição reduzida (4/4/256).
5. `ARTIGO_PROJETO1_RASCUNHO.tex` e PDF compilado em `out/` — relatório IEEE.
6. `ROTEIRO_APRESENTACAO_5_MIN.md` — apoio ao seminário oral.

## Execução dos notebooks

Os notebooks 03 e 04 foram executados no Google Colab com GPU. Em uma sessão nova, carregar os três arquivos `train.jsonl`, `validation.jsonl` e `test.jsonl` de `dados/modelagem/`, executar as células em ordem e exportar os artefatos antes de encerrar a sessão. A GPU e o espaço de `/content` são temporários. Os checkpoints e os resultados exportados devem ser mantidos no Drive, fora do histórico Git se excederem os limites de tamanho.

Os notebooks do autor devem ser vinculados aqui antes da entrega final:

- Colab 01 — auditoria do corpus: **inserir link de compartilhamento**.
- Colab 02 — preparação: **inserir link de compartilhamento**.
- Colab 03 — baseline: **inserir link de compartilhamento**.
- Colab 04 — comparativo: **inserir link de compartilhamento**.

## Procedência e autoria do código

- `model.py`, `train.py` e utilitários importados são do repositório [nanoGPT](https://github.com/karpathy/nanoGPT), de Andrej Karpathy, licença MIT. Experimentos fixam o commit `3adf61e154c3fe3fca428ad6bc3818b27a3b8291`.
- A arquitetura/configuração de caracteres é adaptada do exemplo `shakespeare_char` do nanoGPT; não é uma implementação original integral nem reprodução do GPT-2.
- Os notebooks deste projeto integram as etapas de inventário/auditoria, preparação e partição dos dados, serialização do tokenizador, configuração de duas condições, avaliação e exportação. As participações individuais devem ser descritas pelo estudante de acordo com o trabalho efetivamente realizado.
- Dados-fonte, manifesto, auditorias, código e resultados têm seus caminhos registrados no repositório. O corpus é uma versão de trabalho: a cobertura de todos os livros ainda não está comprovada.

## Estado de verificação

O sumário versionável dos dois experimentos está em `RESULTADOS_EXPERIMENTOS.json`; os JSONs detalhados ficam dentro das pastas experimentais, ignoradas pelo Git por conterem checkpoints grandes. `experimentos/gpt_caractere_nanogpt/reevaluacao_baseline_cpu.json` documenta a reavaliação independente que reproduziu, ao arredondamento, a saída Colab do baseline. O ZIP original e logs históricos não foram recuperados. A matrícula ainda precisa ser preenchida no artigo. Os links públicos/compartilháveis dos Colabs também precisam ser acrescentados. Não se afirma que a apresentação oral já ocorreu.
