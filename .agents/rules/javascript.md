---
trigger: model_decision
description: Convenções JS/TS, estrutura de projeto, nomenclatura, testes e formatação com ESLint/Prettier.
---

# Regras para JavaScript/TypeScript:

## 1: Runtime e Versão

- **Node.js**: 20.x LTS (ou superior).
- **Package Manager**: npm (padrão), yarn ou pnpm (identifique lendo o arquivo de lock: `package-lock.json`, `yarn.lock` ou `pnpm-lock.yaml`).
- **TypeScript**: Quando presente, assuma `strict: true` no `tsconfig.json`. Priorize tipagem estática e evite o uso de `any`.

## 2: Estrutura de Projeto

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

## 3: Convenções de Código

### Nomenclatura (Sempre em pt-BR):

- **Variáveis e Funções**: camelCase (`calcularTotal`, `usuarioAtual`).
- **Componentes React**: PascalCase (`FormularioProduto`, `ListaCarrinho`).
- **Constantes**: SCREAMING_SNAKE_CASE (`CHAVE_STORAGE`, `URL_API`).
- **Tipos/Interfaces**: PascalCase **sem prefixos** (`Produto`, `UsuarioProps`). _Evite usar prefixos como `IUsuario` ou `TipoProduto`, use apenas o nome da entidade._

### Declaração e Assincronicidade:

- **Variáveis**: Use `const` por padrão. Use `let` apenas se a variável precisar ser reatribuída. Nunca use `var`.
- **Assincronicidade**: Priorize `async/await` com blocos `try/catch` em vez de encadeamento de `.then().catch()`.
- **Funções**:
  - Preferir _arrow functions_ para funções anônimas e callbacks.
  - Usar _function declaration_ (`function nomeDaFuncao() {}`) para funções nomeadas exportadas, aproveitando o hoisting.

### Imports:

- Use imports absolutos quando configurado no `tsconfig.json` ou Vite/Webpack.
- Ordem de agrupamento: Bibliotecas externas → Componentes internos → Utils → Tipos.

## 4: Testes

- **Framework**: Vitest (para projetos Vite) ou Jest.
- **Nomenclatura**: `<arquivo>.test.ts` ou `<arquivo>.spec.ts`.
- **Cobertura**: Foco em testar comportamento e regras de negócio (mínimo desejado de 70%).

## 5: Formatação e Linting

- **Prettier**: Respeite as regras do `.prettierrc` se existir no projeto.
- **ESLint**: Siga as regras do `.eslintrc` ou `eslint.config.js`.
- **Padrão Geral (se não houver config)**: Uso de ponto e vírgula (semicolons) obrigatório e aspas simples (`'`) para strings.

## 6: Ambiente de Desenvolvimento

- **Dev Container**: Docker Compose com Node.js Alpine.
- **Variáveis de Ambiente**: `.env.development` para desenvolvimento (nunca commite arquivos `.env` reais).
- **Hot Reload**: Habilitado via Vite/Webpack ou `tsx watch`/`nodemon` no backend.

## 7: Documentação

- Use **JSDoc** (`/** ... */`) para documentar funções públicas, parâmetros e retornos.
- Mantenha o `README.md` atualizado com instruções de setup.

### 7.1: Comentários Didáticos Inline

Este repositório é de **ESTUDOS**. Além do JSDoc, o código deve conter **comentários inline didáticos** que sirvam como material de aprendizado para quem lê.

**Regras:**

1. Toda instrução não-trivial deve ter um comentário `//` acima explicando **o que faz** e **por quê**.
2. Blocos lógicos (loops, condicionais, `try/catch`) devem ter um comentário de abertura contextualizando o bloco inteiro.
3. Variáveis com nomes curtos ou técnicos devem ter um comentário ao lado explicando seu propósito.
4. Imports de bibliotecas externas devem ter um comentário rápido explicando para que servem.
5. Comentários em **pt-BR**, com linguagem acessível a iniciantes.
6. Comentários complementam o JSDoc, **NÃO** o substituem.

**Exemplo Prático:**

```typescript
// zod = biblioteca de validação de schemas com inferência de tipo automática
import { z } from "zod";

// express = framework para criar servidores HTTP e rotas de API
import express from "express";

/**
 * Schema de validação para criação de um novo usuário.
 * Garante que os dados recebidos na API estejam no formato correto.
 */
const schemaUsuario = z.object({
  nome: z.string().min(2), // Nome precisa ter pelo menos 2 caracteres
  email: z.string().email(), // Valida formato de email automaticamente
  idade: z.number().min(18), // Idade mínima permitida: 18 anos
});

/**
 * Cria um novo usuário a partir dos dados da requisição.
 * @param {express.Request} req - Objeto da requisição HTTP.
 * @param {express.Response} res - Objeto da resposta HTTP.
 */
function criarUsuario(req: express.Request, res: express.Response) {
  // safeParse() valida os dados sem lançar exceção;
  // retorna um objeto com { success, data, error } em vez de fazer throw
  const resultado = schemaUsuario.safeParse(req.body);

  // Se a validação falhou, retorna 400 (Bad Request) com os erros detalhados
  if (!resultado.success) {
    return res.status(400).json({ erros: resultado.error.errors });
  }

  // Desestrutura os campos validados para usar individualmente
  const { nome, email, idade } = resultado.data;

  // Aqui entraria a lógica de persistência no banco de dados
  // Por enquanto, retorna os dados validados como confirmação
  return res.status(201).json({ nome, email, idade });
}
```
