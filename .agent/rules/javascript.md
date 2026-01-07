---
trigger: linguagem_projeto == "javascript"
---

# Regras para JavaScript/TypeScript

## 1. Runtime e Versão

- **Node.js**: 20.x LTS
- **Package Manager**: npm (padrão) ou pnpm
- **TypeScript**: quando presente, usar strict mode

## 2. Estrutura de Projeto

```
src/
├── components/     # Componentes React
├── services/       # Lógica de negócio e APIs
├── hooks/          # Custom hooks
├── types/          # Tipos TypeScript
└── utils/          # Funções utilitárias
```

## 3. Convenções de Código

### Nomenclatura

- **Variáveis e funções**: camelCase em português (`calcularTotal`, `usuarioAtual`)
- **Componentes React**: PascalCase (`FormularioProduto`, `ListaCarrinho`)
- **Constantes**: SCREAMING_SNAKE_CASE (`CHAVE_STORAGE`, `URL_API`)
- **Tipos/Interfaces**: PascalCase com prefixo descritivo (`TipoProduto`, `InterfaceUsuario`)

### Imports

- Imports absolutos quando configurado no tsconfig/vite
- Agrupar por: bibliotecas externas → componentes → utils → tipos

### Funções

- Preferir arrow functions para funções anônimas
- Usar function declaration para funções nomeadas exportadas

## 4. Testes

- **Framework**: Vitest (projetos Vite) ou Jest
- **Nomenclatura**: `<arquivo>.test.ts` ou `<arquivo>.spec.ts`
- **Cobertura mínima**: 70%

## 5. Formatação

- **Prettier**: Configurado em `.prettierrc`
- **ESLint**: Usar configuração do projeto
- **Semicolons**: Sim (configurable)
- **Quotes**: Single quotes para strings

## 6. Ambiente de Desenvolvimento

- **Dev Container**: Docker Compose com Node.js Alpine
- **Variáveis de ambiente**: `.env.development` para desenvolvimento
- **Hot Reload**: Habilitado via Vite/Webpack

## 7. Documentação

- JSDoc para funções públicas
- Comentários em português explicando lógica complexa
- README.md atualizado com instruções de setup
