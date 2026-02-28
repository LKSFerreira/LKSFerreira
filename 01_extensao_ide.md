# 01 — Extensão Codex na IDE

> 🔗 Fonte oficial: [developers.openai.com/codex/ide](https://developers.openai.com/codex/ide)
> ⬅️ [Índice](./00_indice.md) | ➡️ [Funcionalidades](./02_funcionalidades.md)

---

## 📄 Documentação Oficial

### O que é

A extensão Codex para IDE (VS Code, Cursor e JetBrains) permite programar ao lado de um agente de IA diretamente no editor. Planos ChatGPT Plus, Pro, Business, Edu e Enterprise já incluem o Codex.

### Instalação

1. Abra o VS Code
2. Vá em Extensões (`Ctrl+Shift+X`)
3. Pesquise por **"ChatGPT"** (extensão oficial da OpenAI)
4. Instale e reinicie o editor

### Configuração Inicial

- **Mover para a barra lateral direita**: Arraste o ícone do Codex para a barra lateral direita do editor
- **Login**: Clique no painel Codex → faça login com sua conta OpenAI
- **Atalhos de teclado**: Acesse `Ctrl+Shift+P` → `Preferences: Open Keyboard Shortcuts` → procure por `Codex`

### Funcionalidades Resumidas

| Funcionalidade | Descrição |
|---------------|-----------|
| Prompt com contexto | Use `@arquivo` para referenciar arquivos no prompt |
| Troca de modelos | Alterne modelos pelo seletor abaixo do chat |
| Esforço de raciocínio | Ajuste entre `low`, `medium` e `high` |
| Modos de aprovação | `Chat`, `Agent` e `Agent (Full Access)` |
| Delegação cloud | Envie tarefas pesadas para a nuvem |
| Comandos da IDE | Paleta de comandos com atalhos |
| Slash commands | Comandos `/` diretamente no chat |
| Configurações | Ajuste o comportamento no painel de settings |

---

## 🎯 Exemplos Práticos

### Exemplo 1: Primeiro uso — pedir para explicar um arquivo

```
Abra o arquivo que deseja entender → selecione o código → no painel Codex, escreva:

"Explique o que este código faz, linha por linha."
```

O Codex usará automaticamente o arquivo aberto como contexto.

### Exemplo 2: Referenciar múltiplos arquivos

```
Use @components/Header.tsx e @styles/global.css como referência
para criar um novo componente Footer seguindo o mesmo padrão visual.
```

O `@` permite que o Codex acesse diretamente esses arquivos do seu projeto.

### Exemplo 3: Criando um componente do zero

```
Crie um componente React de modal de login com validação de email
e senha. Use @components/Button.tsx como referência para o estilo
dos botões.
```

---

## 📖 Explicação Didática

### O que acontece "por baixo dos panos"?

Quando você usa a extensão Codex na IDE, o fluxo é:

1. **Você escreve um prompt** no painel do Codex
2. **O Codex analisa o contexto** — arquivos abertos, seleção atual, arquivos referenciados com `@`
3. **O agente processa** — usando o modelo selecionado (ex: GPT-5) com o nível de raciocínio escolhido
4. **No modo Agent**, ele pode executar ações sozinho:
   - Ler/escrever arquivos do projeto
   - Rodar comandos no terminal (ex: `npm test`)
   - Buscar na web por documentação
5. **Você revisa e aprova** as mudanças no diff integrado

### Analogia: é como pair programming

Pense no Codex como um colega de equipe sênior que:
- **Modo Chat** = vocês estão numa reunião de planejamento (só conversa)
- **Modo Agent** = seu colega está no computador dele, fazendo as mudanças, e te pede permissão para coisas fora do escopo
- **Modo Agent Full Access** = seu colega tem acesso total ao repositório (cuidado!)

### Windows: WSL é obrigatório para o modo Agent

No Windows, o Codex **precisa do WSL (Windows Subsystem for Linux)** para executar o modo Agent com segurança. Isso porque a sandbox roda comandos em ambiente Linux isolado. Se você só usar modo Chat, não precisa do WSL.

---

> ⬅️ [Índice](./00_indice.md) | ➡️ [Funcionalidades](./02_funcionalidades.md)
