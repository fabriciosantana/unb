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
