---
description: Workflow para versionamento de código
---

Execute as etapas abaixo para garantir um versionamento atômico e organizado:

## Fluxo de Execução:

1. **Descoberta**: Analise o estado atual com `git status` e examine as alterações com `git diff --staged`.
2. **Seleção**: Realize o stage seletivo (se necessário) seguindo rigorosamente as políticas em `.agents/rules/git.md`.
3. **Escrita**: Gere a mensagem de commit usando obrigatoriamente o **Template obrigatório de commit**.
4. **Execução**: Execute um único comando com o `git add & git commit -m`.
5. **Iteração**: Repita o processo até que todas as alterações pendentes tenham sido processadas em commits atômicos ou de agrupamento.

[!IMPORTANT]

> Por padrão, todos os arquivos devem ser commitados, a menos que haja uma instrução explícita do usuário.

---

## Relatório de Entrega:

> Disponibilizar o Walkthrough
