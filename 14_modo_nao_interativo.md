# 14 — Modo Não-Interativo (codex exec)

> 🔗 Fonte oficial: [developers.openai.com/codex/noninteractive](https://developers.openai.com/codex/noninteractive)
> ⬅️ [Multi-Agentes](./13_multi_agentes.md) | ➡️ [App Server](./15_app_server.md)

---

## 📄 Documentação Oficial

### Quando usar `codex exec`

- Automação em **pipelines** (CI/CD, pre-merge, jobs agendados)
- Gerar saídas para **pipar** em outras ferramentas
- Rodar com sandbox e aprovações **pré-definidas** (sem interação humana)

### Uso Básico

```bash
# Prompt simples
codex exec "resuma a estrutura do repositório e liste as 5 áreas de risco"

# Redirecionar saída
codex exec "gere notas de release dos últimos 10 commits" | tee release-notes.md

# Modo efêmero (não persiste sessão)
codex exec --ephemeral "faça triagem do repositório"
```

### Permissões

```bash
# Padrão: read-only
codex exec "analise o código"

# Permitir edições
codex exec --full-auto "corrija o bug no arquivo main.ts"

# Acesso total (apenas em ambientes controlados!)
codex exec --sandbox danger-full-access "instale e configure o projeto"
```

### Saída em JSON (Machine-Readable)

```bash
codex exec --json "resuma a estrutura do repo" | jq
```

Eventos emitidos:
- `thread.started` → `turn.started` → `item.started` → `item.completed` → `turn.completed`

### Saída Estruturada (Schema)

```bash
# Definir um schema JSON
cat > schema.json << 'EOF'
{
  "type": "object",
  "properties": {
    "nome_projeto": { "type": "string" },
    "linguagens": { "type": "array", "items": { "type": "string" } }
  },
  "required": ["nome_projeto", "linguagens"],
  "additionalProperties": false
}
EOF

# Executar com schema
codex exec "Extraia metadados do projeto" \
  --output-schema ./schema.json \
  -o ./metadados.json
```

### Autenticação em CI

```bash
# Via variável de ambiente
CODEX_API_KEY=sk-... codex exec --json "triagem de bug reports"
```

> `CODEX_API_KEY` só é suportado no `codex exec`.

### Resumir Sessão

```bash
# Executar em partes
codex exec "revise o código para race conditions"
codex exec resume --last "corrija as race conditions encontradas"

# Ou com ID específico
codex exec resume <SESSION_ID> "continue a tarefa"
```

### Requisito: Git

O Codex exige rodar dentro de um repositório Git. Para ignorar:
```bash
codex exec --skip-git-repo-check "..."
```

---

## 🎯 Exemplos Práticos

### Auto-fix de CI com GitHub Actions

```yaml
name: Codex auto-fix em falha de CI

on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]

jobs:
  auto-fix:
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    runs-on: ubuntu-latest
    env:
      OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}

    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0

      - name: Instalar Codex
        run: npm i -g @openai/codex

      - name: Autenticar
        run: codex login --api-key "$OPENAI_API_KEY"

      - name: Corrigir
        run: |
          codex exec --full-auto --sandbox workspace-write \
            "Leia o repositório, rode os testes, identifique a correção mínima para passar, implemente e pare."

      - name: Verificar
        run: npm test --silent

      - name: Criar PR
        if: success()
        uses: peter-evans/create-pull-request@v6
        with:
          branch: codex/auto-fix-${{ github.event.workflow_run.run_id }}
          title: "Auto-fix via Codex"
```

### Script de geração de documentação diária

```bash
#!/bin/bash
CODEX_API_KEY=$OPENAI_KEY codex exec --ephemeral \
  "Analise as mudanças dos últimos commits e gere um resumo
   técnico das alterações mais relevantes." \
  -o ./docs/resumo-diario.md
```

---

## 📖 Explicação Didática

### `codex exec` vs. usar o Codex na IDE

| Aspecto | IDE / TUI | `codex exec` |
|---------|-----------|-------------|
| Interação | Conversa contínua | Uma tarefa, sem follow-up |
| Saída | Visual no editor | stdout (para scripts) |
| Aprovações | Interativas (você clica) | Automáticas (sem humano) |
| Uso principal | Desenvolvimento | CI/CD e automação |

### `--json` vs. `--output-schema`

- `--json`: Emite **todos os eventos** como JSON Lines (debug e monitoramento)
- `--output-schema`: Força que a **resposta final** siga um formato JSON específico (para downstream tools)

---

> ⬅️ [Multi-Agentes](./13_multi_agentes.md) | ➡️ [App Server](./15_app_server.md)
