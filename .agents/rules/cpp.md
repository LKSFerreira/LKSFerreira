---
trigger: model_decision
description: Convenções C++, padrões modernos (C++17/20), gerenciamento de memória, CMake e testes.
---

# Regras para C++

## 1. Padrão e Compilador
- **Standard**: C++17 ou C++20 (Estritamente C++ moderno).
- **Compiladores**: GCC, Clang ou MSVC.
- **Aviso Importante**: **NUNCA** escreva código estilo "C com classes" (C++98/03). Utilize sempre as abstrações modernas da STL (Standard Template Library).

## 2. Estrutura de Projeto e Build System (CMake)
O **CMake** é o sistema de build padrão absoluto. Não utilize Makefiles puros a menos que seja explicitamente solicitado.

```text
projeto/
├── CMakeLists.txt      # Configuração do build
├── include/            # Arquivos de cabeçalho (.h, .hpp)
│   └── projeto/
├── src/                # Arquivos de implementação (.cpp)
├── tests/              # Testes unitários
└── build/              # Diretório de saída (ignorado no git)
```

**Comandos Padrão (CMake):**
```bash
# Configurar o projeto (gerar arquivos de build)
cmake -S . -B build

# Compilar o projeto
cmake --build build

# Rodar testes (se configurado com CTest)
cd build && ctest
```

## 3. Convenções de Código

### Nomenclatura (Sempre em pt-BR)
- **Classes e Structs**: PascalCase (`GerenciadorMemoria`, `VetorDinamico`).
- **Métodos e Variáveis**: snake_case (`calcular_total`, `usuario_atual`) - *Padrão da STL*.
- **Constantes e Macros**: SCREAMING_SNAKE_CASE (`TAXA_MAXIMA`, `TAMANHO_BUFFER`). Evite macros (`#define`), prefira `constexpr`.
- **Namespaces**: snake_case (`namespace sistema_bancario`).

### Boas Práticas de Arquitetura
- Separe declaração (`.hpp` ou `.h`) da implementação (`.cpp`).
- Use `#pragma once` no topo de todos os arquivos de cabeçalho (evite os antigos *include guards* `#ifndef`).
- Evite `using namespace std;` em arquivos globais ou de cabeçalho para não poluir o escopo.

## 4. C++ Moderno e Gerenciamento de Memória (CRUCIAL)

A regra de ouro é: **Evite vazamento de memória e cópias desnecessárias.**

- **Ponteiros e Alocação**: 
  - **PROIBIDO** usar `new` e `delete` (ponteiros crus/raw pointers), a menos que esteja escrevendo um alocador customizado.
  - Use **Smart Pointers**: `std::unique_ptr` (padrão) e `std::shared_ptr` (apenas quando o *ownership* for compartilhado).
  - Instancie com `std::make_unique` e `std::make_shared`.
- **Passagem de Parâmetros**:
  - Tipos primitivos (`int`, `float`): Passe por valor.
  - Tipos complexos (`std::string`, `std::vector`, classes): Passe por **referência constante** (`const T&`) para evitar cópias.
- **Const Correctness**: Marque variáveis como `const` sempre que possível. Marque métodos de classe que não alteram o estado do objeto com `const` no final da assinatura.
- **Strings**: Use `std::string`. Se for apenas para leitura/passagem de parâmetro, prefira `std::string_view` (C++17).

## 5. Testes
- **Framework**: Google Test (GTest) ou Catch2.
- **Nomenclatura**: Arquivos de teste devem terminar com `_test.cpp` (ex: `calculadora_test.cpp`).

## 6. Formatação e Linting
- **Formatador**: Assuma o uso do `clang-format`. Respeite o arquivo `.clang-format` na raiz do projeto.
- **Linter/Análise Estática**: Assuma o uso do `clang-tidy` para capturar bugs e sugerir modernizações no código.

## 7. Documentação (Doxygen)
Use o padrão Doxygen para documentar classes e métodos públicos nos arquivos de cabeçalho (`.hpp`). Não polua o `.cpp` com documentação de interface.

**Exemplo:**
```cpp
/**
 * @brief Processa o pagamento de um cliente.
 * 
 * @param valor_compra O valor total da compra.
 * @param id_cliente O identificador único do cliente.
 * @return true Se o pagamento for aprovado.
 * @return false Se o pagamento for recusado.
 */
bool processar_pagamento(double valor_compra, const std::string& id_cliente);
```