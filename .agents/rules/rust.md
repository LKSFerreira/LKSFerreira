---
trigger: model_decision
description: Convenções Rust, Cargo, Ownership, tratamento de erros idiomático e Clippy.
---

# Regras para Rust

## 1. Toolchain e Gerenciamento (Cargo)

O ecossistema Rust é centralizado no **Cargo**. Ele é o gerenciador de pacotes, sistema de build e executor de testes.

**Regras de Execução:**

- **NUNCA** invoque o compilador `rustc` diretamente. Use sempre o `cargo`.

**Comandos Padrão:**

```bash
# Adicionar dependência (crate)
cargo add serde

# Compilar o projeto (modo dev)
cargo build

# Rodar o projeto
cargo run

# Rodar testes
cargo test

# Compilar para produção (otimizado)
cargo build --release
```

## 2. Estrutura de Projeto

A estrutura padrão do Cargo deve ser estritamente respeitada.

```text
projeto/
├── Cargo.toml          # Manifesto de dependências e metadados
├── src/
│   ├── main.rs         # Ponto de entrada para binários
│   ├── lib.rs          # Ponto de entrada para bibliotecas
│   └── modelos.rs      # Módulos adicionais
├── tests/              # Testes de integração (pasta raiz)
└── target/             # Diretório de build (ignorado no git)
```

## 3. Convenções de Código

### Nomenclatura (Sempre em pt-BR)

- **Structs, Enums e Traits**: PascalCase (`CarrinhoCompras`, `StatusPagamento`).
- **Funções, Variáveis e Módulos**: snake_case (`calcular_total`, `usuario_atual`).
- **Constantes e Statics**: SCREAMING_SNAKE_CASE (`TAXA_MAXIMA`).

### Boas Práticas de Módulos

- Mantenha a árvore de módulos limpa. Declare módulos no `main.rs` ou `lib.rs` usando `mod nome_do_modulo;`.
- Use a keyword `pub` apenas onde a visibilidade externa for estritamente necessária.

## 4. Segurança e Paradigmas (CRUCIAL)

A regra de ouro do Rust é: **Trabalhe com o Borrow Checker, não contra ele.**

- **Ownership e Borrowing**:
  - Priorize passar referências (`&T` ou `&mut T`) em vez de transferir o _ownership_ (propriedade), a menos que a função precise consumir o valor.
  - **PROIBIDO** o uso excessivo de `.clone()`. Só clone um dado se for arquiteturalmente indispensável.
- **Tratamento de Erros (Sem Exceptions)**:
  - **PROIBIDO** o uso de `.unwrap()` ou `.expect()` em código de produção. Eles causam _panics_ (crashes).
  - Retorne sempre `Result<T, E>` para erros recuperáveis e `Option<T>` para ausência de valor.
  - Propague erros usando o operador `?` (ex: `let arquivo = File::open("caminho")?;`).
- **Mutabilidade**: Variáveis são imutáveis por padrão. Use `mut` apenas quando a variável precisar ser alterada.

## 5. Testes

- **Testes Unitários**: Devem ficar no mesmo arquivo do código que estão testando, dentro de um módulo anotado com `#`.
- **Testes de Integração**: Devem ficar na pasta `tests/` na raiz do projeto.

**Exemplo de Teste Unitário:**

```rust
#
mod tests {
    use super::*;

    #
    fn deve_calcular_total_corretamente() {
        assert_eq!(calcular_total(10.0, 2.0), 20.0);
    }
}
```

## 6. Linting e Formatação

- **Formatador**: O código deve estar sempre em conformidade com o `cargo fmt`.
- **Linter (Clippy)**: O código gerado deve passar sem avisos no `cargo clippy`. O Clippy é a autoridade máxima de boas práticas em Rust. Se o Clippy sugerir uma melhoria, aplique-a.

## 7. Documentação (Rustdoc)

Use comentários de documentação `///` para funções, structs e traits públicas. O Rustdoc suporta Markdown e executa blocos de código como testes.

**Exemplo:**

````rust
/// Calcula o valor com desconto aplicado.
///
/// # Exemplos
///
/// ```
/// let total = meu_app::aplicar_desconto(100.0, 10.0);
/// assert_eq!(total, 90.0);
/// ```
pub fn aplicar_desconto(valor: f64, desconto: f64) -> f64 {
    valor - desconto
}
````

### 7.1: Comentários Didáticos Inline

Este repositório é de **ESTUDOS**. Além do Rustdoc (`///`), o código deve conter **comentários inline didáticos** que sirvam como material de aprendizado para quem lê.

**Regras:**

1. Toda instrução não-trivial deve ter um comentário `//` acima explicando **o que faz** e **por quê**.
2. Blocos lógicos (loops, `match`, `if let`, `?`) devem ter um comentário de abertura contextualizando o bloco inteiro.
3. Variáveis com nomes curtos ou técnicos devem ter um comentário ao lado explicando seu propósito.
4. Dependências externas (`use`) devem ter um comentário rápido explicando para que servem.
5. Comentários em **pt-BR**, com linguagem acessível a iniciantes.
6. Comentários complementam o Rustdoc, **NÃO** o substituem.

**Exemplo Prático:**

```rust
// std::fs = módulo da biblioteca padrão para operações no sistema de arquivos
use std::fs;

// std::io = módulo de entrada/saída; importamos o tipo Error para tratar falhas
use std::io;

/// Lê o conteúdo de um arquivo e retorna apenas as linhas não vazias.
///
/// # Erros
///
/// Retorna `io::Error` se o arquivo não existir ou não puder ser lido.
pub fn ler_linhas_validas(caminho: &str) -> Result<Vec<String>, io::Error> {
    // read_to_string() lê o arquivo inteiro para a memória como uma String.
    // O operador '?' propaga o erro automaticamente caso a leitura falhe,
    // evitando a necessidade de um match ou unwrap manual
    let conteudo = fs::read_to_string(caminho)?;

    // Processa o conteúdo linha por linha usando iteradores:
    // .lines() = divide a string por quebras de linha (\n)
    // .filter() = descarta linhas que estão vazias após remover espaços
    // .map() = converte cada &str em String (tipo owned, com ownership próprio)
    // .collect() = agrupa todos os resultados em um Vec<String>
    let linhas: Vec<String> = conteudo
        .lines()
        .filter(|linha| !linha.trim().is_empty())
        .map(|linha| linha.to_string())
        .collect();

    // Ok() encapsula o resultado de sucesso dentro do tipo Result
    Ok(linhas)
}
```
