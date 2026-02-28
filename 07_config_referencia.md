# 07 — Referência Completa de Configuração

> 🔗 Fonte oficial: [developers.openai.com/codex/config-reference](https://developers.openai.com/codex/config-reference)
> ⬅️ [Config Básica](./06_config_basica.md) | ➡️ [Config de Exemplo](./08_config_exemplo.md)

---

## 📄 Documentação Oficial

Esta é a referência completa de **todas as chaves** disponíveis no `config.toml`. Para autocompletar no VS Code, adicione no topo do arquivo:

```toml
#:schema https://developers.openai.com/codex/config-schema.json
```

### Modelo e Provedor

| Chave | Tipo | Descrição |
|-------|------|-----------|
| `model` | string | Modelo a usar (ex: `"gpt-5-codex"`) |
| `model_provider` | string | ID do provedor (padrão: `"openai"`) |
| `model_reasoning_effort` | enum | `minimal` · `low` · `medium` · `high` · `xhigh` |
| `model_reasoning_summary` | enum | `auto` · `concise` · `detailed` · `none` |
| `model_verbosity` | enum | `low` · `medium` · `high` |
| `model_context_window` | number | Janela de contexto em tokens |
| `model_auto_compact_token_limit` | number | Limite para compactação automática do histórico |
| `model_instructions_file` | path | Arquivo para substituir instruções built-in |
| `review_model` | string | Modelo para `/review` (padrão: modelo da sessão) |
| `personality` | enum | `none` · `friendly` · `pragmatic` |

### Aprovação e Sandbox

| Chave | Tipo | Descrição |
|-------|------|-----------|
| `approval_policy` | enum/object | `untrusted` · `on-request` · `never` · `{ reject = {...} }` |
| `sandbox_mode` | enum | `read-only` · `workspace-write` · `danger-full-access` |
| `sandbox_workspace_write.writable_roots` | array | Diretórios extras de escrita |
| `sandbox_workspace_write.network_access` | boolean | Permitir rede na sandbox |
| `allow_login_shell` | boolean | Permitir shells de login |

### Servidores MCP

| Chave | Tipo | Descrição |
|-------|------|-----------|
| `mcp_servers.<id>.command` | string | Comando para STDIO server |
| `mcp_servers.<id>.args` | array | Argumentos para o server |
| `mcp_servers.<id>.url` | string | URL para HTTP server |
| `mcp_servers.<id>.env` | map | Variáveis de ambiente |
| `mcp_servers.<id>.enabled` | boolean | Ativar/desativar sem remover |
| `mcp_servers.<id>.required` | boolean | Falhar se não inicializar |
| `mcp_servers.<id>.enabled_tools` | array | Lista de ferramentas permitidas |
| `mcp_servers.<id>.disabled_tools` | array | Lista de ferramentas bloqueadas |
| `mcp_servers.<id>.startup_timeout_sec` | number | Timeout de inicialização (padrão: 10s) |
| `mcp_servers.<id>.tool_timeout_sec` | number | Timeout por ferramenta (padrão: 60s) |

### Multi-Agentes

| Chave | Tipo | Descrição |
|-------|------|-----------|
| `agents.max_threads` | number | Máximo de agentes simultâneos |
| `agents.max_depth` | number | Profundidade máxima de nesting |
| `agents.<name>.description` | string | Quando usar este agente |
| `agents.<name>.config_file` | path | Config TOML para o papel do agente |

### Skills

| Chave | Tipo | Descrição |
|-------|------|-----------|
| `skills.config` | array | Overrides por skill |
| `skills.config.<index>.path` | path | Caminho para a pasta da skill |
| `skills.config.<index>.enabled` | boolean | Ativar/desativar a skill |

### Web Search

| Chave | Tipo | Descrição |
|-------|------|-----------|
| `web_search` | enum | `disabled` · `cached` · `live` |

### Histórico e Interface

| Chave | Tipo | Descrição |
|-------|------|-----------|
| `history.persistence` | enum | `save-all` · `none` |
| `history.max_bytes` | number | Tamanho máximo do histórico |
| `file_opener` | enum | `vscode` · `cursor` · `windsurf` · `none` |
| `log_dir` | path | Diretório de logs |
| `tui.notifications` | boolean/array | Notificações do terminal |
| `tui.animations` | boolean | Animações da TUI |

### Provedores de Modelo Customizados

| Chave | Tipo | Descrição |
|-------|------|-----------|
| `model_providers.<id>.base_url` | string | URL base da API |
| `model_providers.<id>.env_key` | string | Variável de ambiente com a API key |
| `model_providers.<id>.wire_api` | enum | `chat` · `responses` |

### requirements.toml (Admin)

Arquivo `requirements.toml` para admins imporem restrições:

| Chave | Tipo | Descrição |
|-------|------|-----------|
| `allowed_approval_policies` | array | Políticas permitidas |
| `allowed_sandbox_modes` | array | Modos de sandbox permitidos |
| `allowed_web_search_modes` | array | Modos de web search permitidos |

---

## 📖 Explicação Didática

### Provedores Customizados — o que são?

O Codex não precisa usar apenas a API da OpenAI. Você pode configurar provedores alternativos como **Azure OpenAI**, **Ollama** (local), ou qualquer API compatível com OpenAI. Veja exemplos em [Config de Exemplo](./08_config_exemplo.md).

### `requirements.toml` — para quem é?

É um arquivo de controle **para administradores de equipe**. Se sua empresa quer impedir que desenvolvedores usem `danger-full-access`, o admin coloca essa restrição no `requirements.toml` e ninguém consegue sobrescrever.

---

> ⬅️ [Config Básica](./06_config_basica.md) | ➡️ [Config de Exemplo](./08_config_exemplo.md)
