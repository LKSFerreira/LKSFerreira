# 03 — Configurações da Extensão Codex na IDE

> 🔗 Fonte oficial: [developers.openai.com/codex/ide/settings](https://developers.openai.com/codex/ide/settings)
> ⬅️ [Funcionalidades](./02_funcionalidades.md) | ➡️ [Comandos](./04_comandos_ide.md)

---

## 📄 Documentação Oficial

### Como alterar uma configuração

1. Abra as configurações do editor (`Ctrl+,`)
2. Busque por `Codex` ou pelo nome da configuração
3. Altere o valor

### Referência de Configurações

| Setting | O que faz |
|---------|-----------|
| `chatgpt.cliExecutable` | Caminho para o executável do Codex CLI. **Não altere** a menos que esteja desenvolvendo a CLI. |
| `chatgpt.commentCodeLensEnabled` | Ativa botões CodeLens acima de comentários `// TODO` para implementação automática pelo Codex. |
| `chatgpt.composerEnterBehavior` | Define o que a tecla `Enter` faz no painel do Codex (`enter` = envia, `shift+enter` = nova linha). |
| `chatgpt.followUpQueueMode` | Controla como mensagens de follow-up são tratadas (`queue` = fila, ou interrompe a tarefa atual). |
| `chatgpt.localeOverride` | Força o idioma da interface do Codex. Vazio = auto-detect. |
| `chatgpt.openOnStartup` | Se marcado, abre automaticamente a sidebar do Codex ao iniciar o editor. |
| `chatgpt.runCodexInWindowsSubsystemForLinux` | **(Windows)** Executa o Codex dentro do WSL para melhor sandbox e performance. **Modo Agent requer WSL no Windows.** |

### Configurações Avançadas (via config.toml)

Algumas configurações como modelo padrão, aprovações e sandbox **não ficam no editor**, e sim no arquivo `~/.codex/config.toml`. Veja [Configuração Básica](./06_config_basica.md).

---

## 🎯 Exemplos Práticos

### Ativar CodeLens para TODOs

Com `chatgpt.commentCodeLensEnabled` ativado, qualquer comentário `// TODO` no código ganha um botão clicável acima:

```javascript
// TODO: validar email antes de enviar o formulário
function enviarFormulario() {
  // O Codex mostrará um botão "Implement with Codex" acima do TODO
}
```

Clicar no botão faz o Codex implementar automaticamente o que está descrito.

### WSL no Windows — configuração recomendada

Se você usa Windows:
1. Instale o WSL: `wsl --install` no PowerShell (como admin)
2. Ative `chatgpt.runCodexInWindowsSubsystemForLinux` nas settings
3. Reinicie o VS Code

Isso garante que o modo Agent funcione com sandbox segura.

---

## 📖 Explicação Didática

### Por que o Codex precisa do WSL no Windows?

O modo Agent executa comandos de terminal (como `npm install`, `git status`). No Linux/macOS, o Codex cria uma **sandbox** (ambiente isolado) que impede que comandos perigosos afetem seu sistema. No Windows, essa sandbox não funciona nativamente — por isso ele roda dentro do WSL, que é essencialmente um Linux dentro do Windows.

### CodeLens — o que é?

CodeLens é uma funcionalidade do VS Code que exibe informações contextuais **acima de linhas de código** (ex: "3 referências", "último commit"). O Codex adiciona seu próprio CodeLens para comentários `TODO`, permitindo implementação com um clique.

---

> ⬅️ [Funcionalidades](./02_funcionalidades.md) | ➡️ [Comandos](./04_comandos_ide.md)
