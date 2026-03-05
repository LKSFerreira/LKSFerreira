# 🚀 Vibe Coding Workspace & Template de Estudos

Bem-vindo ao seu **Ambiente de Estudos e Laboratório Prático**. Este repositório funciona como uma **"Caixa de Ferramentas" (Toolbox) Educacional** gerenciada por Agentes IA que atuarão como seus mentores e tutores. Ele contém templates dinâmicos, pipelines de ambientes Docker otimizados e regras de comportamento para organizar, documentar e acelerar o aprendizado aplicado em qualquer projeto.

Este guia explica o ecossistema de fluxos (`Workflows`) para iniciar um projeto educacional do zero ou como reconectar de forma segura e guiada aos seus estudos em andamento.

---

## 🛠️ O Que é Este Repositório?

Este repositório fornece a base arquitetural para suas ideias e estudos. Suas pastas ocultas contêm o núcleo do sistema didático:

- **`.agents/workflows/`**: Comandos Slash (ex: `/init`) que definem passos lógicos estritos para o Agente executar como tutor.
- **`.agents/templates/`**: Blueprints e arquivos de referência "Ouro" para entender a infraestrutura (Docker, ambientes de container) e reutilizar padrões com menos atrito.
- **`.agents/rules/`**: Diretrizes de estilo, linguagem e comportamento para forçar a IA a manter o padrão do projeto e priorizar explicações detalhadas voltadas ao aprendizado.

---

## 🧭 O Fluxo de Trabalho (Workflows)

Abaixo descrevemos o ciclo de vida completo do uso dos comandos e em qual ordem eles devem ser acionados pelo chat:

### 🌟 1. Inicializando um NOVO Experimento/Laboratório

Quando você clonar ou esvaziar a raiz para começar uma nova ideia de estudo:

1. **`/init`** (Gerador de Contexto Inicial)
   - **O que faz:** Analisa os arquivos para detectar a stack predominante. Gera automaticamente as documentações vitais (`.metadocs/roadmap.md`, regras `.agents/rules/<linguagem>.md` e o `README.md` do repositório) e assina a tag de linguagem do agente mentor. O resultado mantém foco didático e coerência estrutural.
   - **Quando usar:** No primeiríssimo prompt do experimento, logo após inserir os arquivos base ou gerar o boilerplate inicial.

2. **`/setup_docker`** (Bootstrapping de Infraestrutura)
   - **O que faz:** Pega as arquiteturas dos templates "Ouro" e constrói a pasta `.docker/` real na raiz do seu projeto. Cria os arquivos locais `.env` e o utilitário `dev.sh` (Injetando IP dinâmico para hot-reload confiável em qualquer SO).
   - **Quando usar:** Logo em seguida ao `/init`, para ter seu ambiente Docker e Banco de Dados rodando em questão de segundos.

---

### 🔄 2. Retornando aos Seus Estudos (Novo Chat)

Devido ao limite de contexto, frequentemente você abrirá novas janelas de chat para continuar um laboratório em dias diferentes. Evite o caos com uma reconexão padronizada:

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
- **Arquitetura Multi-stage e Comentários**: Seus contêineres usam a estratégia de Ouro desenhada na subpasta `.docker/`. Modifique suas dependências via arquivo de pacotes nativos da linguagem e, no _rebuild_, o cache do Docker ajudará a manter as atualizações rápidas sem sacrificar entendimento.

> Desenvolva rápido e deixe fluir na 'vibe', mas deixe o Agente manter a estrutura viva e formal para você. Conte sempre com o seu IA focado em didática, clareza e prática deliberada. Bons estudos!


