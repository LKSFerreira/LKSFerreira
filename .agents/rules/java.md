---
trigger: model_decision
description: Convenções Java, estrutura de projeto (puro e Spring Boot), comandos de compilação e execução.
---

# Regras para Java:

## 1: Versão e Ambiente

- **JDK**: 17+ (LTS) ou 21+ (LTS).
- **Recursos Modernos**: Sempre que aplicável e melhorar a legibilidade, utilize recursos do Java moderno (ex: `Records`, `var` para variáveis locais, `Text Blocks` e `Switch Expressions`).

## 2: Purista vs Framework

### 2.1: Estrutura para Java Puro:

Ideal para estudar conceitos básicos, algoritmos, lambdas e streams.

```text
projeto/
├── src/
│   └── Main.java
├── out/           # Arquivos compilados (.class)
└── README.md
```

**Compilação e Execução:**

```bash
# Compilar um arquivo
javac -d out/ src/Main.java

# Executar
java -cp out/ Main

# Compilar múltiplos arquivos no diretório
javac -d out/ src/*.java
```

---

### 2.2: Estrutura para Spring Boot:

Ideal para estudar Spring Framework, APIs REST e injeção de dependência.

```text
projeto/
├── src/
│   └── main/
│       ├── java/
│       │   └── com/exemplo/
│       │       └── Application.java
│       └── resources/
│           └── application.properties
├── pom.xml (ou build.gradle)
└── README.md
```

**Compilação e Execução (Assuma Maven como padrão, a menos que veja um build.gradle):**

```bash
# Baixar dependências e compilar
mvn clean compile

# Executar a aplicação
mvn spring-boot:run

# Executar testes
mvn test

# Gerar JAR executável
mvn clean package
```

> **Nota:** Projetos Spring Boot são criados via `https://start.spring.io`. Se o projeto usar o wrapper do Maven, utilize `./mvnw` em vez de `mvn`.

---

## 3: Convenções de Código

### Nomenclatura (Sempre em pt-BR, conforme regra global):

- **Classes/Records/Interfaces**: PascalCase (`GerenciadorProdutos`, `CarrinhoCompras`).
- **Métodos e Variáveis**: camelCase (`calcularTotal`, `nomeCliente`).
- **Constantes**: SCREAMING_SNAKE_CASE (`TAXA_IMPOSTO`, `URL_API`).
- **Pacotes**: lowercase e sem caracteres especiais (`com.exemplo.servicos`).

### Boas Práticas:

- Uma classe pública por arquivo.
- Nome do arquivo = nome da classe.
- Use modificadores de acesso explícitos (`private`, `public`, `protected`).
- **Imutabilidade**: Priorize o uso de `final` para variáveis e atributos que não devem ser alterados.

## 4: Conceitos do Curso (Lambdas e Streams)

- **Lambda Expressions**: Sintaxe `(parametros) -> expressao`. Usadas com interfaces funcionais (`Consumer`, `Predicate`, `Function`).
- **Stream API**:
  - Operações intermediárias: `filter()`, `map()`, `sorted()`.
  - Operações terminais: `collect()`, `forEach()`, `reduce()`.
  - Lembre-se: Streams são *lazy* (executam só quando necessário).
- **Method References**: `Classe::metodo` ou `Classe::new`.

## 5: Spring Framework (Boas Práticas)

- **Injeção de Dependência**: **Evite** usar `@Autowired` em atributos (Field Injection). Priorize sempre a **Injeção via Construtor** (Constructor Injection), seja manualmente ou usando `@RequiredArgsConstructor` do Lombok.
- **Componentes**: `@Component`, `@Service`, `@Repository`, `@RestController`.
- **Configuração**: `application.properties` ou `application.yml`.

## 6: Ambiente Docker (DevContainer)

Para rodar/estudar sem instalar o Java localmente:

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

## 7: Documentação

### Javadoc

- Use **Javadoc** (`/** ... */`) para documentar classes, métodos e atributos públicos.
- Inclua `@param`, `@return` e `@throws` quando aplicável.

### 7.1: Comentários Didáticos Inline

Este repositório é de **ESTUDOS**. Além do Javadoc, o código deve conter **comentários inline didáticos** que sirvam como material de aprendizado para quem lê.

**Regras:**

1. Toda instrução não-trivial deve ter um comentário `//` acima explicando **o que faz** e **por quê**.
2. Blocos lógicos (loops, condicionais, `try/catch`) devem ter um comentário de abertura contextualizando o bloco inteiro.
3. Variáveis com nomes curtos ou técnicos devem ter um comentário ao lado explicando seu propósito.
4. Imports de bibliotecas externas devem ter um comentário rápido explicando para que servem.
5. Comentários em **pt-BR**, com linguagem acessível a iniciantes.
6. Comentários complementam o Javadoc, **NÃO** o substituem.

**Exemplo Prático:**

```java
// List e ArrayList = estruturas de dados da Collections Framework
// List é a interface (contrato), ArrayList é a implementação (array dinâmico)
import java.util.List;
import java.util.ArrayList;

// Stream API = permite processar coleções de forma declarativa (filter, map, reduce)
import java.util.stream.Collectors;

/**
 * Gerencia uma lista de produtos com operações de busca e filtragem.
 */
public class GerenciadorProdutos {

    // Lista interna que armazena todos os produtos cadastrados
    private final List<String> produtos = new ArrayList<>();

    /**
     * Filtra os produtos cujo nome contém o termo buscado (case-insensitive).
     *
     * @param termo Palavra-chave para busca.
     * @return Lista de produtos que contêm o termo.
     */
    public List<String> buscar(String termo) {
        // Converte o termo para minúsculas uma única vez,
        // evitando repetir a conversão a cada iteração do stream
        var termoNormalizado = termo.toLowerCase();

        // Stream API: transforma a lista em um fluxo de dados para processar
        // .filter() = mantém apenas os elementos que satisfazem a condição
        // .collect() = agrupa os resultados filtrados de volta em uma nova List
        return produtos.stream()
            .filter(produto -> produto.toLowerCase().contains(termoNormalizado))
            .collect(Collectors.toList());
    }
}
```

