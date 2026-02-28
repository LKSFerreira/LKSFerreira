# 06 — Configuração Básica (config.toml)

> 🔗 Fonte oficial: [developers.openai.com/codex/config-basic](https://developers.openai.com/codex/config-basic)
> ⬅️ [Slash Commands](./05_slash_commands.md) | ➡️ [Referência de Configuração](./07_config_referencia.md)

---

## 📄 Documentação Oficial

### Arquivo de Configuração

O Codex armazena configurações em **TOML** em dois níveis:

| Escopo | Localização | Uso |
|--------|------------|-----|
| **Usuário (global)** | `~/.codex/config.toml` | Preferências pessoais (todas as máquinas) |
| **Projeto (local)** | `.codex/config.toml` (na raiz do repo) | Configurações específicas do projeto |

Na extensão IDE: clique no ícone de engrenagem → `Codex Settings` → `Open config.toml`.

### Precedência de Configuração

Ordem de prioridade (maior para menor):

1. **Flags CLI** e `--config` overrides
2. **Perfil** ativo (`--profile <nome>`)
3. **Config do projeto**: `.codex/config.toml` (apenas projetos confiáveis)
4. **Config do usuário**: `~/.codex/config.toml`
5. **Config do sistema**: `/etc/codex/config.toml` (Unix)
6. **Padrões internos**

### Opções Mais Usadas

#### Modelo Padrão
```toml
model = "gpt-5.2"
```

#### Política de Aprovação
```toml
approval_policy = "on-request"
# Opções: "untrusted" | "on-request" | "never"
```

- `untrusted`: Só comandos read-only são auto-executados; o resto pede aprovação
- `on-request`: O modelo decide quando perguntar (padrão)
- `never`: Nunca pede aprovação (arriscado!)

#### Nível da Sandbox
```toml
sandbox_mode = "workspace-write"
# Opções: "read-only" | "workspace-write" | "danger-full-access"
```

#### Windows Sandbox
```toml
[windows]
sandbox = "elevated"  # Recomendado (precisa de admin)
# sandbox = "unelevated"  # Fallback se não tiver admin
```

#### Pesquisa Web
```toml
web_search = "cached"   # padrão — cache da OpenAI
# web_search = "live"   # busca em tempo real
# web_search = "disabled"
```

#### Esforço de Raciocínio
```toml
model_reasoning_effort = "high"
# Opções: "minimal" | "low" | "medium" | "high" | "xhigh"
```

#### Estilo de Comunicação
```toml
personality = "friendly"  # ou "pragmatic" ou "none"
```

#### Variáveis de Ambiente para Comandos
```toml
[shell_environment_policy]
include_only = ["PATH", "HOME"]
```

#### Diretório de Logs
```toml
log_dir = "/caminho/para/logs"
```

### Feature Flags

Ative funcionalidades experimentais na seção `[features]`:

```toml
[features]
shell_snapshot = true   # Acelera comandos repetidos
multi_agent = true      # Habilita colaboração entre agentes
```

Para ativar via CLI:
```bash
codex --enable shell_snapshot
codex --enable multi_agent
```

---

## 🎯 Exemplos Práticos

### Config mínima para uso diário

```toml
# ~/.codex/config.toml
model = "gpt-5.2-codex"
model_reasoning_effort = "medium"
approval_policy = "on-request"
sandbox_mode = "workspace-write"
web_search = "cached"
personality = "pragmatic"
```

### Config para projetos que usam Docker

```toml
# .codex/config.toml (na raiz do projeto)
sandbox_mode = "workspace-write"

[sandbox_workspace_write]
network_access = true
writable_roots = ["/tmp"]
```

---

## 📖 Explicação Didática

### `config.toml` — por que TOML e não JSON?

TOML é mais legível para humanos, suporta comentários (JSON não suporta) e é o padrão em ferramentas de linha de comando modernas (Rust, Python, etc).

### Sandbox — as 3 camadas de segurança

Pense na sandbox como um quarto isolado onde o Codex trabalha:

1. **`read-only`**: Ele pode **olhar** seus arquivos, mas não pode **tocar** em nada
2. **`workspace-write`**: Ele pode **editar** arquivos da pasta do projeto, mas não pode acessar a internet nem outras pastas
3. **`danger-full-access`**: O quarto está **aberto** — ele faz o que quiser (use apenas em ambientes controlados como CI)

---

> ⬅️ [Slash Commands](./05_slash_commands.md) | ➡️ [Referência de Configuração](./07_config_referencia.md)
