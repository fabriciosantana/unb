# Avaliação de cobertura bibliográfica do corpus

## Escopo e conclusão

O corpus local é uma amostra de trabalho, não um inventário completo da obra. O professor esclareceu que não é necessário reunir todas as obras: uma amostra útil ao treinamento e ao aprendizado é suficiente. Assim, a ausência de exaustividade não é tratada como descumprimento; documentamos a composição e os limites para interpretar os resultados sem generalizá-los à obra inteira. A fonte de aquisição é o pacote `machado` do NLTK, com origem declarada na coleção MEC/NUPILL. Seus 246 arquivos TXT se dividem em 116 itens indexados e 130 arquivos não indexados. Dos 116 indexados, quatro foram excluídos por não serem textos autorais de Machado: três traduções integrais de obras alheias e *Queda que as mulheres têm para os tolos*, de Paul de Kock, traduzido por Machado. Restam 112 itens indexados classificados como autorais. O mestre final reúne esses 112 itens e os 130 contos avulsos não indexados, totalizando 242 unidades textuais (112 + 130). Portanto, a diferença entre 246 arquivos da fonte e 242 itens no mestre corresponde exatamente aos quatro arquivos excluídos; os 130 contos já fazem parte dos 246 arquivos, não são acréscimos externos. A seleção heurística reduz parte da duplicação, mas não prova ineditismo nem cobertura de todos os livros originais.

O cruzamento local com a bibliografia da Academia Brasileira de Letras contém 32 títulos: 24 correspondências diretas de caminho, seis entradas com material relacionado mas equivalência integral não verificada, uma tradução excluída da obra autoral e uma lacuna. A bibliografia oficial lista explicitamente *Correspondência* (1932); portanto, a anotação antiga “não localizada no índice-fonte” era imprecisa. A entrada foi corrigida para registrar que a obra aparece na lista da ABL, mas o volume não foi localizado no pacote NLTK. O conteúdo epistolar não foi acrescentado ao corpus nem modelado, pois não há fonte textual de edição identificada dentro dos dados presentes.

## Limites e verificações úteis

- **Correspondência (1932):** título listado pela ABL; conteúdo não localizado no pacote consultado. É uma lacuna documentada da amostra, não uma exigência pendente. Só considerar inclusão futura se houver fonte digital confiável e proveniência verificável.
- **Teatro, Poesias completas, Crítica (1910), Outras relíquias (1910), Crônicas (4 volumes, 1937) e Crítica literária (1937):** há arquivos relacionados no pacote, mas falta comparar sumários/edições para comprovar que todos os componentes dos volumes estejam representados e evitar duplicação.
- **Contos avulsos:** 130 arquivos não indexados foram incluídos automaticamente quando a cobertura de n-gramas distintos de 32 caracteres em relação às sete coletâneas ficou abaixo de 0,40. O limiar 0,85 identifica sobreposição alta, e 0,40 marca sobreposição parcial; 0,85 não foi o corte efetivo de inclusão. A inclusão programática está registrada no manifesto e na auditoria. Baixa sobreposição é apenas sinal heurístico, não evidência de ineditismo.
- **Edições e notas:** o pacote preserva transcrições com cabeçalhos/notas editoriais. A proveniência de cada transcrição e separação entre texto de Machado, notas e paratextos ainda precisa de validação editorial completa.

## Interpretação dos resultados

Os números dos dois modelos descrevem exclusivamente a amostra identificada pelo SHA-256 `f5562aa740556fae3435cfacf5b54c414909cd54f2fb627067132225791cc5b3`. Não é necessário ampliar o corpus nem repetir os treinamentos apenas para atingir cobertura integral. Qualquer ampliação futura deve gerar nova versão/digest do mestre, refazer as partições e repetir ambas as condições sob o mesmo protocolo antes de atribuir resultados ao corpus ampliado.

## Fontes de controle

- [Bibliografia de Machado de Assis — Academia Brasileira de Letras](https://www.academia.org.br/academicos/machado-de-assis/bibliografia), consultada em 26/09/2026.
- [Coleção digital Machado de Assis — MEC/NUPILL](https://machado.mec.gov.br/).
- Inventário reproduzível e manifesto: `../dados/inventario_fontes.csv`, `../dados/cruzamento_bibliografia_abl.csv` e `../dados/manifesto_corpus.json`.
