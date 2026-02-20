---
trigger: model_decision
description: Convenções JS/TS, estrutura de projeto, nomenclatura, testes e formatação com ESLint/Prettier.
---

# Regras para JavaScript/TypeScript

## 1. Runtime e Versão
- **Node.js**: 20.x LTS (ou superior).
- **Package Manager**: npm (padrão), yarn ou pnpm (identifique lendo o arquivo de lock: `package-lock.json`, `yarn.lock` ou `pnpm-lock.yaml`).
- **TypeScript**: Quando presente, assuma `strict: true` no `tsconfig.json`. Priorize tipagem estática e evite o uso de `any`.

## 2. Estrutura de Projeto
A estrutura pode variar se for Frontend (React/Vue) ou Backend (Node/Express/Nest). Adapte-se ao contexto:

**Exemplo Frontend (React/Vite):**
```text
src/
├── components/     # Componentes visuais
├── services/       # Lógica de negócio e chamadas de API
├── hooks/          # Custom hooks
├── types/          # Tipagem global TypeScript
└── utils/          # Funções utilitárias
```

**Exemplo Backend (Node.js):**
```text
src/
├── controllers/    # Lida com requisições e respostas
├── services/       # Regras de negócio
├── routes/         # Definição de rotas da API
├── models/         # Esquemas de banco de dados
└── utils/          # Funções utilitárias
```

## 3. Convenções de Código

### Nomenclatura (Sempre em pt-BR)
- **Variáveis e Funções**: camelCase (`calcularTotal`, `usuarioAtual`).
- **Componentes React**: PascalCase (`FormularioProduto`, `ListaCarrinho`).
- **Constantes**: SCREAMING_SNAKE_CASE (`CHAVE_STORAGE`, `URL_API`).
- **Tipos/Interfaces**: PascalCase **sem prefixos** (`Produto`, `UsuarioProps`). *Evite usar prefixos como `IUsuario` ou `TipoProduto`, use apenas o nome da entidade.*

### Declaração e Assincronicidade
- **Variáveis**: Use `const` por padrão. Use `let` apenas se a variável precisar ser reatribuída. Nunca use `var`.
- **Assincronicidade**: Priorize `async/await` com blocos `try/catch` em vez de encadeamento de `.then().catch()`.
- **Funções**: 
  - Preferir *arrow functions* para funções anônimas e callbacks.
  - Usar *function declaration* (`function nomeDaFuncao() {}`) para funções nomeadas exportadas, aproveitando o hoisting.

### Imports
- Use imports absolutos quando configurado no `tsconfig.json` ou Vite/Webpack.
- Ordem de agrupamento: Bibliotecas externas → Componentes internos → Utils → Tipos.

## 4. Testes
- **Framework**: Vitest (para projetos Vite) ou Jest.
- **Nomenclatura**: `<arquivo>.test.ts` ou `<arquivo>.spec.ts`.
- **Cobertura**: Foco em testar comportamento e regras de negócio (mínimo desejado de 70%).

## 5. Formatação e Linting
- **Prettier**: Respeite as regras do `.prettierrc` se existir no projeto.
- **ESLint**: Siga as regras do `.eslintrc` ou `eslint.config.js`.
- **Padrão Geral (se não houver config)**: Uso de ponto e vírgula (semicolons) obrigatório e aspas simples (`'`) para strings.

## 6. Ambiente de Desenvolvimento
- **Dev Container**: Docker Compose com Node.js Alpine.
- **Variáveis de Ambiente**: `.env.development` para desenvolvimento (nunca commite arquivos `.env` reais).
- **Hot Reload**: Habilitado via Vite/Webpack ou `tsx watch`/`nodemon` no backend.

## 7. Documentação
- Use **JSDoc** (`/** ... */`) para documentar funções públicas, parâmetros e retornos.
- Comentários em português explicando o *porquê* de lógicas complexas, não o *o quê*.
- Mantenha o `README.md` atualizado com instruções de setup.
