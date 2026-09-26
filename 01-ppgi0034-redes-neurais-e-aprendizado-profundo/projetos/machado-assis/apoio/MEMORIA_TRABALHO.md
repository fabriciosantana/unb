# Memória do trabalho

## Estado atual

- Projeto: `01-ppgi0034-redes-neurais-e-aprendizado-profundo`.
- Execução realizada no Colab Web com GPU Tesla T4.
- PyTorch: `2.11.0+cu128`.
- Notebook executado: `projetos/machado-assis/notebooks/03_baseline_gpt_caractere_nanogpt.ipynb`.
- Modelo: nanoGPT treinado em nível de caractere, a partir do zero.
- Commit do nanoGPT: `3adf61e154c3fe3fca428ad6bc3818b27a3b8291`.
- Vocabulário: 147 tokens (caracteres e os tokens especiais EOS e UNK).
- Dados usados: `train.jsonl`, `validation.jsonl` e `test.jsonl`.
- Documentos de teste: 31.
- Configuração principal: 6 camadas, 6 cabeças, embedding 384, `block_size=256`, `batch_size=64`, `max_iters=5000`, `float16`.
- Parâmetros do modelo: aproximadamente 10,68 milhões.
- Perda amostral: `1,2399 nats por token` do vocabulário de caracteres, incluindo EOS e UNK nos alvos.
- Perplexidade amostral: `3,455` (adimensional, calculada sobre os mesmos tokens).
- O modelo aprendeu padrões de português e estilo literário, mas as amostras ainda apresentam incoerências semânticas, como esperado para um modelo pequeno treinado do zero.

### Atualização da auditoria e documentação (2026-09-26)

- O `train.py` do nanoGPT fixado usa seed efetiva 1337 no treino de uma GPU. A seed `20260925` controla preparação/tokenizador e geração; `20260926` controla a amostragem do teste.
- Os checkpoints disponíveis são da iteração 5.000. `always_save_checkpoint=True` grava checkpoints nos intervalos; não declarar que o `ckpt.pt` é o melhor por validação sem curva/evidência adicional.
- A avaliação usa 200 lotes de 32 sequências de contexto 256 no fluxo concatenado de teste; é estimativa amostral, não varredura exaustiva nem média por obra.
- Artefatos do baseline estavam trocados de nome. Foram corrigidos: `config_train_machado_char.py`, `meta.pkl` (tokenizer pickle) e `amostra_gerada.txt` (texto). `resultados_baseline.json` registra a saída reportada do Colab; `reevaluacao_baseline_cpu.json` documenta a reavaliação independente que concordou ao arredondamento (loss 1,239860; PPL 3,455131). O ZIP original não foi recuperado. A cópia de checkpoint de 129 MB disfarçada de amostra foi removida após SHA-256 confirmar identidade com `out/ckpt.pt`.
- Parâmetros totais únicos incluindo posições: baseline 10.776.576; reduzido 3.251.200 (redução 69,8%). A contagem de pesos impressa pelo nanoGPT exclui posição: 10.678.272 e 3.185.664.
- O corpus é uma amostra, não uma coleção exaustiva. O professor esclareceu que não é necessário reunir todas as obras; a ausência de `Correspondência` (1932) é documentada, mas não é pendência nem motivo para novo treinamento. Não afirmar que a amostra é completa.
- O artigo revisado foi compilado em quatro páginas, dentro do limite de até seis esclarecido pelo professor. Matrícula e links dos Colabs ainda aguardam preenchimento; o roteiro oral prepara, mas não comprova, a apresentação.
- Sumário reprodutível dos resultados de ambos os modelos: `projetos/machado-assis/RESULTADOS_EXPERIMENTOS.json`.

### Implementação da revisão de redação acadêmica (2026-09-26)

A revisão solicitada foi aplicada com orientação da skill `ars-codex:academic-research-suite`, restrita à documentação e sem novo treinamento. O texto mantém a comparação descritiva, a execução única por condição e os limites dos artefatos preservados.

- **Métrica e arredondamento:** perda em nats por token do vocabulário de caracteres, incluindo EOS/UNK; perplexidade adimensional. Contexto de 256 tokens. A diferença de perda é `0.1463685995340346`, arredondada a **0,1464**, calculada antes de arredondar os valores da tabela. As chaves legadas `per_character` e `context_characters` do sumário JSON foram mantidas, com notas explicativas; nenhum valor numérico foi alterado.
- **Fundamentação:** explicação de Q, K, V, dimensão das chaves e máscara causal; percurso dos embeddings até as probabilidades do próximo token; distinção entre treinamento por gradientes e aprendizagem em contexto no GPT-3.
- **Método:** limpeza descrita a partir do manifesto, proporções efetivas das partições e critérios de sobreposição conferidos no notebook 01. Atenção: `0,85` marca sobreposição alta, `0,40` marca parcial; a inclusão automática efetiva selecionou os 130 contos com cobertura **abaixo de 0,40**, sem contenção integral. Não descrever `0,85` como único corte de inclusão. A geração produz 700 tokens e depois trunca a apresentação no primeiro EOS; não é parada antecipada da geração.
- **Coesão:** ressalvas repetidas foram consolidadas; justificativas administrativas e instruções de entrega saíram do corpo científico. A matrícula continua como campo visível no cabeçalho; as pendências de links permanecem em `LEIA-ME-ENTREGA.md`.
- **Referências:** citações diretas aos metadados do pacote `machado` do NLTK e à bibliografia da ABL; referência do nanoGPT com commit fixado; notas editoriais de preenchimento substituídas por dados bibliográficos, sem inventar datas de publicação.
- **Linguagem e interpretação:** grafia `autorregressivo`, terminologia consistente e relação explícita `PPL_reduzido/PPL_baseline = exp(L_reduzido - L_baseline) ≈ 1,158`. A contagem menor de pesos não é apresentada como ganho medido de velocidade.

Arquivos principais: `latex/ARTIGO_PROJETO1_RASCUNHO.tex`, `referências/bibliografia.bib` e PDF em `latex/out/ARTIGO_PROJETO1_RASCUNHO.pdf`. O relatório de apoio e o roteiro oral foram sincronizados; neste último, a semente de amostragem do teste foi corrigida para **20260926**. Próximo passo: leitura final pelo autor, preenchimento de matrícula e links e preparação da apresentação; não há terceiro experimento previsto.

### Esclarecimento do professor e avaliação revisada

- O professor esclareceu que **não é necessário reunir todas as obras**: o objetivo é construir uma amostra boa e útil ao treinamento de um modelo de linguagem e ao aprendizado da disciplina. Portanto, a ausência de `Correspondência` (1932) e a falta de exaustividade bibliográfica não devem ser tratadas como descumprimento central do requisito. Não alegar que o corpus é completo; descrevê-lo como amostra de trabalho e justificar sua utilidade/limitações.
- A amostra existente tem 242 itens, aproximadamente 14 MB de texto mestre, variedade de categorias e partições por documento (181 treino, 30 validação, 31 teste). A seleção heurística de contos avulsos e os elementos editoriais continuam sendo limitações a relatar, não razão automática para exigir a reunião de todas as obras.
- Nota simulada revisada frente ao esclarecimento: **8,5/10**, não oficial. A avaliação anterior de 7,8/10 foi revista porque atribuía perda excessiva à ausência de cobertura integral. A nota ainda é provisória: matrícula e links dos Colabs faltam, e a apresentação oral não foi observada.
- Próximo passo quando o estudante retornar: revisar o artigo e os materiais de entrega; preencher matrícula e links dos Colabs; preparar/apresentar os cinco minutos em sala.

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
- A especificação formal pede artigo IEEE de até seis páginas, com descrição do problema e avaliações/comparações dos resultados obtidos. O limite não é uma meta de extensão; priorizar clareza e fundamentação.
- A comparação experimental está atendida pelas duas condições; os limites da comparação estão registrados no artigo.
- Não comparar diretamente a perplexidade deste modelo com GPT-2/GPT-3, pois as escalas, corpora e tokenizações são diferentes.

## Experimento comparativo concluído

- Notebook: `projetos/machado-assis/notebooks/04_comparativo_gpt_caractere_reduzido.ipynb`.
- Condição comparativa: 4 camadas, 4 cabeças e embedding 256.
- Alteração: capacidade conjunta (camadas, cabeças e embedding); não isola causalmente cada fator.
- Compartilhados: corpus, partições, tokenização, contexto de 256, 5.000 iterações, hiperparâmetros, GPU, precisão e protocolo.
- Diretório de resultados: `projetos/machado-assis/experimentos/gpt_caractere_reduzido/`.
- O notebook foi executado no Colab com GPU e os artefatos locais estão nessa pasta.

### Resultado do comparativo

- Parâmetros: 3,19 milhões.
- Perda amostral: `1,3862 nats por token` do vocabulário de caracteres, incluindo EOS e UNK nos alvos.
- Perplexidade amostral: `4,000` (adimensional, calculada sobre os mesmos tokens).
- Documentos de teste: 31.
- Em relação ao baseline, a contagem total incluindo embeddings posicionais caiu 69,8%; a perda amostral aumentou 11,8% e a perplexidade 15,8%.
- A amostra preservou padrões locais de português, mas também apresentou fragmentação e incoerência semântica; não há avaliação humana formal que classifique a qualidade literária dos dois modelos.
