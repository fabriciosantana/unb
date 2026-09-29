# Avaliação final de fechamento — Projeto 1 RNAP

**Data:** 29 de setembro de 2026  
**Escopo:** conferência da versão do artigo, dos notebooks commitados e dos artefatos das execuções finais no Colab/Drive. Esta é uma revisão técnica de fechamento, não uma nota oficial nem uma revisão independente por pares.

## Parecer

O trabalho está **tecnicamente fechado e pronto para submissão após liberar ao avaliador as duas pastas de resultados no Drive**. Não há justificativa para treinar outro modelo, ampliar o corpus ou acrescentar mais uma arquitetura. O artigo foi atualizado para os resultados pareados mais recentes, compilado com a bibliografia resolvida e gerado com quatro páginas, dentro do limite máximo de seis páginas informado para a atividade.

## Resultados finais registrados

| Condição | Parâmetros únicos | Perda de teste (nats/token) | Perplexidade |
|---|---:|---:|---:|
| Baseline, 6/6/384 | 10.776.576 | 1,239708 | 3,454606 |
| Reduzida, 4/4/256 | 3.251.200 | 1,386213 | 3,999673 |

As duas execuções usaram Tesla T4, PyTorch 2.11.0+cu128, o mesmo commit do nanoGPT, o mesmo corpus e partições, 5.000 atualizações e a mesma avaliação de 6.400 janelas de teste. A variante reduzida tem 69,8% menos parâmetros únicos; sua perda foi 0,1465 nats/token (11,8%) maior e sua perplexidade 15,8% maior. A conclusão é descritiva: houve uma execução por condição, e camadas, cabeças e dimensão foram alteradas conjuntamente.

As curvas registradas a cada 500 atualizações mostram a menor perda de validação observada na iteração 5.000 para ambas as condições. O artigo descreve corretamente esse resultado como o menor entre os pontos registrados. Uma ocorrência de `½` (U+00BD) no teste foi mapeada para `<|unk|>` e incluída como alvo; essa limitação pontual está documentada.

## Verificações de fechamento

- Os quatro notebooks executados estão versionados com saídas e têm links diretos do Colab no [README de entrega](../README.md).
- O artigo contém links para os quatro notebooks e para as pastas de resultados do Drive.
- O [PDF final](../latex/out/ARTIGO_PROJETO1_FINAL.pdf) foi recompilado com `latexmk` e BibTeX; as referências foram resolvidas e o documento tem quatro páginas.
- O [sumário JSON](../RESULTADOS_EXPERIMENTOS.json) registra as métricas integrais, a proveniência e os identificadores das execuções.
- A [pasta compartilhada do projeto](https://drive.google.com/drive/folders/1VgfGCoNn-FatGc0q5tSDLwDOgLNgdkGa) contém dados, execuções e PDF final. O Drive confirma permissão `anyone: reader` tanto nessa pasta quanto nas pastas do baseline e do modelo reduzido.
- O [PDF final no Drive](https://drive.google.com/file/d/1F5IyjmACoBWa8HJQLv8BQb8EuwnpjMyx/view?usp=drivesdk) também tem permissão `anyone: reader`.
- O corpus é descrito como amostra de trabalho, sem alegação de completude, conforme o esclarecimento do professor registrado na [avaliação de cobertura](AVALIACAO_COBERTURA_CORPUS.md).

## Ações restantes do autor

1. Commitar e enviar ao GitHub as alterações locais, incluindo o README, o artigo, o sumário e o PDF final; isso atualiza os links de `main` citados no artigo.
2. Entregar o PDF final, o link do repositório/README e os quatro links do Colab, seguindo as instruções específicas da disciplina. O acesso ao Drive está configurado como leitura por link.
3. Realizar a apresentação oral de cinco minutos exigida pela atividade. O roteiro é apoio de preparação, não comprovação de que a apresentação ocorreu.

Não foram identificadas outras mudanças de conteúdo com benefício suficiente para justificar nova alteração do manuscrito ou novos experimentos. A avaliação simulada e a memória de trabalho são documentos de apoio internos e não integram o pacote a ser entregue.
