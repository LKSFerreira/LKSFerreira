---
description: Workflow de Configuração de Ambiente Docker Compose
---

Sempre que solicitado para configurar o ambiente Docker, atue como Especialista em DevOps e execute os passos abaixo rigorosamente.

## 1. Fase de Reconhecimento
- Identifique a stack através dos arquivos de manifesto (`package.json`, `requirements.txt`, `go.mod`, etc.).
- Localize o template correspondente em `.agent/templates/.devcontainer/`.

## 2. Implementação da Estrutura (Ação)

Execute os comandos para montar o ambiente:

1. **Diretório de Configuração**: Crie `.devcontainer/` na raiz.
2. **Docker Compose**: Copie o arquivo `compose.yaml` e `Dockerfile.*` do template escolhido para `.devcontainer/`.
   - **Ajuste de Path**: Se o `compose.yaml` ou o `Dockerfile` referenciarem o código como `./`, altere para `../` para refletir que agora estão dentro de uma subpasta e devem apontar para a raiz.
3. **Variáveis de Ambiente**:
   - Copie `.agent/templates/.devcontainer/.env.example` para a raiz do projeto com o nome `.env`.
   - **Personalização**: Substitua `meu_banco` ou `nome_do_projeto` pelo nome real do diretório atual.
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

## 3. Segurança e Limpeza
- **Git**: Adicione `.env` e `dev.sh` (opcional) ao `.gitignore` se não estiverem lá.
- **Permissões**: Informe ao usuário que ele deve rodar `chmod +x dev.sh` em sistemas Unix.
- **Cleanup (Obrigatório)**: Remova o diretório `.agent/templates/` após concluir a configuração.

## 4. Entrega Final
Apresente o resumo:
- [ ] `.devcontainer/compose.yaml` configurado.
- [ ] `.env` criado na raiz com as credenciais.
- [ ] `dev.sh` criado na raiz.
- [ ] Templates removidos.

**Comando para iniciar:** `bash dev.sh`