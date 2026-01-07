---
description: Configura ambiente de desenvolvimento com Docker Compose (sem servidor remoto)
---

# Workflow: Configuração de Ambiente Docker Compose

Este workflow configura o ambiente de desenvolvimento usando Docker Compose puro — simples, leve e sem dependência de servidor remoto.

## Filosofia

- **Docker Compose direto**: Sem Dev Containers, sem servidor remoto
- **Um comando**: `docker compose up` e pronto
- **Código sincronizado**: Volume bind monta o código local no container
- **Hot reload**: Alterações são refletidas automaticamente

---

## 1. Criar Estrutura

```bash
mkdir -p .devcontainer
```

---

## 2. Identificar Linguagem e Copiar Template

Verifique os templates disponíveis em `.agent/templates/.devcontainer/`:

| Linguagem                 | Template              |
| ------------------------- | --------------------- |
| JavaScript (Vite/React)   | `javascript-vite/`    |
| JavaScript (Express/Next) | `javascript-express/` |
| Python (FastAPI)          | `python-fastapi/`     |
| Python (Django)           | `python-django/`      |
| Java (Spring Boot)        | `java-spring/`        |
| PHP (Laravel)             | `php-laravel/`        |
| Go                        | `go/`                 |
| Rust                      | `rust/`               |

Copie o `compose.yaml` do template para `.devcontainer/`:

```bash
cp .agent/templates/.devcontainer/<linguagem>/compose.yaml .devcontainer/
```

---

## 3. Criar Arquivo de Variáveis de Ambiente

Crie `.env.development` na **raiz do projeto** (não dentro de `.devcontainer/`):

```bash
# PostgreSQL
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=nome_do_projeto

# Conexão com o banco
DATABASE_URL=postgresql://postgres:postgres@database:5432/nome_do_projeto

# Variáveis específicas do projeto
# ...
```

> **Importante:** O nome do host é `database` (nome do serviço no compose), não `localhost`.

---

## 4. Estrutura Final

```
projeto/
├── .devcontainer/
│   └── compose.yaml          # Docker Compose
├── .env.development          # Variáveis de ambiente
├── src/                      # Código fonte
└── ...
```

---

## 5. Executar o Ambiente

```bash
cd .devcontainer
docker compose up
```

Ou em background:

```bash
docker compose up -d
docker compose logs -f app
```

---

## 6. Comandos Úteis

| Comando                      | Descrição                           |
| ---------------------------- | ----------------------------------- |
| `docker compose up`          | Inicia os containers                |
| `docker compose down`        | Para os containers                  |
| `docker compose down -v`     | Para e remove volumes (limpa banco) |
| `docker compose logs -f app` | Mostra logs do app                  |
| `docker compose exec app sh` | Acessa shell do container           |

---

## 7. Atualizar .gitignore

Adicione ao `.gitignore`:

```gitignore
# Ambiente
.env
.env.local
.env.development
.env.*.local
```

---

## Verificação

- [ ] `docker compose up` inicia sem erros
- [ ] App é acessível na porta configurada (ex: `localhost:5173`)
- [ ] Banco de dados conecta corretamente
- [ ] Alterações no código são refletidas automaticamente (hot reload)

---

## 8. Limpeza: Remover Templates (OBRIGATÓRIO)

Após copiar o template para `.devcontainer/`, **remova o diretório de templates** pois ele já cumpriu seu propósito:

```bash
rm -rf .agent/templates/
```

> **Motivo:** Os templates são usados apenas na inicialização do projeto. Mantê-los no repositório gera duplicação desnecessária.
