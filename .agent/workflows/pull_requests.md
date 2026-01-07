---
description: Modelo para criação consistente das pull requests
---

🚨 REGRAS CRÍTICAS DE FORMATAÇÃO DE ARQUIVOS 🚨

1.  **PROIBIDO**: Nunca use o protocolo `cci:`, `file:///` ou caminhos absolutos do Windows (ex: `c:/Users/...`).
2.  **PROIBIDO**: Não tente criar "smart links" ou links duplos (ex: `[[arquivo](link)]`).
3.  **OBRIGATÓRIO**: Ao citar arquivos, use EXATAMENTE e APENAS o formato Markdown padrão relativo.
    - Correto: `[app/controllers/api_controller.py](app/controllers/api_controller.py)`
    - Correto: `[tests/test_main.py](tests/test_main.py)`
    - Incorreto: `[[app/main.py](cci:7://...)]`

Resumo:
Coloque dentro de um bloco markdown, use apenas referências relativas com [ ]()

> Nenhum link ou referência deve ter algo como (cci:7://file:///c:/)

Sempre que eu solicitar a criação de um Pull Request (PR), você deve ignorar formatos padrão e seguir estritamente a estrutura abaixo. Mantenha os emojis, as seções em negrito e o bloco de nota final. Seja técnico e conciso.

```markdown
✨ [TIPO_DA_MUDANÇA] Nome da Feature/Etapa: Título Descritivo

🎯 Visão Geral

Este Pull Request consolida a [Etapa/Feature] do Roadmap, focando em [Objetivo Principal] através da [Técnica/Ferramenta Utilizada]. O objetivo foi [Benefício Claro/Problema Resolvido] (como [Exemplo de erro evitado ou melhoria]).

🛠️ Alterações Realizadas

🧩 [Categoria de Mudança 1 - ex: Tipagem/Backend]

- Implementação de [Detalhe técnico 1] em [Módulos afetados].
- Adição de [Detalhe técnico 2].
- [Detalhe técnico 3].

🛡️ [Categoria de Mudança 2 - ex: Segurança/Tratamento de Erros]

- Refatoração de [Fluxo lógico] para garantir [Comportamento esperado].
- Correção de [Item específico].

🏛️ Melhorias de Arquitetura

- Criação de [Novos componentes/propriedades] para melhor [Encapsulamento/Performance/Manutenibilidade].

📈 Resultados Técnicos

- [Métrica ou Validação]: O comando [Comando executado] agora retorna [Resultado esperado].
- [Benefício Direto]: [Melhoria observada no desenvolvimento ou produção].

🧪 Como Validar?

1. Ative o ambiente virtual: [Comando de ativação]
2. Execute a validação: [Comando de teste/validação]
3. Execute os testes unitários: [Comando de teste]

---

> Nota:
> Este PR encerra formalmente a [Fase/Etapa Atual], preparando o terreno para [Próxima Etapa].
```
