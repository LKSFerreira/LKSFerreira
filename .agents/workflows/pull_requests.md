---
description: Workflow operacional para comando /pr
---

# Workflow `/pr`

Quando o usuário solicitar `/pr`, execute nesta ordem:

1. Carregue `.agents/rules/git.md`.
2. Analise o diff do branch atual em relação à base definida pelo usuário (ou `main` por padrão).
3. Gere o corpo de PR usando obrigatoriamente o **Template obrigatório de PR** da regra de git.
4. Não invente etapas: descreva apenas o que está no diff e no contexto real do projeto.

Formato de saída:
1. Título
2. Visão geral
3. Alterações realizadas
4. Como validar
5. Riscos e pendências
