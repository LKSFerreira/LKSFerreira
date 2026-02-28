# 15 — App Server

> 🔗 Fonte oficial: [developers.openai.com/codex/app-server](https://developers.openai.com/codex/app-server)
> ⬅️ [Modo Não-Interativo](./14_modo_nao_interativo.md) | ➡️ [MCP Server](./16_mcp_server.md)

---

## 📄 Documentação Oficial

### O que é o App Server?

O App Server é um **protocolo** que permite embutir o Codex dentro de outros produtos. Pense nele como uma API local para controlar o Codex programaticamente.

### Protocolo

- Baseado em **JSON-RPC 2.0** (sem o header `"jsonrpc":"2.0"`)
- Comunicação **bidirecional**: você envia requests, recebe responses e notifications

### Transportes Suportados

| Transporte | Flag | Formato |
|-----------|------|---------|
| **stdio** (padrão) | `--listen stdio://` | JSONL (uma linha JSON por mensagem) |
| **WebSocket** (experimental) | `--listen ws://IP:PORT` | Um JSON-RPC por frame |

### Primitivas Principais

| Conceito | Descrição |
|----------|-----------|
| **Thread** | Uma conversa com o agente. Contém turns. |
| **Turn** | Um request do usuário + a resposta do agente. Contém items. |
| **Item** | Unidade de IO: mensagem, execução de comando, mudança de arquivo, etc. |

### Ciclo de Vida

```
1. initialize     → Handshake com metadata do cliente
2. initialized    → Confirma que está pronto
3. thread/start   → Inicia nova conversa
4. turn/start     → Envia input do usuário
5. [notifications]→ item/started, item/completed, deltas...
6. turn/completed → Agente terminou
```

### Iniciar o Server

```bash
# STDIO (padrão)
codex app-server

# WebSocket
codex app-server --listen ws://127.0.0.1:4500
```

### Exemplo: Cliente Node.js

```typescript
import { spawn } from "node:child_process";
import readline from "node:readline";

const proc = spawn("codex", ["app-server"], {
  stdio: ["pipe", "pipe", "inherit"],
});

const rl = readline.createInterface({ input: proc.stdout });

const enviar = (mensagem: unknown) => {
  proc.stdin.write(`${JSON.stringify(mensagem)}\n`);
};

let threadId: string | null = null;

rl.on("line", (linha) => {
  const msg = JSON.parse(linha) as any;
  console.log("servidor:", msg);

  if (msg.id === 1 && msg.result?.thread?.id && !threadId) {
    threadId = msg.result.thread.id;
    enviar({
      method: "turn/start",
      id: 2,
      params: {
        threadId,
        input: [{ type: "text", text: "Resuma este repositório." }],
      },
    });
  }
});

// Handshake
enviar({
  method: "initialize",
  id: 0,
  params: {
    clientInfo: { name: "meu_produto", title: "Meu Produto", version: "0.1.0" },
  },
});
enviar({ method: "initialized", params: {} });

// Iniciar conversa
enviar({ method: "thread/start", id: 1, params: { model: "gpt-5.2-codex" } });
```

### Gerar Schemas

```bash
codex app-server generate-ts --out ./schemas
codex app-server generate-json-schema --out ./schemas
```

---

## 📖 Explicação Didática

### Para quem é o App Server?

Para **desenvolvedores que querem integrar o Codex em seus próprios produtos**:
- Uma IDE customizada
- Um dashboard interno de DevOps
- Um chatbot especializado
- Uma ferramenta de code review automatizada

### Analogia: é como uma API REST, mas via processo local

Em vez de chamar `https://api.openai.com/...`, você spawna o processo `codex app-server` e conversa com ele via stdin/stdout (como um pipe Unix) ou WebSocket.

### Thread vs. Turn vs. Item

```
Thread (conversa)
├── Turn 1 (usuário pergunta algo)
│   ├── Item: mensagem do agente
│   ├── Item: execução de comando (npm test)
│   └── Item: mudança de arquivo (fix.ts)
├── Turn 2 (follow-up)
│   └── Item: mensagem do agente
```

---

> ⬅️ [Modo Não-Interativo](./14_modo_nao_interativo.md) | ➡️ [MCP Server](./16_mcp_server.md)
