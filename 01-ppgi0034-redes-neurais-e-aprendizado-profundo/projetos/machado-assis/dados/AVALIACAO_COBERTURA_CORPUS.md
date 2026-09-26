# Avaliação de cobertura bibliográfica do corpus

## Escopo e conclusão

O corpus local é uma versão de trabalho, não um inventário completo da obra. A fonte de aquisição é o pacote `machado` do NLTK (246 arquivos TXT extraídos; 112 itens indexados classificados como autorais), com origem declarada na coleção MEC/NUPILL. O mestre final agrega 242 itens, incluindo 130 contos avulsos selecionados por baixa sobreposição textual com sete coletâneas. Essa heurística evita parte das duplicações, mas não prova que os contos sejam inéditos nem que represente todos os livros originais.

O cruzamento local com a bibliografia da Academia Brasileira de Letras contém 32 títulos: 24 correspondências diretas de caminho, seis entradas com material relacionado mas equivalência integral não verificada, uma tradução excluída da obra autoral e uma lacuna. A bibliografia oficial lista explicitamente *Correspondência* (1932); portanto, a anotação antiga “não localizada no índice-fonte” era imprecisa. A entrada foi corrigida para registrar que a obra aparece na lista da ABL, mas o volume não foi localizado no pacote NLTK. O conteúdo epistolar não foi acrescentado ao corpus nem modelado, pois não há fonte textual de edição identificada dentro dos dados presentes.

## Pendências por categoria

- **Correspondência (1932):** título listado pela ABL; conteúdo não localizado no pacote consultado. Identificar edição digital confiável e direitos/proveniência, depois auditar inclusão ou exclusão justificada.
- **Teatro, Poesias completas, Crítica (1910), Outras relíquias (1910), Crônicas (4 volumes, 1937) e Crítica literária (1937):** há arquivos relacionados no pacote, mas falta comparar sumários/edições para comprovar que todos os componentes dos volumes estejam representados e evitar duplicação.
- **Contos avulsos:** 130 itens foram incluídos automaticamente quando a sobreposição de n-gramas de 32 caracteres com sete coletâneas ficou abaixo de 0,85. Atualizou-se o manifesto para tornar explícita essa inclusão programática. Baixa sobreposição é apenas sinal heurístico, não evidência de ineditismo.
- **Edições e notas:** o pacote preserva transcrições com cabeçalhos/notas editoriais. A proveniência de cada transcrição e separação entre texto de Machado, notas e paratextos ainda precisa de validação editorial completa.

## Efeito sobre os resultados

Não alterar silenciosamente o corpus já usado nos dois modelos. Se a cobertura for corrigida com novas obras, gerar uma versão/digest novo do mestre, refazer as partições e repetir as duas condições sob o mesmo protocolo antes de atribuir resultados ao corpus ampliado. Até lá, os números do artigo descrevem exclusivamente a versão de trabalho identificada pelo SHA-256 `f5562aa740556fae3435cfacf5b54c414909cd54f2fb627067132225791cc5b3`.

## Fontes de controle

- [Bibliografia de Machado de Assis — Academia Brasileira de Letras](https://www.academia.org.br/academicos/machado-de-assis/bibliografia), consultada em 26/09/2026.
- [Coleção digital Machado de Assis — MEC/NUPILL](https://machado.mec.gov.br/).
- Inventário reproduzível e manifesto: `inventario_fontes.csv`, `cruzamento_bibliografia_abl.csv` e `manifesto_corpus.json`.
