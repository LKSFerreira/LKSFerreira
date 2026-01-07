---
description: Gerador de Contexto de Inicialização
---

Atue como um Arquiteto de Software focado em Padronização de Projetos.
Sua tarefa é configurar o ambiente inicial do projeto.

## Estrutura de Diretórios Padrão

Assuma que o projeto segue esta estrutura:

- `.agent/rules/agents.md` (Regras do Agente)
- `.agent/rules/<linguagem>.md` (Regras específicas da linguagem)
- `.metadocs/roadmap.md` (Planejamento)
- `README.md` (Visão Geral)

> Caso os diretórios não existam, crie-os.

## AÇÃO OBRIGATÓRIA: Identificar e Configurar Linguagem

**VOCÊ DEVE EXECUTAR ESTAS AÇÕES NA ORDEM:**

### Passo 1: Identificar a linguagem dominante

Analise os arquivos de configuração na raiz:

| Arquivo                              | Linguagem  |
| ------------------------------------ | ---------- |
| `pyproject.toml`, `requirements.txt` | python     |
| `package.json`                       | javascript |
| `go.mod`                             | go         |
| `Cargo.toml`                         | rust       |
| `pom.xml`, `build.gradle`            | java       |
| `composer.json`                      | php        |

### Passo 2: Atualizar agents.md

**AÇÃO IMPERATIVA:** Abra o arquivo `.agent/rules/agents.md` e substitua:

```markdown
<!-- LINGUAGEM_PROJETO: <linguagem_programacao> -->
```

Por (exemplo para JavaScript):

```markdown
<!-- LINGUAGEM_PROJETO: javascript -->
```

> Use o valor identificado no Passo 1. Este passo é OBRIGATÓRIO e não opcional.

### Passo 3: Verificar regras da linguagem

Verifique se existe o arquivo `.agent/rules/<linguagem>.md`.

- Se existir: leia-o para conhecer as regras específicas.
- Se não existir: crie-o com as convenções padrão da linguagem.

## Resultado Esperado

Após executar este workflow, o projeto deve ter:

1. Campo `LINGUAGEM_PROJETO` preenchido em `agents.md`
2. Arquivo de regras específicas da linguagem

---

> **Próximo passo:** Para configurar o ambiente Docker, execute o workflow `/devcontainers`.

**AGUARDE:** Notifique o usuário sobre as configurações realizadas antes de prosseguir.
