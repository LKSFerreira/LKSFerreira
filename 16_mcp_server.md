# 16 — Codex como MCP Server (Agents SDK)

> 🔗 Fonte oficial: [developers.openai.com/codex/guides/agents-sdk](https://developers.openai.com/codex/guides/agents-sdk)
> ⬅️ [App Server](./15_app_server.md) | ➡️ [GitHub Action](./17_github_action.md)

---

## 📄 Documentação Oficial

### O que é isso?

Você pode rodar o Codex **como um servidor MCP** e conectá-lo a outros agentes. Isso permite criar **workflows multi-agente** usando o OpenAI Agents SDK.

### Iniciar como MCP Server

```bash
codex mcp-server
```

Inspecionar com o MCP Inspector:
```bash
npx @modelcontextprotocol/inspector codex mcp-server
```

### Ferramentas Expostas

| Ferramenta | Descrição | Parâmetros |
|-----------|-----------|------------|
| `codex` | Inicia uma sessão Codex | `prompt`, `approval-policy`, `sandbox`, `model`, `config`, `cwd` |
| `codex-reply` | Continua uma sessão existente | `prompt`, `threadId`, `conversationId` |

### Exemplo: Workflow com um agente

```python
import asyncio
from agents import Agent, Runner
from agents.mcp import MCPServerStdio

async def main() -> None:
    async with MCPServerStdio(
        name="Codex CLI",
        params={
            "command": "npx",
            "args": ["-y", "codex", "mcp-server"],
        },
        client_session_timeout_seconds=360000,
    ) as codex_mcp_server:

        desenvolvedor = Agent(
            name="Game Developer",
            instructions=(
                "Você é expert em jogos HTML+CSS+JS sem dependências. "
                'Sempre chame codex com "approval-policy": "never" '
                'e "sandbox": "workspace-write".'
            ),
            mcp_servers=[codex_mcp_server],
        )

        designer = Agent(
            name="Game Designer",
            instructions=(
                "Crie um brief de design de jogo em 3 frases e "
                "passe para o Game Developer."
            ),
            model="gpt-5",
            handoffs=[desenvolvedor],
        )

        await Runner.run(designer, "Implemente um jogo divertido!")

if __name__ == "__main__":
    asyncio.run(main())
```

### Exemplo: Workflow multi-agente completo

Agentes: **Project Manager** → **Designer** → **Frontend Dev** → **Backend Dev** → **Tester**

```python
import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, ModelSettings, Runner, WebSearchTool, set_default_openai_api
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from agents.mcp import MCPServerStdio
from openai.types.shared import Reasoning

load_dotenv(override=True)
set_default_openai_api(os.getenv("OPENAI_API_KEY"))

async def main() -> None:
    async with MCPServerStdio(
        name="Codex CLI",
        params={"command": "npx", "args": ["-y", "codex", "mcp"]},
        client_session_timeout_seconds=360000,
    ) as codex_mcp_server:

        designer = Agent(
            name="Designer",
            instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
            Você é o Designer. Crie design_spec.md em /design.""",
            mcp_servers=[codex_mcp_server],
        )

        frontend_dev = Agent(
            name="Frontend Developer",
            instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
            Implemente o frontend baseado no design_spec.md.""",
            mcp_servers=[codex_mcp_server],
        )

        # ... backend_dev, tester (padrão similar)

        gerente = Agent(
            name="Project Manager",
            instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
            Coordene: crie REQUIREMENTS.md, AGENT_TASKS.md, TEST.md.
            Depois delegue para Designer → Frontend → Backend → Tester.""",
            model="gpt-5",
            model_settings=ModelSettings(reasoning=Reasoning(effort="medium")),
            handoffs=[designer, frontend_dev],
            mcp_servers=[codex_mcp_server],
        )

        # Handoffs reversos
        designer.handoffs = [gerente]
        frontend_dev.handoffs = [gerente]

        resultado = await Runner.run(gerente, "Crie um jogo Bug Busters", max_turns=30)
        print(resultado.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

### Rastreamento (Traces)

Após a execução, abra o [Traces dashboard](https://platform.openai.com/trace) para inspecionar cada prompt, tool call e handoff.

---

## 📖 Explicação Didática

### Para que serve isso na prática?

1. **Automação de tarefas complexas**: Um "gerente" coordena vários Codex trabalhando em paralelo
2. **Pipelines de desenvolvimento**: Designer → Dev → Tester, tudo automatizado
3. **Code review multi-perspectiva**: Segurança + Performance + Qualidade, cada aspecto com um agente diferente

### Diferença entre Multi-Agent (config.toml) e Agents SDK

| Aspecto | Multi-Agent (config.toml) | Agents SDK |
|---------|--------------------------|------------|
| Configuração | Arquivo TOML | Código Python |
| Flexibilidade | Papéis pré-definidos | Total (qualquer lógica) |
| Handoffs | Automáticos | Programáticos |
| Onde roda | Dentro do Codex | Programa externo que orquestra o Codex |

---

> ⬅️ [App Server](./15_app_server.md) | ➡️ [GitHub Action](./17_github_action.md)
