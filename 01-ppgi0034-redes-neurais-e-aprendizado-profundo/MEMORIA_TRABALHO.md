# Memória do trabalho

## Estado atual

- Projeto: `01-ppgi0034-redes-neurais-e-aprendizado-profundo`.
- Execução realizada no Colab Web com GPU Tesla T4.
- PyTorch: `2.11.0+cu128`.
- Notebook executado: `projetos/machado-assis/03_baseline_gpt_caractere_nanogpt.ipynb`.
- Modelo: nanoGPT treinado em nível de caractere, a partir do zero.
- Commit do nanoGPT: `3adf61e154c3fe3fca428ad6bc3818b27a3b8291`.
- Vocabulário: 147 caracteres, incluindo EOS e UNK.
- Dados usados: `train.jsonl`, `validation.jsonl` e `test.jsonl`.
- Documentos de teste: 31.
- Configuração principal: 6 camadas, 6 cabeças, embedding 384, `block_size=256`, `batch_size=64`, `max_iters=5000`, `float16`.
- Parâmetros do modelo: aproximadamente 10,68 milhões.
- Test loss: `1,2399 nats/caractere`.
- Perplexidade por caractere: `3,455`.
- O modelo aprendeu padrões de português e estilo literário, mas as amostras ainda apresentam incoerências semânticas, como esperado para um modelo pequeno treinado do zero.

## Artefatos

- Checkpoint: `out/ckpt.pt`.
- Artefatos exportados em `machado_gpt_caractere_baseline.zip`.
- Os artefatos foram preservados no Google Drive, na pasta `machado-gpt-treinamento-colab`.
- O disco `/content` do Colab é temporário; sempre copiar resultados importantes para o Google Drive ou para o projeto local.

## Próximos passos

1. Usar este experimento como baseline.
2. Registrar perdas de treino e validação, se necessário, corrigindo a exibição dos logs com Python unbuffered.
3. Executar novos experimentos mantendo as mesmas partições de treino, validação e teste.
4. Comparar loss, perplexidade, tempo, configuração, seed, dispositivo e amostras geradas.
5. Atualizar o relatório ou artigo com os resultados e as limitações do modelo.

## Avaliação de escopo

- O baseline já cobre o núcleo do trabalho: preparação dos dados, treinamento de um modelo autorregressivo nanoGPT em nível de caractere, avaliação no conjunto de teste e preservação do checkpoint.
- O notebook caracteriza o modelo como uma linha de base educacional, não como reprodução do GPT-2 original nem como modelo conversacional.
- A especificação formal exige um artigo IEEE de seis páginas com avaliações e comparações dos resultados obtidos.
- Portanto, o baseline está concluído, mas a entrega final ainda precisa de uma comparação experimental ou de uma forma de comparação explicitamente aceita pelo professor.
- Não comparar diretamente a perplexidade deste modelo com GPT-2/GPT-3, pois as escalas, corpora e tokenizações são diferentes.

## Experimento comparativo planejado

- Notebook: `projetos/machado-assis/04_comparativo_gpt_caractere_reduzido.ipynb`.
- Condição comparativa: 4 camadas, 4 cabeças e embedding 256.
- Variável alterada em relação ao baseline: capacidade arquitetural.
- Mantidos constantes: corpus, partições, tokenização, seed `20260925`, contexto de 256 caracteres, 5.000 iterações, hiperparâmetros de otimização, GPU, precisão e protocolo de avaliação.
- Diretório de resultados esperado: `projetos/machado-assis/experimentos/gpt_caractere_reduzido/`.
- O novo notebook foi criado limpo, sem resultados executados; deve ser rodado no Colab com GPU.

### Resultado do comparativo

- Parâmetros: 3,19 milhões.
- Test loss: `1,3862 nats/caractere`.
- Perplexidade por caractere: `4,000`.
- Documentos de teste: 31.
- Em relação ao baseline, houve redução aproximada de 70,1% nos parâmetros, aumento de 11,8% na perda de teste e aumento de 15,8% na perplexidade.
- A amostra preservou padrões locais de português, mas mostrou maior fragmentação e incoerência semântica.
