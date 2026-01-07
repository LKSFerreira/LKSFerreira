# 🐳 Templates Docker Compose

Templates prontos para desenvolvimento com Docker Compose.

## Como Usar

1. Copie a pasta da linguagem desejada para `.devcontainer/` do seu projeto
2. Renomeie `compose.yaml.template` para `compose.yaml`
3. Crie o arquivo `.env.development` na raiz do projeto
4. Execute `docker compose up` dentro de `.devcontainer/`

## Templates Disponíveis

| Linguagem                 | Porta Padrão | Banco de Dados     |
| ------------------------- | ------------ | ------------------ |
| JavaScript (Node/Vite)    | 5173         | PostgreSQL         |
| JavaScript (Node/Express) | 3000         | PostgreSQL         |
| Python (FastAPI)          | 8000         | PostgreSQL         |
| Python (Django)           | 8000         | PostgreSQL         |
| Java (Spring Boot)        | 8080         | PostgreSQL         |
| PHP (Laravel)             | 8000         | PostgreSQL + Redis |
| Go (Fiber/Gin)            | 8080         | PostgreSQL         |
| Rust (Actix/Axum)         | 8080         | PostgreSQL         |

## Estrutura de Cada Template

```
linguagem/
├── compose.yaml    # Docker Compose configurado
├── .env.example    # Variáveis de ambiente exemplo
└── README.md       # Instruções específicas
```
