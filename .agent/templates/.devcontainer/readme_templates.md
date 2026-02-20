# 🐳 Catálogo de Templates Docker

Este diretório contém os blueprints para o ambiente de desenvolvimento. 

## 📂 Recursos Disponíveis

- **Pasta `<linguagem>`**: Contém o `compose.yaml` pré-configurado para a stack.
- **`.env.example`**: Template mestre de variáveis de ambiente (deve ser movido para a raiz como `.env`).
- **`dev.sh`**: Script de inicialização (deve ser criado na raiz pelo Agente).

## 📋 Matriz de Compatibilidade

| Identificador | Porta App | Serviço de Dados | Host do Banco |
| :--- | :--- | :--- | :--- |
| `javascript-vite` | 5173 | PostgreSQL | `database` |
| `javascript-express`| 3000 | PostgreSQL | `database` |
| `python-fastapi` | 8000 | PostgreSQL | `database` |
| `python-django` | 8000 | PostgreSQL | `database` |
| `java-spring` | 8080 | PostgreSQL | `database` |
| `php-laravel` | 8000 | PostgreSQL + Redis | `database` |
| `go` | 8080 | PostgreSQL | `database` |
| `rust` | 8080 | PostgreSQL | `database` |

## ⚠️ Premissas Técnicas
- Todos os volumes de banco de dados são nomeados como `pgdata`.
- O script `dev.sh` é necessário para injetar o `HOST_IP` no ambiente (útil para conexões fora do container).