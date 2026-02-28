# 09 — Regras (Rules)

> 🔗 Fonte oficial: [developers.openai.com/codex/rules](https://developers.openai.com/codex/rules)
> ⬅️ [Config de Exemplo](./08_config_exemplo.md) | ➡️ [AGENTS.md](./10_agents_md.md)

---

## 📄 Documentação Oficial

### O que são Rules?

Rules controlam **quais comandos** o Codex pode executar fora da sandbox. É uma lista de permissão/bloqueio para comandos do terminal.

### Criar um arquivo de regras

1. Crie um arquivo `.rules` em `~/.codex/rules/` (ex: `~/.codex/rules/default.rules`)
2. Adicione regras
3. Reinicie o Codex

### Sintaxe de uma Regra

```python
# Solicitar aprovação antes de rodar 'gh pr view'
prefix_rule(
    pattern = ["gh", "pr", "view"],
    decision = "prompt",
    justification = "Visualizar PRs é permitido com aprovação",
    match = [
        "gh pr view 7888",
        "gh pr view --repo openai/codex",
    ],
    not_match = [
        "gh pr --repo openai/codex view 7888",
    ],
)
```

### Campos de uma Rule

| Campo | Obrigatório | Descrição |
|-------|------------|-----------|
| `pattern` | ✅ | Lista de tokens que formam o prefixo do comando |
| `decision` | Não (padrão: `"allow"`) | `"allow"` · `"prompt"` · `"forbidden"` |
| `justification` | Não | Texto explicativo mostrado ao usuário |
| `match` | Não | Exemplos que **devem** casar com a regra (para testar) |
| `not_match` | Não | Exemplos que **não devem** casar (para testar) |

### Precedência de decisões

Se múltiplas regras casam com um comando, a mais restritiva vence:
`forbidden` > `prompt` > `allow`

### Comandos compostos (shell pipes)

Quando o Codex encontra `bash -lc "git add . && rm -rf /"`:
- Se o script é **simples** (só palavras + `&&`, `||`, `;`, `|`), ele divide em comandos individuais e avalia cada um separadamente
- Se há **lógica complexa** (redireções, variáveis, loops), ele avalia o comando inteiro como um bloco

### Testar uma regra

```bash
codex execpolicy check --pretty \
  --rules ~/.codex/rules/default.rules \
  -- gh pr view 7888
```

### Linguagem

Os arquivos `.rules` usam **Starlark** (parecido com Python, mas seguro — sem acesso ao sistema de arquivos).

---

## 🎯 Exemplos Práticos

### Bloquear `rm -rf` completamente

```python
prefix_rule(
    pattern = ["rm", "-rf"],
    decision = "forbidden",
    justification = "Comando destrutivo proibido. Use 'git clean' para limpar.",
    match = ["rm -rf /", "rm -rf ."],
)
```

### Permitir `npm test` sem aprovação

```python
prefix_rule(
    pattern = ["npm", "test"],
    decision = "allow",
    justification = "Testes são seguros para rodar sem aprovação",
)
```

### Solicitar aprovação para deploys

```python
prefix_rule(
    pattern = ["npm", "run", "deploy"],
    decision = "prompt",
    justification = "Deploy precisa de aprovação manual",
)
```

---

## 📖 Explicação Didática

### Por que Rules existem?

No modo Agent, o Codex gera e executa comandos de terminal automaticamente. Sem Rules, ele poderia executar algo perigoso (ex: `rm -rf /`) se interpretasse mal um prompt. Rules são uma **camada de segurança** que garante que:

1. Comandos seguros rodam sem interrupção
2. Comandos sensíveis pedem aprovação
3. Comandos perigosos são bloqueados

### Smart Approvals — o quê é isso?

Quando você está usando o Codex e ele pede aprovação para um comando, o recurso **Smart Approvals** (ativado por padrão) sugere automaticamente uma `prefix_rule` para você. Se aceitar, o Codex salva em `~/.codex/rules/default.rules` para não perguntar novamente.

---

> ⬅️ [Config de Exemplo](./08_config_exemplo.md) | ➡️ [AGENTS.md](./10_agents_md.md)
