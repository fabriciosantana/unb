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

### Atualização da auditoria e documentação (2026-09-26)

- O `train.py` do nanoGPT fixado usa seed efetiva 1337 no treino de uma GPU. A seed `20260925` controla preparação/tokenizador e geração; `20260926` controla a amostragem do teste.
- Os checkpoints disponíveis são da iteração 5.000. `always_save_checkpoint=True` grava checkpoints nos intervalos; não declarar que o `ckpt.pt` é o melhor por validação sem curva/evidência adicional.
- A avaliação usa 200 lotes de 32 sequências de contexto 256 no fluxo concatenado de teste; é estimativa amostral, não varredura exaustiva nem média por obra.
- Artefatos do baseline estavam trocados de nome. Foram corrigidos: `config_train_machado_char.py`, `meta.pkl` (tokenizer pickle) e `amostra_gerada.txt` (texto). `resultados_baseline.json` registra a saída reportada do Colab; `reevaluacao_baseline_cpu.json` documenta a reavaliação independente que concordou ao arredondamento (loss 1,239860; PPL 3,455131). O ZIP original não foi recuperado. A cópia de checkpoint de 129 MB disfarçada de amostra foi removida após SHA-256 confirmar identidade com `out/ckpt.pt`.
- Parâmetros totais únicos incluindo posições: baseline 10.776.576; reduzido 3.251.200 (redução 69,8%). A contagem de pesos impressa pelo nanoGPT exclui posição: 10.678.272 e 3.185.664.
- A cobertura do corpus não está comprovada. A ABL lista `Correspondência` (1932), ausente no pacote NLTK; não afirmar obra completa nem alterar o corpus sem regenerar partições e repetir ambas as condições.
- O artigo foi ampliado e compilado em seis páginas. Matrícula e links dos Colabs aguardam preenchimento; o roteiro oral prepara, mas não comprova, a apresentação.
- Sumário reprodutível dos resultados de ambos os modelos: `RESULTADOS_EXPERIMENTOS.json`.

## Artefatos

- Checkpoint: `out/ckpt.pt`.
- Artefatos exportados em `machado_gpt_caractere_baseline.zip`.
- Os artefatos foram preservados no Google Drive, na pasta `machado-gpt-treinamento-colab`.
- O disco `/content` do Colab é temporário; sempre copiar resultados importantes para o Google Drive ou para o projeto local.

## Próximos passos

1. Usar este experimento como baseline.
2. Registrar perdas de treino e validação, se necessário, corrigindo a exibição dos logs com Python unbuffered.
3. Não fazer terceiro experimento sem necessidade: as duas condições existentes atendem ao requisito comparativo.
4. Antes de entregar, acrescentar matrícula e links dos Colabs; ensaiar e realizar a apresentação oral.

## Avaliação de escopo

- O baseline já cobre o núcleo do trabalho: preparação dos dados, treinamento de um modelo autorregressivo nanoGPT em nível de caractere, avaliação no conjunto de teste e preservação do checkpoint.
- O notebook caracteriza o modelo como uma linha de base educacional, não como reprodução do GPT-2 original nem como modelo conversacional.
- A especificação formal exige um artigo IEEE de seis páginas com avaliações e comparações dos resultados obtidos.
- A comparação experimental está atendida pelas duas condições; os limites da comparação estão registrados no artigo.
- Não comparar diretamente a perplexidade deste modelo com GPT-2/GPT-3, pois as escalas, corpora e tokenizações são diferentes.

## Experimento comparativo concluído

- Notebook: `projetos/machado-assis/04_comparativo_gpt_caractere_reduzido.ipynb`.
- Condição comparativa: 4 camadas, 4 cabeças e embedding 256.
- Alteração: capacidade conjunta (camadas, cabeças e embedding); não isola causalmente cada fator.
- Compartilhados: corpus, partições, tokenização, contexto de 256, 5.000 iterações, hiperparâmetros, GPU, precisão e protocolo.
- Diretório de resultados: `projetos/machado-assis/experimentos/gpt_caractere_reduzido/`.
- O notebook foi executado no Colab com GPU e os artefatos locais estão nessa pasta.

### Resultado do comparativo

- Parâmetros: 3,19 milhões.
- Test loss: `1,3862 nats/caractere`.
- Perplexidade por caractere: `4,000`.
- Documentos de teste: 31.
- Em relação ao baseline, a contagem total incluindo embeddings posicionais caiu 69,8%; a perda amostral aumentou 11,8% e a perplexidade 15,8%.
- A amostra preservou padrões locais de português, mas mostrou maior fragmentação e incoerência semântica.
