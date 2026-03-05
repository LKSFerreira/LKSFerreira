## Padrões de Código e Arquitetura

1. **Clean Code & Clean Architecture:**
   - Funções pequenas e com responsabilidade única (SRP).
   - Uso de _Guard Clauses_ para evitar aninhamentos profundos.
   - O código deve ser focado em legibilidade e fácil manutenção.

2. **Idioma e Nomenclatura:**
   - Base do código em **Português (pt-BR)**.
   - Exceções para inglês: padrões da indústria (`models/`, `api/`, `utils`), ações consolidadas (`commit`, `push`, `get`, `set`) ou quando o termo não tiver tradução boa/ficar esquisito em português (ex: `endpoint`, `payload`).
   - **Sem abreviações:** Proibido usar variáveis de uma ou duas letras (`p`, `u`, `l`, `evt`, `req`).
   - Usar nomes expressivos e descritivos em tudo, incluindo parâmetros de lambdas e arrow functions (ex: `usuarios.map(usuario => ...)` e não `usuarios.map(u => ...)`).

3. **Foco em Produção e Manutenibilidade:**
   - O código final deve priorizar **performance, segurança e legibilidade** estrutural.
   - Comentários não devem ser didáticos (não explique "o que" o bloco faz, dê nomes expressivos aos métodos/variáveis).
   - Comentários devem existir apenas para justificar decisões de arquitetura complexas e _trade-offs_ de negócio ("por que" foi feito assim).
   - Manter o fluxo conciso, reduzindo blocos desnecessários sempre que o padrão Clean Code permitir.

4. **Tratamento de Erros:**
   - Evitar falhas silenciosas (não engolir exceções).
   - Escrever mensagens de erro claras que ajudem no debug.

5. **Organização e Documentação:**
   - Não manter código comentado/morto no arquivo. Apague o que não for mais usado.
   - Documentação específica por linguagem (tipagem, docstrings, comandos) deve seguir as regras definidas em `/.agents/rules/<linguagem>.md`.
