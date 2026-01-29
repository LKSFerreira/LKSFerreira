---
trigger: model_decision
description: Convenções Java, estrutura de projeto (puro e Spring Boot), comandos de compilação e execução.
---

# Regras para Java

## 1. Versão e Ambiente

- **JDK**: 17+ (LTS) ou 21+ (LTS)
- **IDE**: Qualquer (VS Code, IntelliJ, Eclipse)

## 2. Purista vs Framework

### 2.1 Estrutura para Java Puro

Ideal para estudar conceitos básicos, lambdas e streams.

```
projeto/
├── src/
│   └── Main.java
├── out/           # Arquivos compilados (.class)
└── README.md
```

**Compilação e Execução:**

```bash
# Compilar
javac src/Main.java -d out/

# Executar
java -cp out/ Main

# Compilar múltiplos arquivos
javac src/*.java -d out/
```

---

### 2.2 Estrutura para Spring Boot

Ideal para estudar Spring Framework, APIs REST e injeção de dependência.

```
projeto/
├── src/
│   └── main/
│       ├── java/
│       │   └── com/exemplo/
│       │       └── Application.java
│       └── resources/
│           └── application.properties
├── pom.xml
└── README.md
```

**Compilação e Execução (Maven):**

```bash
# Baixar dependências e compilar
mvn compile

# Executar a aplicação
mvn spring-boot:run

# Executar testes
mvn test

# Gerar JAR executável
mvn package
```

> **Nota:** Projetos Spring Boot são criados via [start.spring.io](https://start.spring.io)

---

## 3. Convenções de Código

### Nomenclatura

- **Classes**: PascalCase (`GerenciadorProdutos`, `CarrinhoCompras`)
- **Métodos e variáveis**: camelCase (`calcularTotal`, `nomeCliente`)
- **Constantes**: SCREAMING_SNAKE_CASE (`TAXA_IMPOSTO`, `URL_API`)
- **Pacotes**: lowercase (`com.exemplo.servicos`)

### Boas Práticas

- Uma classe pública por arquivo
- Nome do arquivo = nome da classe
- Usar modificadores de acesso explícitos (`private`, `public`)

## 4. Conceitos do Curso (Lambdas e Streams)

### Lambda Expressions

- Sintaxe: `(parâmetros) -> expressão`
- Usadas com interfaces funcionais (`Consumer`, `Predicate`, `Function`)

### Stream API

- Operações intermediárias: `filter()`, `map()`, `sorted()`
- Operações terminais: `collect()`, `forEach()`, `reduce()`
- Streams são lazy (executam só quando necessário)

### Method References

- Referência a método: `Classe::metodo`
- Referência a construtor: `Classe::new`

## 5. Spring Framework (Básico)

- **Injeção de Dependência**: `@Autowired`
- **Componentes**: `@Component`, `@Service`, `@Repository`
- **Configuração**: `application.properties` ou `application.yml`

## 6. Ambiente Docker (DevContainer)

Para estudar sem instalar Java localmente:

```yaml
# compose.yaml
services:
  java:
    image: eclipse-temurin:21-jdk
    volumes:
      - ../:/workspace
    working_dir: /workspace
    command: sleep infinity
```
