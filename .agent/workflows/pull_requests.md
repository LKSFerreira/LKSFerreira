---
description: Gerador de Pull Request com Rigor de Sintaxe e Caminhos Relativos
---

Atue como um Tech Lead revisor. Sua tarefa é gerar o corpo de um Pull Request baseado nas alterações realizadas no branch atual (diff).

## 🚨 REGRAS CRÍTICAS DE FORMATAÇÃO (SINTAXE)

1. **PROIBIÇÃO ABSOLUTA**: Nunca use os protocolos `cci:`, `file:///` ou caminhos absolutos (ex: `C:/Users/...`).
2. **PROIBIÇÃO DE LINKS DUPLOS**: Não use a sintaxe `[[arquivo](link)]`.
3. **OBRIGATORIEDADE DE LINKS RELATIVOS**: Ao citar qualquer arquivo, use exclusivamente o formato Markdown padrão relativo: `[caminho/do/arquivo.ext](caminho/do/arquivo.ext)`.
4. **EMOJIS**: Mantenha os emojis e os códigos de tipo (ex: `:sparkles: feat`) conforme definido no padrão de commits do projeto.

---

## 📋 ESTRUTURA DO PULL REQUEST

Gere a saída seguindo este template estrito, extraindo as informações do `git diff` e do `.metadocs/roadmap.md`:

# ✨ [TIPO] Nome da Feature: Título Descritivo

## 🎯 Visão Geral
Consolidação da [Etapa] do Roadmap. Foco em **[Objetivo Principal]** através de **[Técnica/Ferramenta]**. 
*Problema resolvido:* [Descreva o benefício claro ou erro evitado].

## 🛠️ Alterações Realizadas

### 🧩 [Categoria 1: ex: Backend/Logic]
- [Mudança 1] em [arquivo](caminho/relativo).
- [Mudança 2] em [arquivo](caminho/relativo).

### 🛡️ [Categoria 2: ex: Segurança/Refatoração]
- [Ajuste de fluxo] para garantir [comportamento].
- Correção de [item específico].

## 🏛️ Melhorias de Arquitetura
- [Novos componentes/abstrações] para melhor [Encapsulamento/Performance].

## 📈 Resultados Técnicos
- **Validação:** O comando `[comando]` retorna `[resultado]`.
- **Benefício:** [Melhoria observada].

## 🧪 Como Validar?
1. **Ambiente:** [Comando de ativação/setup]
2. **Execução:** [Comando de teste/validação]
3. **Testes:** [Comando de testes unitários]

---

> **Nota:** Este PR encerra formalmente a [Fase Atual], preparando o terreno para [Próxima Etapa do Roadmap].

---

## INSTRUÇÃO DE EXECUÇÃO
1. Analise o `git diff` das alterações não commitadas ou do branch atual vs `main`.
2. Verifique o `.metadocs/roadmap.md` para identificar a Fase/Etapa.
3. Gere o texto final pronto para cópia, aplicando rigorosamente a regra de links relativos.