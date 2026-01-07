---
description: Configura infraestrutura de Dev Containers para desenvolvimento isolado via Docker
---

# Workflow: Configuração de Dev Containers

Este workflow guia a criação completa da infraestrutura de Dev Containers para projetos de qualquer linguagem.

## Pré-requisitos

- Docker Desktop instalado e funcionando
- VS Code com a extensão "Dev Containers" (`ms-vscode-remote.remote-containers`)

---

## 1. Criar Estrutura de Diretórios

Crie o diretório `.devcontainer` na raiz do projeto:

```bash
mkdir -p .devcontainer
```

---

## 2. Identificar a Linguagem do Projeto

Analise o projeto para identificar a linguagem principal:
- `pyproject.toml`, `requirements.txt` → Python
- `package.json` → JavaScript/TypeScript
- `go.mod` → Go
- `Cargo.toml` → Rust
- `pom.xml`, `build.gradle` → Java

---

## 3. Criar o devcontainer.json

Crie o arquivo `.devcontainer/devcontainer.json` com a estrutura abaixo, adaptando conforme a linguagem.

### Template para Python

```json
{
    "name": "Python Dev Container",
    "image": "mcr.microsoft.com/devcontainers/python:1-3.12-bullseye",
    
    "features": {
        "ghcr.io/devcontainers/features/git:1": {}
    },
    
    "forwardPorts": [],
    
    "postCreateCommand": "pip install --user -r requirements.txt && pip install --user -r requirements-dev.txt || true",
    
    "customizations": {
        "vscode": {
            "extensions": [
                "ms-python.python",
                "ms-python.vscode-pylance",
                "charliermarsh.ruff",
                "tamasfe.even-better-toml"
            ],
            "settings": {
                "python.defaultInterpreterPath": "/usr/local/bin/python",
                "python.testing.pytestEnabled": true,
                "python.testing.pytestArgs": ["tests"],
                "editor.formatOnSave": true
            }
        }
    },
    
    "remoteUser": "vscode"
}
```

### Template para JavaScript/TypeScript

```json
{
    "name": "Node.js Dev Container",
    "image": "mcr.microsoft.com/devcontainers/javascript-node:1-20-bullseye",
    
    "features": {
        "ghcr.io/devcontainers/features/git:1": {}
    },
    
    "forwardPorts": [3000],
    
    "postCreateCommand": "npm install",
    
    "customizations": {
        "vscode": {
            "extensions": [
                "dbaeumer.vscode-eslint",
                "esbenp.prettier-vscode"
            ],
            "settings": {
                "editor.formatOnSave": true,
                "editor.defaultFormatter": "esbenp.prettier-vscode"
            }
        }
    },
    
    "remoteUser": "node"
}
```

---

## 4. (Opcional) Criar Dockerfile Customizado

Se precisar de customizações avançadas, crie `.devcontainer/Dockerfile`:

```dockerfile
# Para Python
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Configurações adicionais
USER vscode
```

E atualize o `devcontainer.json`:

```json
{
    "build": {
        "dockerfile": "Dockerfile",
        "context": ".."
    }
}
```

---

## 5. (Opcional) Docker Compose para Multi-Serviços

Se o projeto precisar de banco de dados ou outros serviços, crie `.devcontainer/docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build:
      context: ..
      dockerfile: .devcontainer/Dockerfile
    volumes:
      - ..:/workspace:cached
    command: sleep infinity
    
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: dev
      POSTGRES_DB: app_dev
    volumes:
      - postgres-data:/var/lib/postgresql/data

volumes:
  postgres-data:
```

E atualize o `devcontainer.json`:

```json
{
    "dockerComposeFile": "docker-compose.yml",
    "service": "app",
    "workspaceFolder": "/workspace"
}
```

---

## 6. Atualizar .agent/rules/<linguagem>.md

Após criar o Dev Container, atualize as regras da linguagem para refletir o novo ambiente:

### Exemplo para Python

Substitua as referências a `.venv/Scripts/python.exe` por:
- **Python**: `python` ou `python3`
- **Pip**: `pip` ou `pip3`
- **Pytest**: `pytest`

> **Nota:** Dentro do Dev Container, não é necessário ambiente virtual. O container já fornece isolamento.

---

## 7. Abrir o Projeto no Dev Container

No VS Code:
1. Pressione `F1` ou `Ctrl+Shift+P`
2. Digite: `Dev Containers: Reopen in Container`
3. Aguarde o build e configuração automática

---

## 8. Commitar a Configuração

```bash
git add .devcontainer/
git commit -m ":bricks: ci: Adiciona configuracao de Dev Container"
```

---

## Verificação

- [ ] Container inicia sem erros
- [ ] Extensões do VS Code são instaladas automaticamente
- [ ] Dependências do projeto são instaladas via `postCreateCommand`
- [ ] Comandos da linguagem funcionam (ex: `python --version`, `pytest`)
