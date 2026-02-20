---
description: Diretrizes e padrões para criação de commits no projeto
---

Sempre que eu solicitar a criação de um commit, analise as alterações staged (diff) e siga estritamente as regras de atomicidade e formatação abaixo.

## Regras Gerais

- **Atomicidade**: Os commits devem ser atômicos (uma alteração lógica por vez). Se houver múltiplas alterações não relacionadas, sugira dividi-las.
- **Formato dos Emojis**: Use **APENAS** o código do emoji (ex: `:tada:`). Nunca inclua o caractere Unicode/desenho visual do emoji.
- **Idioma**: A descrição do commit deve ser em [PT-BR/EN - escolha um e mantenha].

## Lista de Referência (Código : Tipo)

- `:tada:` : Commit inicial
- `:books: docs` : Atualização de documentação
- `:bug: fix` : Correção de erro
- `:sparkles: feat` : Nova funcionalidade
- `:bricks: ci` : Configuração de CI/Docker/Ambiente
- `:recycle: refactor` : Refatoração de código
- `:zap: perf` : Melhoria de performance
- `:boom: fix` : Reversão ou mudança crítica (breaking change)
- `:lipstick: feat` : Estilização, UI ou ajustes visuais
- `:test_tube: test` : Criação ou alteração de testes
- `:bulb: docs` : Adição/ajuste de comentários no código
- `:card_file_box: raw` : Alterações em arquivos de dados ou DB
- `:broom: cleanup` : Limpeza de código morto ou formatação
- `:wastebasket: remove` : Remoção de arquivos ou diretórios

## Formato da Mensagem

A saída deve conter apenas a mensagem de commit no padrão:
`:emoji_code: tipo: Descrição sucinta da mudança`

**Exemplo de saída:**
`:broom: cleanup: remove logs de debug no controller de usuários`