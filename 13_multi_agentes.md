# 13 — Multi-Agentes

> 🔗 Fonte oficial: [developers.openai.com/codex/multi-agent](https://developers.openai.com/codex/multi-agent)
> ⬅️ [Skills](./12_skills.md) | ➡️ [Modo Não-Interativo](./14_modo_nao_interativo.md)

---

## 📄 Documentação Oficial

### O que é Multi-Agent?

Permite que o Codex **spawne múltiplos sub-agentes** que trabalham em paralelo, cada um com um papel específico. É como ter uma equipe de programadores trabalhando ao mesmo tempo.

> ⚠️ **Experimental**: Este recurso precisa ser habilitado explicitamente.

### Habilitar Multi-Agent

Via CLI:
```bash
# Na TUI do Codex:
/experimental
# Ative "Multi-agents" → reinicie
```

Via config:
```toml
# ~/.codex/config.toml
[features]
multi_agent = true
```

### Fluxo Típico

1. Você pede uma tarefa grande
2. O Codex decide (ou você pede) que precisa de vários agentes
3. Cada sub-agente trabalha em paralelo
4. O Codex consolida os resultados

### Gerenciar Sub-Agentes

- `/agent` — alterna entre threads de agentes na CLI
- Peça diretamente para parar/redirecionar um sub-agente
- `wait` — suporta polling longo (até 1 hora por chamada)

### Aprovações e Sandbox

Sub-agentes **herdam** a política de sandbox, mas rodam com **aprovações não-interativas**. Se um sub-agente tentar algo que precisaria de aprovação, a ação **falha** e o erro aparece no workflow pai.

### Papéis de Agente (Roles)

Papéis built-in:

| Papel | Foco |
|-------|------|
| `default` | Propósito geral |
| `worker` | Implementação e correções |
| `explorer` | Exploração de codebase (read-only) |
| `monitor` | Monitoramento de tarefas longas |

#### Configurar papéis customizados

```toml
# .codex/config.toml
[agents]
max_threads = 6
max_depth = 1

[agents.reviewer]
description = "Revisor de PRs focado em segurança e testes."
config_file = "agents/reviewer.toml"
```

Arquivo `agents/reviewer.toml`:
```toml
model = "gpt-5.2-codex"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
developer_instructions = """
Revise como um dono do código. Priorize: correção, segurança,
regressões e cobertura de testes.
"""
```

---

## 🎯 Exemplos Práticos

### Review de PR em paralelo

```
Quero revisar os seguintes pontos do PR atual (esta branch vs main).
Spawne um agente por ponto, espere todos, e resuma o resultado:
1. Segurança
2. Qualidade de código
3. Bugs
4. Race conditions
5. Flakiness de testes
6. Manutenibilidade
```

### Time de Frontend Debugging

```toml
# .codex/config.toml
[agents]
max_threads = 6
max_depth = 1

[agents.explorer]
description = "Explora o código-fonte e mapeia os caminhos."
config_file = "agents/explorer.toml"

[agents.browser_debugger]
description = "Reproduz bugs no browser usando DevTools."
config_file = "agents/browser-debugger.toml"

[agents.worker]
description = "Implementa correções pontuais."
config_file = "agents/worker.toml"
```

Prompt:
```
Investigue por que o modal de settings não salva. Tenha o
browser_debugger reproduzindo, o explorer traçando o caminho
no código, e o worker implementando o fix mais simples.
```

---

## 📖 Explicação Didática

### Analogia: Multi-Agent = equipe de desenvolvimento

Pense assim:
- Você é o **Tech Lead** dando a diretiva
- O Codex é o **Gerente de Projeto** que distribui tarefas
- Os sub-agentes são os **desenvolvedores** trabalhando em paralelo

O Codex garante que nenhum sub-agente faça algo não autorizado (aprovações), e consolida tudo no final.

### `max_depth` — o que controla?

É a **profundidade de nesting**. Com `max_depth = 1`:
- O agente principal pode spawnar sub-agentes
- Sub-agentes **não podem** spawnar seus próprios sub-agentes

Com `max_depth = 2`, sub-agentes podem criar sub-sub-agentes (cuidado!).

### Quando NÃO usar multi-agent

- Tarefas simples (um arquivo, uma função)
- Quando ordem importa (passos sequenciais dependentes)
- Para evitar consumo excessivo de tokens em tarefas triviais

---

> ⬅️ [Skills](./12_skills.md) | ➡️ [Modo Não-Interativo](./14_modo_nao_interativo.md)
