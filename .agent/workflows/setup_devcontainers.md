---
description: Workflow de Configuração de Ambiente Docker Compose
---

# Workflow: Configuração de Ambiente Docker Compose

Sempre que solicitado para configurar o ambiente Docker, atue como Especialista em DevOps e execute os passos abaixo rigorosamente.

## Filosofia

- **Docker Compose direto**: Sem Dev Containers, sem dependência de servidor remoto.
- **Simplicidade**: Um script para iniciar e compilar tudo (`dev.sh`).
- **Código sincronizado**: Volume bind monta o código local no container.
- **Hot reload**: Alterações são refletidas automaticamente.

---

## 1. Fase de Reconhecimento e Preparação

- Identifique a stack através dos arquivos de manifesto (`package.json`, `requirements.txt`, `go.mod`, etc.).
- Analise o arquivo `readme_templates.md`.
- Verifique os templates disponíveis em `.agent/templates/.devcontainer/`:

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

---

## 2. Implementação da Estrutura (Ação)

Execute as instruções abaixo para estruturar o ambiente:

1. **Diretório de Configuração**: Crie o diretório `.devcontainer/` na raiz do projeto (`mkdir -p .devcontainer`).
2. **Docker Compose e Dockerfile**: Copie o arquivo `compose.yaml` e o `Dockerfile.*` do template correspondente para a pasta `.devcontainer/`.
   - **Ajuste de Path**: Se o `compose.yaml` ou o `Dockerfile` referenciarem o código limitando ao diretório atual (`./`), altere para `../` para refletir que agora estão dentro de uma subpasta (`.devcontainer/`) e devem apontar para a raiz.
3. **Variáveis de Ambiente**:
   - Crie o arquivo `.env.development` na **raiz do projeto** (você pode se basear no `.env.example` do template, se houver).
   - **Personalização**: Substitua placeholders (como `nome_do_projeto` ou `meu_banco`) pelo nome real do diretório/projeto atual.
   - **Importante:** O nome do host para conexões entre containers é o nome do serviço no compose (ex: `database`), e não `localhost`.
4. **Script de Inicialização**: Crie o arquivo `dev.sh` na raiz com o conteúdo abaixo:

```bash
#!/bin/bash
# =============================================================================
# Dev Script - {nome do projeto}
# =============================================================================
# Este script detecta o IP da sua rede local (Windows) e inicia o Docker.
# Uso: ./dev.sh
# =============================================================================
IP=$(ipconfig | grep -oE "\b(192\.168\.[0-9]{1,3}\.[0-9]{1,3}|10\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\b" | head -n 1 | tr -d '\r ')
if [ -n "$IP" ]; then
    export HOST_IP=$IP
    echo -e "\033[0;32m✅ IP Detectado: $IP\033[0m"
else
    echo -e "\033[0;33m⚠️ IP Local não detectado.\033[0m"
fi
docker compose -f .devcontainer/compose.yaml up --build
```

---

## 3. Estrutura Final Esperada

```text
projeto/
├── .devcontainer/
│   ├── compose.yaml          # Docker Compose
│   └── Dockerfile.{stack}    # Ex: .python - .node - .postgres
├── .env.development          # Variáveis de ambiente
├── dev.sh                    # Script de inicialização
├── src/                      # Código fonte
└── ...
```

---

## 4. Segurança e Limpeza

1. **Atualizar `.gitignore`**: 
   Adicione as variáveis de ambiente e scripts locais ao `.gitignore`.
```gitignore
# Ambiente
.env
.env.local
.env.development
.env.*.local
dev.sh
```
2. **Permissões**: Se aplicável em sistemas Unix, informe ao usuário para rodar `chmod +x dev.sh`.
3. **Limpeza OBRIGATÓRIA**: Após estruturar o Docker, **remova o diretório de templates** pois ele já cumpriu seu propósito.
```bash
rm -rf .agent/templates/
```
> **Motivo:** Os templates são usados apenas na inicialização do projeto. Mantê-los no repositório gera duplicação desnecessária.

---

## 5. Entrega Final e Comandos Úteis

Confirme as configurações validando os itens abaixo:

- [ ] `.devcontainer/compose.yaml` e `Dockerfile.{stack}` configurados corretamente.
- [ ] `.env.development` criado na raiz com as credenciais preenchidas.
- [ ] `dev.sh` criado com a detecção de IP.
- [ ] Gitignore atualizado.
- [ ] Templates removidos da raiz com sucesso.

**Iniciando a aplicação**
```bash
bash dev.sh
```

**Outros Comandos Úteis**
Execute a partir da raiz (ou acesse a pasta `.devcontainer/`):
| Comando                                                | Descrição                           |
| ------------------------------------------------------ | ----------------------------------- |
| `docker compose -f .devcontainer/compose.yaml down`    | Para os containers                  |
| `docker compose -f .devcontainer/compose.yaml down -v` | Para e remove volumes (limpa banco) |
| `docker compose -f .devcontainer/compose.yaml logs -f` | Mostra logs da aplicação e serviços |