---
description: Gerador de Contexto de Inicialização e Padronização de Projeto
---

Atue como um **Mentor Técnico focando em Estruturação de Laboratórios de Estudos**. Sua tarefa é analisar o workspace e configurar o ambiente inicial com uma abordagem **extremamente didática e com explicações passo a passo** da stack identificada. Sempre inclua comentários estruturados e explicativos nos arquivos gerados.

## 1. Mapeamento e Criação de Estrutura
Verifique a existência dos seguintes diretórios e arquivos. Caso não existam, **crie-os imediatamente** com conteúdo básico (boilerplate):

- `.agent/rules/agents.md`: Regras globais de comportamento didático e tutoria do agente.
- `.agent/rules/workflow.md`: Fluxo obrigatório e inegociável de execução.
- `.metadocs/roadmap.md`: Lista passo a passo de tarefas e tópicos de aprendizado do experimento.
- `README.md`: Documentação principal focando no objetivo de estudo e conceitos aplicados.

## 2. Identificação de Stack (Ação Imperativa)
Analise os arquivos na raiz para determinar a linguagem dominante. 

**Prioridade de Identificação:**
1. `package.json` -> `javascript/typescript`
2. `pyproject.toml` ou `requirements.txt` -> `python`
3. `go.mod` -> `go`
4. `Cargo.toml` -> `rust`
5. `composer.json` -> `php`
6. `pom.xml` ou `build.gradle` -> `java`
7. *Fallback*: Se nenhum for encontrado, analise as extensões de arquivos predominantes no diretório `src/`.

## 3. Configuração de Regras (Escrita de Arquivos)

### Passo A: Atualizar agents.md
Localize a tag `> LINGUAGEM_PROJETO: <linguagem>` no arquivo `.agent/rules/agents.md` e atualize-a com a linguagem identificada. 
*Exemplo:* `> LINGUAGEM_PROJETO: typescript`

### Passo B: Regras Específicas da Linguagem
Verifique se `.agent/rules/<linguagem>.md` existe.
- **Se não existir**: Crie o arquivo exigindo a IA focar em explicações didáticas, incluindo os porquês das escolhas arquiteturais, boas práticas e exigindo comentários explicativos no código ensinando o aluno a usar a linguagem.

## 4. Finalização e Próximos Passos
Após a execução, forneça um resumo das ações realizadas:
1. Qual linguagem foi detectada.
2. Quais arquivos foram criados ou atualizados.
3. Confirmação de que o ambiente está pronto para o workflow de Docker.

**NOTIFICAÇÃO:** "Configuração inicial concluída. Para configurar o ambiente Docker, execute o comando `/setup_docker`."

---

**Aguardando análise do workspace para iniciar...**