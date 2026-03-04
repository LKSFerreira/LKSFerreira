---
description: Workflow para versionamento de código
---

Execute as etapas abaixo para garantir um versionamento atômico e organizado:

## Fluxo de Execução:

1. **Descoberta**: Analise o estado atual com `git status` e examine as alterações com `git diff --staged`.
2. **Seleção**: Realize o stage seletivo (se necessário) seguindo rigorosamente as políticas em `.agents/rules/git.md`.
3. **Escrita**: Gere a mensagem de commit usando obrigatoriamente o **Template obrigatório de commit**.
4. **Execução**: Execute um único comando com o `git add & git commit -m`.
4. **Iteração**: Repita o processo até que todas as alterações pendentes tenham sido processadas em commits atômicos ou de agrupamento.

[!IMPORTANT]
> Por padrão, todos os arquivos devem ser commitados, a menos que haja uma instrução explícita do usuário.

---

## Relatório de Entrega:
> \ de escapa não deve ser usada para as mensagem do relátorio.
> Use o caminho absoluto de cada arquivo para exibir no relatório.

Ao finalizar, você deve apresentar um resumo. Utilize o modelo abaixo:

### Versionamento Concluído

Foram realizados os seguintes commits:

- `Mensagem resumida`
[.raiz_do_projeto/caminho/do/arquivo1.eg](.[caminho_absoluto]/arquivo1.eg)
[.raiz_do_projeto/caminho/do/arquivo2.eg](.[caminho_absoluto]]/arquivo2.eg)

---

- `Outra mensagem que foi resumida`
[.raiz_do_projeto/caminho/do/arquivo3.eg](.[pwd]/caminho/do/arquivo3.eg]

---

***

## Exemplo real:

### Versionamento Concluído

Foram realizados os seguintes commits:

- `Corrigido mal comportamento do agente durante commits`
[.agents/rules/git.md](c:/GitHub/projeto/.agents/rules/git.md)
[.agents/rules/git.md](c:/Documents/GitHub/projeto/.agents/workflows/commit.md)

---

- `Adicionado termo test*.md no arquivo .gitignore`
[.gitignore](c:/Documents/GitHub/projeto/.gitignored)

---
