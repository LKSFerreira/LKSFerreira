---
description: Workflow de Configuração de Ambiente Docker Compose
---

# Workflow: Configuração de Ambiente Docker Compose:

Sempre que solicitado para configurar o ambiente Docker, atue como Especialista em DevOps e execute os passos abaixo rigorosamente.

## Filosofia:

- **Docker Compose direto**: Sem Dev Containers, sem dependência de servidor remoto.
- **Simplicidade**: Um script para iniciar e compilar tudo (`dev.sh`).
- **Código sincronizado**: Volume bind monta o código local no container.
- **Hot reload**: Alterações são refletidas automaticamente.

---

## 1: Fase de Reconhecimento e Preparação

- Use `AGENTS.md` (campo `LINGUAGEM_PROJETO`) como fonte de verdade da stack.
- Faça detecção por manifesto (`package.json`, `requirements.txt`, `go.mod`, etc.) apenas como fallback/validação quando o `AGENTS.md` estiver ausente ou inconsistente.
- Este workflow é a fonte de verdade para seleção de template.
- Use somente os templates abaixo, que refletem o conteúdo real de `.agents/templates/.docker/`:

| Contexto | Template |
| --- | --- |
| C++ | `c++/` |
| Go | `go/` |
| Java (genérico) | `java/` |
| Java (Spring Boot) | `java-spring/` |
| JavaScript (Express) | `javascript-express/` |
| JavaScript (Vite/React) | `javascript-vite/` |
| Node.js (genérico) | `node/` |
| PHP (Laravel) | `php-laravel/` |
| PostgreSQL isolado | `postgress/` |
| Python (genérico) | `python/` |
| Python (Django) | `python-django/` |
| Python (FastAPI) | `python-fastapi/` |
| Rust | `rust/` |

### Regra de seleção determinística do template

1. Use `LINGUAGEM_PROJETO` do `AGENTS.md`.
2. Se for `javascript`:
   - Com Vite/React: `javascript-vite/`.
   - Com Express: `javascript-express/`.
   - Sem framework claro: `node/`.
3. Se for `python`:
   - Com FastAPI: `python-fastapi/`.
   - Com Django: `python-django/`.
   - Sem framework claro: `python/`.
4. Se for `java`:
   - Com Spring Boot: `java-spring/`.
   - Sem Spring: `java/`.
5. Se for `go`: `go/`.
6. Se for `rust`: `rust/`.
7. Se for `c++`: `c++/`.
8. Se a demanda for somente banco local: `postgress/`.
9. Se não houver correspondência exata, não invente template.

---

## 2: Implementação da Estrutura (Ação)

Execute as instruções abaixo para estruturar o ambiente:

1. **Diretório de Configuração**: Crie o diretório `.docker/` na raiz do projeto (`mkdir -p .docker`).
2. **Docker Compose e Dockerfile**: Copie o arquivo `compose.yaml` e o `Dockerfile.*` do template selecionado na matriz acima para a pasta `.docker/`.
   - **Ajuste de Path**: Se o `compose.yaml` ou o `Dockerfile` referenciarem o código limitando ao diretório atual (`./`), altere para `../` para refletir que agora estão dentro de uma subpasta (`.docker/`) e devem apontar para a raiz.
3. **Variáveis de Ambiente**:
   - Mova o `.env.example` do template para a **raiz do projeto**.
   - Em seguida, faça uma cópia e renomeie para `.env`.
   - Exemplo de fluxo:
```bash
mv .agents/templates/.env.example ./.env.example
cp ./.env.example ./.env
```
   - **Personalização**: Substitua placeholders no `.env` (como `nome_do_projeto` ou `meu_banco`) pelo nome real do diretório/projeto atual.
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
docker compose -f .docker/compose.yaml up --build
```

---

## 3: Estrutura Final Esperada

```text
projeto/
├── .docker/
│   ├── compose.yaml          # Docker Compose
│   └── Dockerfile.{stack}    # Ex: .python - .node - .postgres
├── .env.example              # Template de variáveis
├── .env                      # Variáveis locais de execução
├── dev.sh                    # Script de inicialização
├── src/                      # Código fonte
└── ...
```

---

## 4: Segurança e Limpeza

1. **Atualizar `.gitignore`**: 
   Adicione as variáveis de ambiente e scripts locais ao `.gitignore`.
```gitignore
# Ambiente
.env
.env.local
.env.*.local
dev.sh
```
2. **Permissões**: Se aplicável em sistemas Unix, informe ao usuário para rodar `chmod +x dev.sh`.
3. **Limpeza OBRIGATÓRIA**: Após estruturar o Docker, **remova o diretório de templates** pois ele já cumpriu seu propósito.
```bash
rm -rf .agents/templates/
```
> **Motivo:** Os templates são usados apenas na inicialização do projeto. Mantê-los no repositório gera duplicação desnecessária.

---

## 5: Entrega Final e Ações Obrigatórias

Confirme as configurações validando os itens abaixo:

- [ ] `.docker/compose.yaml` e `Dockerfile.{stack}` configurados corretamente.
- [ ] `.env.example` movido para a raiz do projeto.
- [ ] `.env` criado a partir do `.env.example` com as credenciais preenchidas.
- [ ] `dev.sh` criado com a detecção de IP.
- [ ] Gitignore atualizado.
- [ ] Templates removidos da raiz com sucesso.

### Execute para iniciar a aplicação
```bash
bash dev.sh
```
### Execute para validar os serviços após subir
```bash
docker compose -f .docker/compose.yaml ps
```

### Para manutenção e reset, siga `.docker/docker.md`


