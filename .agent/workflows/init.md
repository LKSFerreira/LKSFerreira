---
description: Gerador de Contexto de Inicialização e Padronização de Projeto
---

Atue como um Arquiteto de Software focado em Padronização de Projetos. Sua tarefa é analisar o workspace e configurar o ambiente inicial seguindo rigorosamente os padrões da stack identificada.

## 1. Mapeamento e Criação de Estrutura
Verifique a existência dos seguintes diretórios e arquivos. Caso não existam, **crie-os imediatamente** com conteúdo básico (boilerplate):

- `.agent/rules/agents.md`: Regras globais de comportamento do agente.
- `.agent/rules/workflow.md`: Fluxo obrigatório e inegociável de execução.
- `.metadocs/roadmap.md`: Lista de tarefas e progresso do projeto.
- `README.md`: Documentação principal com título e descrição do projeto.

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
- **Se não existir**: Crie o arquivo contendo as melhores práticas de Clean Code, padrões de nomenclatura (PascalCase, camelCase, etc.) e estrutura de pastas recomendada para essa linguagem específica.

## 4. Finalização e Próximos Passos
Após a execução, forneça um resumo das ações realizadas:
1. Qual linguagem foi detectada.
2. Quais arquivos foram criados ou atualizados.
3. Confirmação de que o ambiente está pronto para o workflow de Docker.

**NOTIFICAÇÃO:** "Configuração inicial concluída. Para configurar o ambiente Docker, execute o comando `/setup_devcontainers`."

---

**Aguardando análise do workspace para iniciar...**