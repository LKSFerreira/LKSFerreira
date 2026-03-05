## Padrões de Código e Arquitetura

1. **Clean Code & Clean Architecture:**
   - Funções pequenas e com responsabilidade única (SRP).
   - Uso de *Guard Clauses* para evitar aninhamentos profundos.
   - O código deve ser focado em legibilidade e fácil manutenção.

2. **Idioma e Nomenclatura:**
   - Base do código em **Português (pt-BR)**.
   - Exceções para inglês: padrões da indústria (`models/`, `api/`, `utils`), ações consolidadas (`commit`, `push`, `get`, `set`) ou quando o termo não tiver tradução boa/ficar esquisito em português (ex: `endpoint`, `payload`).
   - **Sem abreviações:** Proibido usar variáveis de uma ou duas letras (`p`, `u`, `l`, `evt`, `req`).
   - Usar nomes expressivos e descritivos em tudo, incluindo parâmetros de lambdas e arrow functions (ex: `usuarios.map(usuario => ...)` e não `usuarios.map(u => ...)`).

3. **Modo Estudos (Didática Escrita):**
   - O layout da implementação deve priorizar a **didática sobre a concisão** (conforme `workflow.md`).
   - Comentários granulares explicando o *porquê* de escolhas técnicas.
   - Código limpo explica "o que" faz. O comentário explica "por que" foi feito daquela forma.

4. **Tratamento de Erros:**
   - Evitar falhas silenciosas (não engolir exceções).
   - Escrever mensagens de erro claras que ajudem no debug.

5. **Organização e Documentação:**
   - Não manter código comentado/morto no arquivo. Apague o que não for mais usado.
   - Documentação específica por linguagem (tipagem, docstrings, comandos) deve seguir as regras definidas em `/.agents/rules/<linguagem>.md`.
