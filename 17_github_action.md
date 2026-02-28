# 17 — Codex GitHub Action

> 🔗 Fonte oficial: [developers.openai.com/codex/github-action](https://developers.openai.com/codex/github-action)
> ⬅️ [MCP Server](./16_mcp_server.md) | ⬅️ [Índice](./00_indice.md)

---

## 📄 Documentação Oficial

### O que é?

A Codex GitHub Action permite rodar o `codex exec` dentro de workflows do GitHub Actions. Automatize revisões de PR, geração de docs, correção de bugs e mais.

### Pré-requisitos

1. Armazene sua API key como secret: `OPENAI_API_KEY`
2. Use runner Linux ou macOS (no Windows, use `safety-strategy: unsafe`)
3. Faça checkout do código antes de invocar a action
4. Forneça o prompt via `prompt` (inline) ou `prompt-file` (arquivo)

### Exemplo: Review de PRs

```yaml
name: Codex review de PR

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  codex:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    outputs:
      final_message: ${{ steps.run_codex.outputs.final-message }}

    steps:
      - uses: actions/checkout@v5
        with:
          ref: refs/pull/${{ github.event.pull_request.number }}/merge

      - name: Buscar refs
        run: |
          git fetch --no-tags origin \
            ${{ github.event.pull_request.base.ref }} \
            +refs/pull/${{ github.event.pull_request.number }}/head

      - name: Rodar Codex
        id: run_codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt-file: .github/codex/prompts/review.md
          output-file: codex-output.md
          safety-strategy: drop-sudo
          sandbox: workspace-write

  post_feedback:
    runs-on: ubuntu-latest
    needs: codex
    if: needs.codex.outputs.final_message != ''
    steps:
      - name: Postar feedback
        uses: actions/github-script@v7
        with:
          github-token: ${{ github.token }}
          script: |
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body: process.env.CODEX_FINAL_MESSAGE,
            });
        env:
          CODEX_FINAL_MESSAGE: ${{ needs.codex.outputs.final_message }}
```

### Configurações da Action

| Input | Descrição |
|-------|-----------|
| `prompt` / `prompt-file` | Instrução inline ou caminho para arquivo de prompt |
| `codex-args` | Flags CLI extras (JSON array ou string) |
| `model` | Modelo a usar |
| `effort` | Esforço de raciocínio |
| `sandbox` | `read-only` · `workspace-write` · `danger-full-access` |
| `safety-strategy` | `drop-sudo` (padrão) · `unsafe` · `unprivileged-user` |
| `output-file` | Salvar resposta final em arquivo |
| `codex-version` | Pinar versão específica da CLI |
| `codex-home` | Diretório home customizado |
| `allow-users` | Lista de usuários autorizados |
| `allow-bots` | Lista de bots autorizados |

### Segurança

| Estratégia | Comportamento |
|-----------|--------------|
| `drop-sudo` (padrão) | Remove `sudo` antes de rodar Codex — **irreversível no job** |
| `unsafe` | Sem restrição (necessário no Windows) |
| `unprivileged-user` | Roda como usuário específico sem privilégio |

### Capturar Saída

- `final-message` → output da action
- `output-file` → salva a resposta final em arquivo
- `--output-schema` via `codex-args` → forçar formato JSON

### Checklist de Segurança

- ✅ Limite quem pode triggerar o workflow
- ✅ Sanitize inputs de PRs (evitar prompt injection)
- ✅ Mantenha `safety-strategy: drop-sudo`
- ✅ Rode Codex como **último step** do job
- ✅ Rotacione API keys se suspeitou de exposição

---

## 🎯 Exemplos Práticos

### Prompt file para review de PR

```markdown
<!-- .github/codex/prompts/review.md -->

Revise este Pull Request focando em:
1. Bugs ou erros lógicos
2. Vulnerabilidades de segurança
3. Testes ausentes para lógica crítica
4. Performance issues em loops ou queries
5. Legibilidade e manutenibilidade

Formate a resposta como uma lista de findings com:
- **Severidade** (Crítica/Alta/Média/Baixa)
- **Arquivo:Linha**
- **Descrição**
- **Sugestão de correção**
```

### Auto-fix de testes falhando

```yaml
- name: Corrigir testes
  uses: openai/codex-action@v1
  with:
    openai-api-key: ${{ secrets.OPENAI_API_KEY }}
    prompt: |
      Leia o repositório, rode npm test, identifique a correção mínima
      para todos os testes passarem, implemente e pare.
    sandbox: workspace-write
    codex-args: '["--full-auto"]'
```

---

## 📖 Explicação Didática

### `safety-strategy: drop-sudo` — por que é importante?

Runners do GitHub têm acesso a `sudo`. Se o Codex for comprometido (prompt injection), ele poderia acessar secrets em memória ou alterar o sistema. Remover `sudo` antes de rodar o Codex é uma camada de proteção contra isso.

### Prompt file vs. prompt inline

- **Inline** (`prompt`): Para prompts curtos e simples
- **File** (`prompt-file`): Para prompts complexos, versionados no repositório, e reutilizáveis entre workflows

---

> ⬅️ [MCP Server](./16_mcp_server.md) | ⬅️ [Índice](./00_indice.md)
