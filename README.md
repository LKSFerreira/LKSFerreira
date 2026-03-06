# 🚀 Vibe Coding Workspace & Infraestrutura de Projetos

Bem-vindo ao seu **Template Base para Projetos**. Este repositório funciona como uma **"Caixa de Ferramentas" (Toolbox)** gerenciada por Agentes IA que atuarão como seus parceiros de desenvolvimento. Ele contém templates dinâmicos, pipelines de ambientes Docker otimizados e regras de comportamento para organizar, documentar e acelerar a entrega de qualquer projeto profissional.

Este guia explica o ecossistema de fluxos (`Workflows`) para iniciar um projeto de engenharia de software do zero ou como padronizar repositórios em andamento.

---

## 🛠️ O Que é Este Repositório?

Este repositório fornece a base arquitetural para novos projetos e padronizações. Suas pastas ocultas contêm o núcleo operacional do template:

- **`.agents/workflows/`**: Comandos Slash (ex: `/init`) que definem passos lógicos estritos para o Agente executar.
- **`.agents/templates/`**: Blueprints e arquivos de referência "Ouro" para infraestrutura, Docker e ambientes de desenvolvimento.
- **`.agents/rules/`**: Diretrizes de estilo, linguagem e comportamento para manter consistência arquitetural e qualidade de entrega.

---

## 🧭 O Fluxo de Trabalho (Workflows)

Abaixo descrevemos o ciclo de vida completo do uso dos comandos e em qual ordem eles devem ser acionados pelo chat:

### 🌟 1. Inicializando um NOVO Projeto

Quando você clonar ou esvaziar a raiz para começar uma nova ideia:

1. **`/init`** (Gerador de Contexto Inicial)
   - **O que faz:** Analisa os arquivos para detectar a stack predominante. Gera automaticamente as documentações vitais (`.metadocs/roadmap.md`, regras `.agents/rules/<linguagem>.md` e o `README.md` do repositório) e assina a tag de linguagem do agente responsável pelo projeto.
   - **Quando usar:** No primeiro prompt do projeto, logo após inserir os arquivos base ou gerar o boilerplate inicial.

2. **`/setup_docker`** (Bootstrapping de Infraestrutura)
   - **O que faz:** Pega as arquiteturas dos templates "Ouro" e constrói a pasta `.docker/` real na raiz do seu projeto. Cria os arquivos locais `.env` e o utilitário `dev.sh` (Injetando IP dinâmico para hot-reload confiável em qualquer SO).
   - **Quando usar:** Logo em seguida ao `/init`, para ter seu ambiente Docker e Banco de Dados rodando em questão de segundos.

---

### 🔄 2. Retornando ao Seu Projeto (Novo Chat)

Devido ao limite de contexto, frequentemente você abrirá novas janelas de chat para continuar um projeto em dias diferentes. Evite o caos com uma reconexão padronizada:

1. **`/novo_chat`** (Sincronização de Contexto e Auditoria)
   - **O que faz:** Força o Agente a ler silenciosamente o `.metadocs/roadmap.md`, regras do repositório e os manifestos para entender onde o trabalho parou. Ele fará uma auditoria e comparará o código atual com o que diz o roadmap.
   - **Quando usar:** **SEMPRE** que você abrir uma nova janela de chat da IA. Nunca retome o trabalho antes de usar este comando para realinhar o contexto.

---

### 💻 3. Desenvolvimento Diário e Entrega Contínua

Enquanto você trabalha ("vibe coding"), use os ajudantes de versionamento restrito e atômico:

1. **`/commits`** (Gerador de Commits Padronizados)
   - **O que faz:** Avalia o seu `git diff`, analisa as mudanças e formata mensagens baseadas em emojis (ex: `:sparkles: feat`, `:bug: fix`, `:recycle: refactor`), reforçando atomicidade e rastreabilidade.
   - **Quando usar:** Sempre que a alteração atual fechar um ciclo lógico de funcionamento no código.

2. **`/pull_requests`** (Formatador de Entregas e Revisão)
   - **O que faz:** Lê o seu `git diff` comparado com a branch principal, cruza isso com o andamento do `.metadocs/roadmap.md` e gera um texto formatado, descritivo e pronto de Pull Request para você abrir no GitHub ou similar.
   - **Quando usar:** Quando uma fase inteira do roadmap for concluída e estiver pronta para revisão e merge.

---

## 💡 Melhores Práticas de Vibe Coding

- **Use e Abuse do Roadmap**: A IA perde contexto facilmente em projetos extensos. O segredo da consistência é sempre manter um passo a passo perfeitamente refletido no `.metadocs/roadmap.md`.
- **Arquitetura Multi-stage e Documentação Formal**: Seus contêineres usam a estratégia de Ouro desenhada na subpasta `.docker/`. Modifique suas dependências via arquivo de pacotes nativos da linguagem e, no _rebuild_, o cache do Docker ajudará a manter as atualizações rápidas. Documentação de classes, métodos e contratos públicos deve continuar explícita e útil para manutenção.

> Desenvolva rápido e deixe fluir na 'vibe', mas deixe o Agente manter a estrutura viva e formal para você. Conte sempre com o seu IA focado em engenharia de software, rastreabilidade e qualidade de entrega.
