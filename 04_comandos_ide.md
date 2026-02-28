# 04 — Comandos da Extensão Codex na IDE

> 🔗 Fonte oficial: [developers.openai.com/codex/ide/commands](https://developers.openai.com/codex/ide/commands)
> ⬅️ [Configurações](./03_configuracoes_ide.md) | ➡️ [Slash Commands](./05_slash_commands.md)

---

## 📄 Documentação Oficial

### Como atribuir atalhos de teclado

1. Abra a Paleta de Comandos (`Ctrl+Shift+P`)
2. Execute `Preferences: Open Keyboard Shortcuts`
3. Busque por `Codex` ou pelo ID do comando (ex: `chatgpt.newChat`)
4. Clique no ícone de lápis e defina o atalho desejado

### Referência de Comandos

| Comando | ID | Atalho Padrão | O que faz |
|---------|-----|---------------|-----------|
| Nova conversa | `chatgpt.newChat` | `Ctrl+N` | Cria uma nova conversa em branco |
| Adicionar ao chat | `chatgpt.addToThread` | — | Adiciona o texto selecionado à conversa atual |
| Adicionar arquivo | `chatgpt.addFileToThread` | — | Importa o arquivo ativo completo para o chat |
| Implementar TODO | `chatgpt.implementTodo` | — | Varre comentários `TODO` e implementa automaticamente |
| Novo painel | `chatgpt.newCodexPanel` | — | Abre o Codex em um painel separado |
| Abrir sidebar | `chatgpt.openSidebar` | — | Foca/abre a sidebar do Codex |

---

## 🎯 Exemplos Práticos

### Fluxo rápido: selecionar código → enviar ao Codex

1. Selecione um trecho de código no editor
2. `Ctrl+Shift+P` → `Codex: Add to Thread`
3. No painel do Codex, escreva sua pergunta
4. O Codex responde considerando a seleção

### Criar atalho personalizado para "Adicionar ao Chat"

1. `Ctrl+Shift+P` → `Open Keyboard Shortcuts`
2. Busque `chatgpt.addToThread`
3. Defina: `Ctrl+Shift+A`

Agora basta selecionar código e pressionar `Ctrl+Shift+A` para enviar ao Codex.

---

## 📖 Explicação Didática

### `addToThread` vs. `addFileToThread`

- **addToThread**: Envia apenas o texto que você **selecionou** (útil para trechos específicos)
- **addFileToThread**: Envia o **arquivo inteiro** aberto (útil quando o Codex precisa entender o contexto completo)

### Quando usar `implementTodo`?

Quando você tem vários TODOs espalhados pelo código e quer que o Codex resolva todos de uma vez. Ele varre o código, identifica cada `// TODO` e gera a implementação correspondente.

---

> ⬅️ [Configurações](./03_configuracoes_ide.md) | ➡️ [Slash Commands](./05_slash_commands.md)
