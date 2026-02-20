---
description: Gerador de Pull Request com Rigor de Sintaxe e Caminhos Relativos
---

Atue como um Tutor Revisor Rigoroso. Sua tarefa é gerar o corpo de um Pull Request baseado nos laboratórios e experimentos realizados no branch atual (diff), ressaltando o aprendizado consolidado.

## 🚨 REGRAS CRÍTICAS DE FORMATAÇÃO (SINTAXE)

1. **PROIBIÇÃO ABSOLUTA**: Nunca use os protocolos `cci:`, `file:///` ou caminhos absolutos (ex: `C:/Users/...`).
2. **PROIBIÇÃO DE LINKS DUPLOS**: Não use a sintaxe `[[arquivo](link)]`.
3. **OBRIGATORIEDADE DE LINKS RELATIVOS**: Ao citar qualquer arquivo, use exclusivamente o formato Markdown padrão relativo: `[caminho/do/arquivo.ext](caminho/do/arquivo.ext)`.
4. **EMOJIS**: Mantenha os emojis e os códigos de tipo (ex: `:sparkles: feat`) conforme definido no padrão de commits do projeto.

---

## 📋 ESTRUTURA DO PULL REQUEST

Gere a saída seguindo este template estrito, extraindo as informações do `git diff` e do `.metadocs/roadmap.md`:

# ✨ [TIPO] Nome da Feature: Título Descritivo

## 🎯 Visão Geral de Aprendizado
Consolidação do Estudo da [Etapa] do Roadmap. Foco em compreender **[Conceito Principal]** através de **[Técnica/Ferramenta]**. 
*O que foi aprendido/resolvido:* [Descreva o insight ou erro compreendido e evitado].

## 🛠️ Alterações Realizadas

### 🧩 [Categoria 1: ex: Backend/Logic]
- [Mudança 1] em [arquivo](caminho/relativo).
- [Mudança 2] em [arquivo](caminho/relativo).

### 🛡️ [Categoria 2: ex: Segurança/Refatoração]
- [Ajuste de fluxo] para garantir [comportamento].
- Correção de [item específico].

## 🏛️ Melhorias de Arquitetura
- [Novos componentes/abstrações] para melhor [Encapsulamento/Performance].

## 📈 Resultados e Insights Técnicos
- **Validação:** O comando `[comando]` testado retorna `[resultado]`.
- **Conhecimento Adquirido:** [O que isso provou ou ensinou na prática].

## 🧪 Como Validar?
1. **Ambiente:** [Comando de ativação/setup]
2. **Execução:** [Comando de teste/validação]
3. **Testes:** [Comando de testes unitários]

---

> **Nota Didática:** Este PR de estudo encerra formalmente a [Fase Atual de Aprendizado], preparando a base conceitual para [Próximo Tópico do Roadmap].

---

## INSTRUÇÃO DE EXECUÇÃO
1. Analise o `git diff` das alterações não commitadas ou do branch atual vs `main`.
2. Verifique o `.metadocs/roadmap.md` para identificar a Fase/Etapa.
3. Gere o texto final pronto para cópia, aplicando rigorosamente a regra de links relativos.