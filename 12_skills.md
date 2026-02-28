# 12 — Agent Skills

> 🔗 Fonte oficial: [developers.openai.com/codex/skills](https://developers.openai.com/codex/skills)
> ⬅️ [MCP](./11_mcp.md) | ➡️ [Multi-Agentes](./13_multi_agentes.md)

---

## 📄 Documentação Oficial

### O que são Skills?

Skills são **pacotes de instruções e scripts** que ensinam novas habilidades ao Codex. É como dar um manual especializado para uma tarefa específica.

### Como o Codex usa Skills

1. **Invocação explícita**: Use `/skills` ou `$nome-da-skill` no prompt
2. **Invocação implícita**: O Codex escolhe automaticamente uma skill quando seu prompt casa com a `description` da skill

### Criar uma Skill

#### Via criador built-in
```
$skill-creator
```
O assistente pergunta o que a skill faz, quando deve disparar e se precisa de scripts.

#### Manualmente

Crie uma pasta com um `SKILL.md`:

```markdown
---
name: minha-skill
description: Explique exatamente quando esta skill deve e não deve disparar.
---

Instruções que o Codex deve seguir quando esta skill estiver ativa.
```

### Onde salvar Skills

| Escopo | Localização |
|--------|------------|
| Repositório | `.agents/skills/` (do `$CWD` até a raiz do repo) |
| Usuário | `$HOME/.agents/skills/` |
| Admin | `/etc/codex/skills/` |
| Sistema | Definido pelo sistema |

### Instalar Skills

```
$skill-installer install the linear skill from the .experimental folder
```

O instalador também pode baixar skills de outros repositórios.

### Habilitar/Desabilitar Skills

```toml
# ~/.codex/config.toml
[[skills.config]]
path = "/caminho/para/skill/SKILL.md"
enabled = false
```

### Metadata opcional (openai.yaml)

```yaml
# agents/openai.yaml
interface:
  display_name: "Nome amigável"
  short_description: "Descrição curta"
  brand_color: "#3B82F6"
  default_prompt: "Prompt padrão para usar a skill"

policy:
  allow_implicit_invocation: false  # true = ativa automaticamente

dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
      description: "OpenAI Docs MCP server"
      transport: "streamable_http"
      url: "https://developers.openai.com/mcp"
```

---

## 🎯 Exemplos Práticos

### Skill: Gerar changelog automático

```markdown
---
name: gerar-changelog
description: >
  Ative quando o usuário pedir para gerar changelog, notas de release,
  ou resumo de mudanças entre versões.
---

## Passos
1. Execute `git log --oneline <tag-anterior>..HEAD`
2. Agrupe os commits por categoria (feat, fix, chore, docs)
3. Gere um CHANGELOG.md formatado com as seções: Added, Fixed, Changed, Removed
4. Use o formato Keep a Changelog (https://keepachangelog.com)
```

### Skill: Review de segurança

```markdown
---
name: review-seguranca
description: >
  Ative quando o usuário pedir revisão de segurança, análise de vulnerabilidades,
  ou hardening do código.
---

## Checklist de Segurança
1. Busque por: SQL injection, XSS, CSRF, secrets expostos
2. Verifique: validação de input, sanitização de output, headers HTTP
3. Analise: dependências com `npm audit` ou equivalente
4. Reporte: severidade (crítica/alta/média/baixa), local, correção sugerida
```

---

## 📖 Explicação Didática

### Skills vs. AGENTS.md — qual a diferença?

| Aspecto | AGENTS.md | Skills |
|---------|-----------|--------|
| Escopo | Projeto inteiro | Tarefa específica |
| Quando ativa | Sempre (ao iniciar o Codex) | Sob demanda (manual ou automático) |
| Complexidade | Texto simples | Pode incluir scripts e metadata |
| Compartilhamento | Por repositório | Por repositório, usuário ou global |

### Boas práticas

- **Uma skill = um trabalho**. Não crie skills "faz-tudo".
- **Prefira instruções a scripts**, a menos que precise de comportamento determinístico.
- **Escreva descriptions com limites claros**: diga quando deve E quando NÃO deve disparar.

---

> ⬅️ [MCP](./11_mcp.md) | ➡️ [Multi-Agentes](./13_multi_agentes.md)
