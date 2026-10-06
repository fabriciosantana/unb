# Baseline GPT autorregressivo em nível de caractere

## 1. Escopo

Este documento registra o experimento de linha de base do projeto RNAP. O
objetivo foi treinar, a partir do zero, um modelo GPT pequeno em nível de
caractere usando o nanoGPT como código-base. O resultado serve como referência
para o trabalho e não como reprodução do GPT-2 original nem como modelo
conversacional.

Foi realizado um segundo treinamento comparativo de capacidade reduzida,
necessário para descrever e comparar os resultados solicitados no enunciado.

## 2. Dados

Foram utilizados os arquivos preparados no notebook de modelagem:

- `train.jsonl`: 11.821.395 bytes;
- `validation.jsonl`: 1.427.693 bytes;
- `test.jsonl`: 1.325.011 bytes.

A divisão foi feita por documento/obra, preservando partições separadas para
treino, validação e teste. O conjunto de teste contém 31 documentos. O
tokenizador de caracteres foi ajustado somente com os dados de treino.

O vocabulário final possui 147 símbolos, incluindo tokens reservados para fim
de documento (`EOS`) e caractere desconhecido (`UNK`). Foram observados 0
caracteres mapeados para `UNK` no treino e 2 na validação.

## 3. Código e ambiente

- Notebook: [`../notebooks/03_baseline_gpt_caractere_nanogpt.ipynb`](../notebooks/03_baseline_gpt_caractere_nanogpt.ipynb);
- código-base: nanoGPT;
- commit fixado: `3adf61e154c3fe3fca428ad6bc3818b27a3b8291`;
- licença do código-base: MIT, presente no checkout utilizado;
- ambiente: Google Colab Web;
- GPU: NVIDIA Tesla T4;
- PyTorch: `2.11.0+cu128`;
- dispositivo: CUDA;
- tipo numérico: `float16`.

## 4. Configuração do modelo

| Parâmetro | Valor |
|---|---:|
| Camadas (`n_layer`) | 6 |
| Cabeças (`n_head`) | 6 |
| Dimensão dos embeddings (`n_embd`) | 384 |
| Contexto (`block_size`) | 256 tokens do vocabulário de caracteres, incluindo EOS/UNK |
| Tamanho do lote (`batch_size`) | 64 |
| Dropout | 0,1 |
| Taxa de aprendizado inicial | 3e-4 |
| Otimizador | AdamW |
| `weight_decay` | 0,1 |
| Aquecimento (`warmup_iters`) | 100 iterações |
| Iterações máximas | 5.000 |
| Gradiente máximo (`grad_clip`) | 1,0 |
| Seed efetiva de treino (nanoGPT, uma GPU) | 1337 |
| Seed da preparação/avaliação/geração | 20260925 (janelas: `SEED+1`) |
| Compilação PyTorch | desativada |

O log do nanoGPT conta 10.678.272 parâmetros treináveis sem incluir embeddings
posicionais. Incluindo os 98.304 parâmetros posicionais únicos, são 10.776.576.
A cabeça de saída compartilha pesos com o embedding de tokens e não é contada
duas vezes.

## 5. Execução

O treinamento foi executado integralmente em CUDA no Colab. O checkpoint final
foi gerado em:

```text
/content/projetos/machado-assis/experimentos/gpt_caractere_nanogpt/out/ckpt.pt
```

Os artefatos foram exportados para o arquivo `machado_gpt_caractere_baseline.zip`
e preservados no Google Drive, na pasta `machado-gpt-treinamento-colab`.

## 6. Resultados quantitativos

| Métrica | Resultado |
|---|---:|
| Número de parâmetros | 10,68 M |
| Documentos avaliados no teste | 31 |
| Perda amostral (execução final pareada no Colab) | 1,239708 nats por token do vocabulário de caracteres, incluindo EOS/UNK |
| Perplexidade amostral (execução final pareada no Colab) | 3,454606 (adimensional; calculada sobre os mesmos tokens) |

A perda inclui caracteres e tokens especiais quando presentes nos alvos; a
perplexidade é a exponencial dessa perda. Portanto, não deve ser comparada
diretamente com perplexidades de modelos que utilizam tokenização BPE ou outra
unidade lexical.

As perdas intermediárias de treino e validação não foram preservadas. Não é
possível afirmar que o checkpoint final seja o de menor perda de validação:
`always_save_checkpoint=True` sobrescreve `ckpt.pt` nos intervalos, e o arquivo
disponível corresponde à iteração 5.000. A métrica principal deste relatório é a
da execução final pareada no Colab, registrada em
`RESULTADOS_EXPERIMENTOS.json` e nos artefatos ligados no README do projeto.
Uma reavaliação anterior em CPU (loss 1,239860; PPL 3,455131) permanece como
checagem histórica de consistência, não como resultado principal. A estimativa
final usa 200 lotes amostrados (batch 32, contexto de 256 tokens), sorteados do
fluxo concatenado que inclui EOS entre documentos; não é uma varredura
exaustiva de todos os tokens.

## 7. Avaliação qualitativa

As amostras geradas apresentam padrões de ortografia, pontuação e vocabulário
compatíveis com textos literários em português. Também aparecem nomes próprios,
estruturas sintáticas e marcas estilísticas semelhantes às do corpus.

Entretanto, a geração ainda contém transições incoerentes, combinações
semânticas improváveis e continuidade narrativa instável. Isso é compatível com
um modelo pequeno, treinado do zero, em nível de caractere. A amostra deve ser
tratada como inspeção qualitativa, não como avaliação humana formal.

## 8. Limitações

- O modelo foi treinado em um corpus específico e relativamente pequeno.
- O vocabulário representa caracteres e os tokens especiais EOS/UNK, não palavras ou subpalavras BPE.
- O modelo não deve ser descrito como GPT-2 pré-treinado.
- A perplexidade do vocabulário char-level não é diretamente comparável à de outros
  tokenizadores.
- Não há, nesta execução, série completa de perdas de treino e validação.
- O conjunto de teste foi usado somente após o treinamento.
- O resultado não mede compreensão, factualidade, autoria ou qualidade literária
  segundo avaliação humana.
- O armazenamento em `/content` do Colab é temporário; os artefatos exportados
  precisam permanecer no Google Drive ou em cópia local.

## 9. Conclusão

O baseline foi executado com sucesso em GPU, produziu um checkpoint válido e
apresentou, na execução final pareada, perda amostral de `1,239708` nats por
token do vocabulário de caracteres, incluindo EOS/UNK, e perplexidade de
`3,454606` sobre os mesmos tokens.
Esses resultados são suficientes para documentar a primeira linha de base do
trabalho. A conclusão não deve extrapolar para alegações de capacidade
conversacional ou de reprodução do GPT-2.

## 10. Artefatos relacionados

- Notebook: [`../notebooks/03_baseline_gpt_caractere_nanogpt.ipynb`](../notebooks/03_baseline_gpt_caractere_nanogpt.ipynb)
- Memória do trabalho: [`MEMORIA_TRABALHO.md`](MEMORIA_TRABALHO.md)
- Dados preparados: [`../dados/modelagem/`](../dados/modelagem/)

## 11. Experimento comparativo de capacidade reduzida

Foi executado um segundo notebook com o mesmo corpus, partições, tokenização,
contexto, orçamento de 5.000 iterações, hiperparâmetros de otimização, GPU e
protocolo. No código de treino fixado, ambos usam semente 1337; a semente 20260925 dos
notebooks controla preparação/tokenizador/geração, e `SEED+1` as janelas de
teste. A condição comparativa altera conjuntamente camadas, cabeças e dimensão
do embedding, não permitindo atribuir causalmente o efeito a um fator isolado.
O orçamento iguala atualizações, não FLOPs nem tempo.

| Modelo | Parâmetros sem posições | Perda (nats/token, incluindo EOS/UNK) | Perplexidade |
|---|---:|---:|---:|
| Baseline (6/6/384) | 10,68 M | 1,239708 | 3,454606 |
| Comparativo reduzido (4/4/256) | 3,19 M | 1,386213 | 3,999673 |

Contando parâmetros únicos incluindo posições, são 3.251.200 no modelo reduzido
contra 10.776.576 no baseline, redução de 69,8%. Sem posições, conforme o log do
nanoGPT, são 3.185.664 contra 10.678.272. Em relação
ao baseline, sua perda amostral aumentou 0,146504 nats por token (0,1465
arredondado), ou cerca de 11,8%, enquanto sua perplexidade aumentou 0,545067
(0,545 arredondado), ou cerca de 15,8%. Portanto,
neste protocolo, a redução de capacidade diminuiu o custo paramétrico, mas
esteve associada a maior perda preditiva no conjunto de teste.

As diferenças foram calculadas com os valores completos de
[`../RESULTADOS_EXPERIMENTOS.json`](../RESULTADOS_EXPERIMENTOS.json), antes do
arredondamento: `1.3862125158309937 - 1.2397083312273025 ≈ 0.1465041846036912`.
A razão entre perplexidades é `exp(perda_reduzido - perda_baseline) ≈ 1,158`.

As amostras dos dois modelos mantiveram padrões locais de português, pontuação
e forma dialogal, mas também exibiram fragmentação e incoerência semântica.
Essa inspeção não estabelece uma classificação global de qualidade literária
nem substitui uma avaliação humana formal.

O notebook do segundo experimento é
[`../notebooks/04_comparativo_gpt_caractere_reduzido.ipynb`](../notebooks/04_comparativo_gpt_caractere_reduzido.ipynb),
com resultados esperados em
`../experimentos/gpt_caractere_reduzido/`. O checkpoint e os demais artefatos do
segundo modelo foram preservados nessa pasta.
