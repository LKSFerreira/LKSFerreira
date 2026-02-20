# 🚀 Vibe Coding Workspace & Agent Workflows

Bem-vindo ao seu ambiente padronizado de **Vibe Coding**. Este repositório funciona como uma **"Caixa de Ferramentas" (Toolbox)** gerenciada por Agentes IA. Ele contém templates dinâmicos, pipelines de DevContainers otimizados e regras de comportamento para organizar o caos, documentar e acelerar a entrega de qualquer projeto.

Este guia explica o ecossistema de fluxos (`Workflows`) para iniciar um projeto do zero ou como reconectar de forma segura a um projeto em andamento.

---

## 🛠️ O Que é Este Repositório?
Este repositório fornece a base arquitetural para suas ideias. Suas pastas ocultas contêm o núcleo do sistema:
- **`.agent/workflows/`**: Comandos Slash (ex: `/init`) que definem passos lógicos estritos para o Agente executar.
- **`.agent/templates/`**: Blueprints e arquivos de referência "Ouro" para infraestrutura (Docker, Devcontainers).
- **`.agent/rules/`**: Diretrizes de estilo, linguagem e comportamento para forçar a IA a manter o padrão do projeto.

---

## 🧭 O Fluxo de Trabalho (Workflows)

Abaixo descrevemos o ciclo de vida completo do uso dos comandos e em qual ordem eles devem ser acionados pelo chat:

### 🌟 1. Inicializando um NOVO Projeto
Quando você clonar ou esvaziar a raiz para começar uma nova ideia:

1. **`/init`** (Gerador de Contexto Inicial)
   - **O que faz:** Analisa os arquivos (ex: `package.json`, `pyproject.toml`) para detectar a stack predominante. Gera automaticamente as documentações vitais (`.metadocs/roadmap.md`, regras `.agent/rules/<linguagem>.md` e o `README.md` do projeto próprio) e assina a tag de linguagem do agente.
   - **Quando usar:** No primeiríssimo prompt do projeto, logo após inserir os arquivos base ou gerar o boilerplate inicial.

2. **`/setup_devcontainers`** (Bootstrapping de Infraestrutura)
   - **O que faz:** Pega as arquiteturas dos templates "Ouro" e constrói a pasta `.devcontainer/` real na raiz do seu projeto. Cria os arquivos locais `.env` e o utilitário `dev.sh` (Injetando IP dinâmico para hot-reload confiável em qualquer SO).
   - **Quando usar:** Logo em seguida ao `/init`, para ter seu ambiente Docker e Banco de Dados rodando em questão de segundos.

---

### 🔄 2. Retornando a um Projeto Existente (Novo Chat)
Devido ao limite de contexto, frequentemente você abrirá novas janelas de chat para continuar um projeto grandioso. Evite o caos através da reconexão padronizada:

1. **`/novo_chat`** (Sincronização de Contexto e Auditoria)
   - **O que faz:** Força o Agente a ler silenciosamente o `.metadocs/roadmap.md`, regras do repositório e os manifestos para entender onde ele parou da última vez. Ele fará uma auditoria e comparará o código atual com o que diz o roadmap.
   - **Quando usar:** **SEMPRE** que você abrir uma nova janela de chat da IA. Nunca inicie o dia de código antes de usar este comando para alinhar o cérebro do Agente.

---

### 💻 3. Desenvolvimento Diário e Versionamento

Enquanto você trabalha ("vibe coding"), use os ajudantes de versionamento restrito e atômico:

1. **`/commits`** (Gerador de Commits Padronizados)
   - **O que faz:** Avalia o seu local `git diff`, analisa as mudanças não consolidadas e formata as mensagens estritas baseadas em emojis (ex: `:sparkles: feat`, `:bug: fix`, `:recycle: refactor`). Garante commits atômicos de forma autônoma.
   - **Quando usar:** Sempre que a alteração atual fechar um ciclo lógico de funcionamento no código, antes de seguir para a próxima tarefa.

2. **`/pull_requests`** (Formatador de Entregas e Revisão)
   - **O que faz:** Lê o seu `git diff` comparado com a branch principal, cruza isso com o andamento do `.metadocs/roadmap.md`, e gera um texto formatado, descritivo e pronto de Pull Request para você abrir no Github ou similar, blindando links quebrados.
   - **Quando usar:** Quando uma fase/etapa inteira do Roadmap for concluída e estiver pronta para revisão e merge.

---

## 💡 Melhores Práticas de Vibe Coding

- **Use e Abuse do Roadmap**: A IA perde contexto facilmente em projetos de semanas de duração. O segredo da consistência é sempre manter as "tasks" estritamente refletidas em `.metadocs/roadmap.md`.
- **Arquitetura Multi-stage**: Seus contêineres usam a estratégia de Ouro desenhadas na subpasta `.devcontainer/`. Modifique suas dependências via arquivo de pacotes nativos da linguagem e no *rebuild* o cache do Docker persistirá as atualizações instantaneamente.

> Desenvolva rápido e deixe fluir na 'vibe', mas deixe o Agente manter a estrutura viva e formal para você.
