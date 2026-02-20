# 🚀 Laboratório de Estudos & Agent Workflows

Bem-vindo ao seu **Ambiente de Estudos e Laboratório Prático**. Este repositório funciona como uma **"Caixa de Ferramentas" (Toolbox) Educacional** gerenciada por Agentes IA que atuarão como seus mentores e tutores. Ele contém templates didáticos, pipelines otimizados e regras focadas no aprendizado passo a passo.

Este guia explica o ecossistema de fluxos (`Workflows`) para iniciar um experimento do zero ou reconectar de forma guiada aos seus estudos em andamento.

---

## 🛠️ O Que é Este Repositório?
Este repositório fornece a base arquitetural para suas ideias e estudos. Suas pastas ocultas contêm o núcleo do sistema didático:
- **`.agent/workflows/`**: Comandos Slash (ex: `/init`) que definem passos lógicos estruturados para o Agente executar como tutor.
- **`.agent/templates/`**: Blueprints e arquivos de referência "Ouro" repletos de comentários explicativos para entender a infraestrutura (Docker, Devcontainers).
- **`.agent/rules/`**: Diretrizes de estilo, linguagem e comportamento para forçar a IA a priorizar explicações detalhadas e código limpo para aprendizado.

---

## 🧭 O Fluxo de Trabalho (Workflows)

Abaixo descrevemos o ciclo de vida completo do uso dos comandos e em qual ordem eles devem ser acionados pelo chat:

### 🌟 1. Inicializando um NOVO Experimento/Laboratório
Quando você clonar ou esvaziar a raiz para começar uma nova ideia de estudo:

1. **`/init`** (Gerador de Contexto Inicial)
   - **O que faz:** Analisa os arquivos para detectar a stack predominante. Gera automaticamente as documentações vitais (`.metadocs/roadmap.md`, regras `.agent/rules/<linguagem>.md` e o `README.md` do repositório) e assina a tag de linguagem do agente mentor. O código gerado terá foco didático.
   - **Quando usar:** No primeiríssimo prompt do experimento, logo após inserir os arquivos base ou gerar o boilerplate inicial.

2. **`/setup_devcontainers`** (Bootstrapping de Infraestrutura)
   - **O que faz:** Pega as arquiteturas dos templates "Ouro" e constrói a pasta `.devcontainer/` real na raiz do seu projeto. Cria os arquivos locais `.env` e o utilitário `dev.sh` (Injetando IP dinâmico para hot-reload confiável em qualquer SO).
   - **Quando usar:** Logo em seguida ao `/init`, para ter seu ambiente Docker e Banco de Dados rodando em questão de segundos.

---

### 🔄 2. Retornando aos Seus Estudos (Novo Chat)
Devido ao limite de contexto, frequentemente você abrirá novas janelas de chat para continuar um laboratório em dias diferentes. Evite o caos através da reconexão padronizada:

1. **`/novo_chat`** (Sincronização de Contexto e Auditoria)
   - **O que faz:** Força o Agente a ler silenciosamente o `.metadocs/roadmap.md`, regras do repositório e os manifestos para entender onde ele parou da última vez. Ele fará uma auditoria e comparará o código atual com o que diz o roadmap.
   - **Quando usar:** **SEMPRE** que você abrir uma nova janela de chat da IA. Nunca inicie o dia de código antes de usar este comando para alinhar o cérebro do Agente.

---

### 💻 3. Desenvolvimento Diário e Aprendizado Ativo

Enquanto você trabalha ("vibe coding"), use os ajudantes de versionamento restrito e atômico:

1. **`/commits`** (Gerador de Commits Padronizados)
   - **O que faz:** Avalia o seu local `git diff`, analisa as mudanças e formata as mensagens baseadas em emojis (ex: `:sparkles: feat`, `:bug: fix`, `:recycle: refactor`), te ajudando a fixar boas práticas e atomicidade de registro.
   - **Quando usar:** Sempre que a alteração atual fechar um ciclo lógico de funcionamento no código, para acompanhar seu ritmo de aprendizagem passo a passo.

2. **`/pull_requests`** (Formatador de Entregas e Revisão)
   - **O que faz:** Lê o seu `git diff` comparado com a branch principal, cruza isso com o andamento do `.metadocs/roadmap.md`, e gera um texto formatado, descritivo e pronto de Pull Request para você abrir no Github ou similar, blindando links quebrados.
   - **Quando usar:** Quando uma fase/etapa inteira do Roadmap for concluída e estiver pronta para revisão e merge.

---

## 💡 Melhores Práticas de Vibe Coding

- **Use e Abuse do Roadmap**: A IA perde contexto facilmente em laboratórios extensos. O segredo da consistência é sempre manter um passo a passo do estudo perfeitamente refletido no `.metadocs/roadmap.md`.
- **Arquitetura Multi-stage e Comentários**: Seus contêineres usam a estratégia de Ouro desenhadas na subpasta `.devcontainer/`, repletas de comentários explicativos que ensinam por que cada linha está ali. Leia-os!

> Siga o passo a passo, explore a fundo o código e conte sempre com o seu IA focado em didática para te manter nos eixos. Bons estudos!
