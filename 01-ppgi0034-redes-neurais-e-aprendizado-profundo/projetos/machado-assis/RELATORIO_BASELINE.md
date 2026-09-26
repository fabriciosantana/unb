# Baseline GPT autorregressivo em nível de caractere

## 1. Escopo

Este documento registra o experimento de linha de base do projeto RNAP. O
objetivo foi treinar, a partir do zero, um modelo GPT pequeno em nível de
caractere usando o nanoGPT como código-base. O resultado serve como referência
para o trabalho e não como reprodução do GPT-2 original nem como modelo
conversacional.

Não foi realizado um segundo treinamento para comparação entre arquiteturas ou
configurações, pois essa comparação não foi estabelecida como requisito do
escopo atual do trabalho.

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

- Notebook: `03_baseline_gpt_caractere_nanogpt.ipynb`;
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
| Contexto (`block_size`) | 256 caracteres |
| Tamanho do lote (`batch_size`) | 64 |
| Dropout | 0,1 |
| Taxa de aprendizado inicial | 3e-4 |
| Otimizador | AdamW |
| `weight_decay` | 0,1 |
| Aquecimento (`warmup_iters`) | 100 iterações |
| Iterações máximas | 5.000 |
| Gradiente máximo (`grad_clip`) | 1,0 |
| Semente | 20260925 |
| Compilação PyTorch | desativada |

O modelo possui aproximadamente 10,68 milhões de parâmetros.

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
| Test loss | 1,2399 nats por caractere |
| Perplexidade por caractere | 3,455 |

A perplexidade foi calculada em nível de caractere e, portanto, não deve ser
comparada diretamente com perplexidades de modelos que utilizam tokenização BPE
ou outra unidade lexical.

As perdas intermediárias de treino e validação não foram registradas no
relatório final da execução, porque a saída do subprocesso de treinamento não
foi exibida de forma contínua no Colab. A métrica de teste acima foi calculada
após a seleção do checkpoint final. Essa ausência deve ser apresentada como uma
limitação de registro, e não como uma estimativa inventada.

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
- A unidade de modelagem é o caractere, não palavras ou tokens BPE.
- O modelo não deve ser descrito como GPT-2 pré-treinado.
- A perplexidade por caractere não é diretamente comparável à de outros
  tokenizadores.
- Não há, nesta execução, série completa de perdas de treino e validação.
- O conjunto de teste foi usado somente após o treinamento.
- O resultado não mede compreensão, factualidade, autoria ou qualidade literária
  segundo avaliação humana.
- O armazenamento em `/content` do Colab é temporário; os artefatos exportados
  precisam permanecer no Google Drive ou em cópia local.

## 9. Conclusão

O baseline foi executado com sucesso em GPU, produziu um checkpoint válido e
apresentou `test loss = 1,2399` e perplexidade por caractere igual a `3,455`.
Esses resultados são suficientes para documentar a primeira linha de base do
trabalho. A conclusão não deve extrapolar para alegações de capacidade
conversacional ou de reprodução do GPT-2.

## 10. Artefatos relacionados

- Notebook: [`03_baseline_gpt_caractere_nanogpt.ipynb`](03_baseline_gpt_caractere_nanogpt.ipynb)
- Memória do trabalho: [`../../MEMORIA_TRABALHO.md`](../../MEMORIA_TRABALHO.md)
- Dados preparados: [`dados/modelagem/`](dados/modelagem/)

## 11. Experimento comparativo de capacidade reduzida

Foi executado um segundo notebook com a mesma seed, corpus, partições,
tokenização, contexto, orçamento de 5.000 iterações, hiperparâmetros de
otimização, GPU e protocolo de avaliação. A única alteração foi a capacidade
arquitetural: 4 camadas, 4 cabeças e embedding 256.

| Modelo | Parâmetros | Test loss | Perplexidade por caractere |
|---|---:|---:|---:|
| Baseline (6/6/384) | 10,68 M | 1,2399 | 3,455 |
| Comparativo reduzido (4/4/256) | 3,19 M | 1,3862 | 4,000 |

O modelo reduzido possui aproximadamente 70,1% menos parâmetros. Em relação
ao baseline, sua perda de teste aumentou 0,1463 nats por caractere, ou cerca de
11,8%, enquanto sua perplexidade aumentou 0,545, ou cerca de 15,8%. Portanto,
neste protocolo, a redução de capacidade diminuiu o custo paramétrico, mas
produziu pior desempenho preditivo no conjunto de teste.

As amostras do modelo reduzido mantiveram padrões locais de português,
pontuação e forma dialogal, mas exibiram mais fragmentação e incoerência
semântica. Essa observação qualitativa é compatível com as métricas, mas não
substitui uma avaliação humana formal.

O notebook do segundo experimento é
[`04_comparativo_gpt_caractere_reduzido.ipynb`](04_comparativo_gpt_caractere_reduzido.ipynb),
com resultados esperados em
`experimentos/gpt_caractere_reduzido/`. O checkpoint e os demais artefatos do
segundo modelo foram preservados nessa pasta.
