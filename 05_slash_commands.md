# 05 — Slash Commands da Extensão Codex

> 🔗 Fonte oficial: [developers.openai.com/codex/ide/slash-commands](https://developers.openai.com/codex/ide/slash-commands)
> ⬅️ [Comandos](./04_comandos_ide.md) | ➡️ [Configuração Básica](./06_config_basica.md)

---

## 📄 Documentação Oficial

### Como usar

1. No campo de chat do Codex, digite `/`
2. Selecione um comando da lista, ou continue digitando para filtrar
3. Pressione `Enter`

### Comandos Disponíveis

| Comando | O que faz |
|---------|-----------|
| `/auto-context` | Infere automaticamente o melhor contexto baseado no que você está editando |
| `/cloud` | Ativa o modo de execução na nuvem |
| `/cloud-environment` | Gerencia ou abre o ambiente cloud das tarefas |
| `/feedback` | Envia feedback para a equipe da OpenAI |
| `/local` | Transfere a execução de volta da nuvem para a máquina local |
| `/review` | Pede ao Codex para focar em **revisão de código** — aponta bugs, brechas e ineficiências |
| `/status` | Verifica a saúde do Codex (rede, cota, autenticação, ferramentas ativas) |

---

## 🎯 Exemplos Práticos

### `/review` — Revisão de código em um arquivo

```
/review

[Selecione o código ou referencie com @arquivo]
```

O Codex analisa o código buscando:
- Bugs potenciais
- Erros lógicos
- Edge cases não tratados
- Problemas de segurança

### `/status` — Diagnóstico rápido

```
/status
```

Resposta típica mostra:
- ✅ Autenticado
- ✅ Modelo ativo: gpt-5.2-codex
- ✅ Web search: cached
- ⚠️ Rate limit: 80% usado

### `/cloud` → `/local` — Fluxo cloud

```
/cloud
"Refatore todos os testes para usar Vitest ao invés de Jest"

[Aguarde o resultado na nuvem]

/local
"Aplique as mudanças localmente e rode os testes"
```

---

## 📖 Explicação Didática

### Diferença entre `/review` e simplesmente pedir "revise meu código"

O `/review` é um **modo especializado**. Quando você usa `/review`, o Codex:
1. Entra em modo focado de revisão (não propõe implementações)
2. Pode usar um modelo diferente otimizado para revisão (configurável via `review_model` no `config.toml`)
3. Estrutura a saída como um code review profissional

Já quando você pede "revise meu código" no chat normal, o Codex trata como uma conversa genérica.

### `/auto-context` — quando é útil?

Quando você abre o Codex e não sabe exatamente quais arquivos referenciar. O `/auto-context` analisa:
- O arquivo ativo
- Arquivos recentemente editados
- Dependências importadas

E monta automaticamente o contexto mais relevante para seu próximo prompt.

---

> ⬅️ [Comandos](./04_comandos_ide.md) | ➡️ [Configuração Básica](./06_config_basica.md)
