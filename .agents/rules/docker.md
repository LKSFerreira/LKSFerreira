---
trigger: always_on
---

# Regra Obrigatória: Dependências e Ambiente Docker

## 1: Fonte da Verdade do Ambiente
- O ambiente de desenvolvimento deste projeto é Docker Compose com arquivos em `.docker/`.
- O comando padrão para subir o ambiente é sempre:
  - `bash dev.sh`
- Se houver mudança de Dockerfile, imagem base ou dependência de sistema, usar:
  - `bash dev.sh --build`

## 2: Regra para Adicionar Dependências JavaScript/TypeScript
- **Proibido** instalar dependências com `npm install` no host para "resolver rápido".
- Como o compose usa volume em `/app/node_modules`, a instalação deve ocorrer no container `app`.
- Com o ambiente já rodando, instalar assim:
  - Dependência de produção: `docker compose -f .docker/compose.yaml exec app npm install <pacote>`
  - Dependência de desenvolvimento: `docker compose -f .docker/compose.yaml exec app npm install -D <pacote>`
- Após instalar, validar que `package.json` e `package-lock.json` foram atualizados.

## 3: Regra para Dependências Python
- Dependências Python devem ser gerenciadas no container `backend`.
- Para instalar pacote temporário de desenvolvimento:
  - `docker compose -f .docker/compose.yaml exec backend uv pip install --system <pacote>`
- Se a mudança for permanente, atualizar também o mecanismo de build do Python em `.docker/Dockerfile.python` (ou arquivo de dependências oficial do projeto, quando existir).

## 4: Sequência Operacional Correta
1. Subir ambiente: `bash dev.sh`
2. Instalar dependência no container correto (`app` ou `backend`)
3. Validar execução da aplicação
4. Se necessário, reconstruir: `bash dev.sh --build`

## 5: Comandos Proibidos Neste Projeto
- `npm install <pacote>` no host para corrigir erro de runtime do container.
- `docker compose up` sem `-f .docker/compose.yaml` (evita usar compose errado).
- Ignorar `dev.sh` para fluxo normal de desenvolvimento.

## 6: Diagnóstico Rápido de Erros Comuns
- Erro "módulo não encontrado" no app:
  - Dependência foi instalada no lugar errado; reinstalar via `exec app npm install ...`.
- Alterou Dockerfile e nada mudou:
  - Faltou rebuild; usar `bash dev.sh --build`.
