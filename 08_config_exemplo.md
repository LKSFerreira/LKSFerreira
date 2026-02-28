# 08 — Configuração de Exemplo Completa

> 🔗 Fonte oficial: [developers.openai.com/codex/config-sample](https://developers.openai.com/codex/config-sample)
> ⬅️ [Referência](./07_config_referencia.md) | ➡️ [Regras](./09_regras.md)

---

## 📄 Config de Exemplo Comentada

Copie e adapte este `config.toml` para `~/.codex/config.toml`:

```toml
#:schema https://developers.openai.com/codex/config-schema.json

################################################################################
# Modelo Principal
################################################################################
model = "gpt-5.2-codex"
model_provider = "openai"
model_reasoning_effort = "medium"
# personality = "friendly"      # "friendly" | "pragmatic" | "none"
# review_model = "gpt-5.2-codex"

################################################################################
# Aprovação e Sandbox
################################################################################
approval_policy = "on-request"   # "untrusted" | "on-request" | "never"
sandbox_mode = "read-only"       # "read-only" | "workspace-write" | "danger-full-access"
allow_login_shell = true

[sandbox_workspace_write]
writable_roots = []
network_access = false

################################################################################
# Pesquisa Web
################################################################################
web_search = "cached"  # "cached" | "live" | "disabled"

################################################################################
# Autenticação
################################################################################
cli_auth_credentials_store = "file"  # "file" | "keyring" | "auto"

################################################################################
# Interface (TUI)
################################################################################
file_opener = "vscode"  # "vscode" | "cursor" | "windsurf" | "none"
hide_agent_reasoning = false

[tui]
notifications = false
animations = true
show_tooltips = true

[history]
persistence = "save-all"

################################################################################
# Variáveis de Ambiente
################################################################################
[shell_environment_policy]
inherit = "all"
ignore_default_excludes = true
exclude = []

################################################################################
# Feature Flags
################################################################################
[features]
# multi_agent = false
# shell_snapshot = false
# personality = true

################################################################################
# Servidores MCP
################################################################################
[mcp_servers]
# [mcp_servers.context7]
# command = "npx"
# args = ["-y", "@upstash/context7-mcp"]

################################################################################
# Provedores de Modelo
################################################################################
[model_providers]
# [model_providers.azure]
# name = "Azure"
# base_url = "https://SEU_PROJETO.openai.azure.com/openai"
# wire_api = "responses"
# env_key = "AZURE_OPENAI_API_KEY"

# [model_providers.ollama]
# name = "Ollama"
# base_url = "http://localhost:11434/v1"
# wire_api = "chat"

################################################################################
# Perfis (presets nomeados)
################################################################################
[profiles]
# [profiles.rapido]
# model = "gpt-5.2-codex"
# model_reasoning_effort = "low"

################################################################################
# Windows
################################################################################
[windows]
sandbox = "unelevated"
```

---

## 🎯 Exemplo: Config para Desenvolvedor JavaScript/TypeScript

```toml
model = "gpt-5.2-codex"
model_reasoning_effort = "medium"
approval_policy = "on-request"
sandbox_mode = "workspace-write"
web_search = "cached"
personality = "pragmatic"
file_opener = "vscode"

[sandbox_workspace_write]
network_access = true           # permite npm install
writable_roots = ["/tmp"]

[shell_environment_policy]
inherit = "all"
exclude = ["AWS_*", "AZURE_*"]  # não vazar secrets

[features]
shell_snapshot = true            # acelera execuções repetidas
```

---

## 📖 Explicação Didática

### Perfis (Profiles) — para que servem?

Perfis permitem ter **configurações pré-definidas** que você alterna rapidamente:

```toml
[profiles.revisao]
model = "gpt-5.2-codex"
model_reasoning_effort = "high"
sandbox_mode = "read-only"

[profiles.implementacao]
model = "gpt-5.2-codex"
model_reasoning_effort = "medium"
sandbox_mode = "workspace-write"
```

Na CLI: `codex --profile revisao "Revise este PR"`

---

> ⬅️ [Referência](./07_config_referencia.md) | ➡️ [Regras](./09_regras.md)
