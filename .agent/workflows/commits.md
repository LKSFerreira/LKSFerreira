---
description: Diretrizes e padrões para criação de commits no projeto
---

Sempre que eu solicitar a criação de um commit, você deve seguir estritamente as regras de formatação, atomicidade e padronização de emojis abaixo.

## Regras Gerais

- **Atomicidade**: Os commits devem ser atômicos (uma alteração por vez).
- **Formato dos Emojis**: Use **APENAS** o código do emoji (ex: `:tada:`), não o desenho visual.

## Lista de Tipos e Emojis

- 🎉 `:tada: Commit inicial`
- 📚 `:books: docs: Atualização de documentação`
- 🐛 `:bug: fix: Correção de erro`
- ✨ `:sparkles: feat: Nova funcionalidade`
- 🧱 `:bricks: ci: Configuração de CI/Docker`
- ♻️ `:recycle: refactor: Refatoração de código`
- ⚡ `:zap: perf: Melhoria de performance`
- 💥 `:boom: fix: Reversão ou mudança crítica`
- 💄 `:lipstick: feat: Estilização/UI`
- 🧪 `:test_tube: test: Testes`
- 💡 `:bulb: docs: Comentários no código`
- 🗃️ `:card_file_box: raw: Arquivos de dados`
- 🧹 `:broom: cleanup: Limpeza de código morto`
- 🗑️ `:wastebasket: remove: Remoção de arquivos`

## Formato da Mensagem

O formato deve seguir estritamente o padrão:
`:emoji_code: tipo: Descrição da mudança`

**Exemplo:**
`:broom: cleanup: Descrição da mudança`