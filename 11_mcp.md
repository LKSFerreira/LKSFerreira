# 11 — MCP (Model Context Protocol)

> 🔗 Fonte oficial: [developers.openai.com/codex/mcp](https://developers.openai.com/codex/mcp)
> ⬅️ [AGENTS.md](./10_agents_md.md) | ➡️ [Skills](./12_skills.md)

---

## 📄 Documentação Oficial

### O que é MCP?

MCP (Model Context Protocol) permite **conectar o Codex a ferramentas de terceiros**. É como dar ao agente acesso a aplicativos externos — Figma, GitHub, Sentry, navegadores, etc.

### Tipos de servidor MCP

| Tipo | Como funciona |
|------|--------------|
| **STDIO** | Roda como processo local (você instala via `npx` ou binário) |
| **Streamable HTTP** | Você acessa via URL (servidores remotos) |

### Autenticação suportada

- Variáveis de ambiente
- Bearer token
- OAuth (`codex mcp login <nome-do-server>`)

### Configurar via CLI

```bash
# Adicionar um servidor MCP
codex mcp add context7 -- npx -y @upstash/context7-mcp

# Adicionar com variáveis de ambiente
codex mcp add meu-server --env API_KEY=abc123 -- meu-server-cli

# Ver comandos disponíveis
codex mcp --help

# Na TUI, ver servidores ativos
/mcp
```

### Configurar via config.toml

#### Servidor STDIO
```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]

[mcp_servers.context7.env]
MY_ENV_VAR = "MY_ENV_VALUE"
```

#### Servidor HTTP
```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
http_headers = { "X-Figma-Region" = "us-east-1" }
```

#### Opções adicionais
```toml
[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
enabled_tools = ["open", "screenshot"]
disabled_tools = ["screenshot"]
startup_timeout_sec = 20
tool_timeout_sec = 45
enabled = true
```

### Servidores MCP Úteis

| Servidor | Descrição |
|----------|-----------|
| [OpenAI Docs](https://developers.openai.com/resources/docs-mcp) | Busca na documentação da OpenAI |
| [Context7](https://github.com/upstash/context7) | Documentação de dev atualizada |
| [Figma](https://developers.figma.com/) | Acesso aos seus designs |
| [Playwright](https://www.npmjs.com/package/@playwright/mcp) | Controle de browser para testes |
| [Chrome DevTools](https://github.com/ChromeDevTools/chrome-devtools-mcp/) | Inspecionar e controlar o Chrome |
| [Sentry](https://docs.sentry.io/product/sentry-mcp/#codex) | Acessar logs de erro |
| [GitHub](https://github.com/github/github-mcp-server) | Gerenciar PRs, issues, etc. |

---

## 🎯 Exemplos Práticos

### Instalar Context7 para documentação atualizada

```bash
codex mcp add context7 -- npx -y @upstash/context7-mcp
```

Agora o Codex pode buscar documentação de qualquer framework/biblioteca quando precisar.

### Configurar GitHub MCP para gerenciar PRs

```toml
[mcp_servers.github]
url = "https://github-mcp.example.com/mcp"
bearer_token_env_var = "GITHUB_TOKEN"
enabled_tools = ["list_issues", "create_pr"]
```

---

## 📖 Explicação Didática

### Analogia: MCP = plugins para o cérebro do Codex

O Codex, por padrão, só sabe ler e editar código no seu repositório. Com MCP, você instala **plugins** que dão capacidades extras:

- **Plugin Figma**: O Codex consegue ver seus mockups e gerar código baseado neles
- **Plugin GitHub**: O Codex consegue criar PRs e gerenciar issues diretamente
- **Plugin Sentry**: O Codex consegue ler logs de erro e propor correções

### STDIO vs. HTTP — quando usar cada um?

- **STDIO**: Use quando o servidor MCP é uma ferramenta que roda **na sua máquina** (ex: Context7, Playwright). É mais rápido e não precisa de infraestrutura.
- **HTTP**: Use quando o servidor é **remoto** (ex: Figma na nuvem). Precisa de autenticação.

### Compartilhamento IDE ↔ CLI

A configuração MCP é **compartilhada** entre a extensão IDE e a CLI. Configure uma vez em `~/.codex/config.toml` e funciona em ambos.

---

> ⬅️ [AGENTS.md](./10_agents_md.md) | ➡️ [Skills](./12_skills.md)
