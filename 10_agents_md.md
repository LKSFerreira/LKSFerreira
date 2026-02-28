# 10 — Instruções Personalizadas com AGENTS.md

> 🔗 Fonte oficial: [developers.openai.com/codex/guides/agents-md](https://developers.openai.com/codex/guides/agents-md)
> ⬅️ [Regras](./09_regras.md) | ➡️ [MCP](./11_mcp.md)

---

## 📄 Documentação Oficial

### O que é AGENTS.md?

É um arquivo Markdown que fornece **instruções customizadas** ao Codex. Funciona como um "manual do funcionário" — toda vez que o Codex inicia, ele lê esse arquivo para saber como se comportar no seu projeto.

### Como o Codex descobre as instruções

Ordem de descoberta (alta para baixa prioridade):

1. **Global**: `~/.codex/AGENTS.override.md` → se não existir, `~/.codex/AGENTS.md`
2. **Projeto**: Da raiz do Git até o diretório atual, procura `AGENTS.override.md` → `AGENTS.md` → fallbacks definidos em `project_doc_fallback_filenames`
3. **Merge**: Concatena todos os arquivos encontrados (raiz para baixo). Arquivos mais próximos do diretório atual prevalecem.

### Criar instruções globais

```bash
mkdir -p ~/.codex
```

```markdown
# ~/.codex/AGENTS.md

## Acordos de trabalho
- Sempre rode `npm test` após modificar arquivos JavaScript.
- Prefira `pnpm` ao instalar dependências.
- Peça confirmação antes de adicionar dependências de produção.
```

Testar: `codex --ask-for-approval never "Resuma as instruções atuais."`

### Instruções por projeto

Na raiz do repositório:
```markdown
# AGENTS.md

## Expectativas do Repositório
- Rode `npm run lint` antes de abrir um pull request.
- Documente utilitários públicos em `docs/` quando alterar comportamento.
```

### Overrides por subdiretório

Em `services/payments/AGENTS.override.md`:
```markdown
## Regras do serviço de pagamentos
- Use `make test-payments` ao invés de `npm test`.
- Nunca rotacione API keys sem notificar o canal de segurança.
```

### Nomes de fallback customizados

Se seu projeto usa outro nome (ex: `TEAM_GUIDE.md`):
```toml
# ~/.codex/config.toml
project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
project_doc_max_bytes = 65536
```

---

## 🎯 Exemplos Práticos

### AGENTS.md para projeto React + TypeScript

```markdown
# AGENTS.md

## Stack
- React 18, TypeScript 5, Vite
- Zustand para estado global
- Vitest + Testing Library para testes

## Convenções
- Componentes: PascalCase, um por arquivo
- Hooks customizados: prefixo `use` + camelCase
- Estilos: CSS Modules (`.module.css`)
- Imports: absolutos via alias `@/`

## Ao modificar código
1. Rode `pnpm lint` e corrija erros
2. Rode `pnpm test` e garanta que passa
3. Não adicione dependências sem justificativa
```

### AGENTS.md para API Node.js

```markdown
# AGENTS.md

## Stack
- Node.js 20, Express, PostgreSQL
- Prisma ORM, Zod para validação

## Regras
- Toda rota nova precisa de teste de integração
- Use `async/await`, nunca callbacks
- Erros devem usar a classe `AppError`
- Logs via `winston`, nunca `console.log`
```

---

## 📖 Explicação Didática

### Analogia: AGENTS.md é como onboarding para um novo membro do time

Imagine que você contratou um programador que nunca viu seu projeto. O `AGENTS.md` é o documento que você entregaria no primeiro dia:
- "Usamos pnpm, não npm"
- "Os testes rodam com Vitest"
- "Nunca comite diretamente na main"

### AGENTS.md vs. AGENTS.override.md

- **AGENTS.md**: Instruções padrão que toda a equipe compartilha
- **AGENTS.override.md**: Sobreposição temporária ou situacional. Quando existe, substitui o `AGENTS.md` do mesmo diretório

> **Dica**: Use `.override.md` quando precisar mudar o comportamento temporariamente sem alterar o arquivo compartilhado.

### Limite de tamanho

O Codex lê no máximo **32 KB** (padrão) de instruções combinadas. Se seus arquivos ultrapassarem esse limite, as instruções serão truncadas. Aumente com `project_doc_max_bytes` no `config.toml`.

---

> ⬅️ [Regras](./09_regras.md) | ➡️ [MCP](./11_mcp.md)
