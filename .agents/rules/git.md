---
trigger: always_on
description: Padrões de commit e pull request do projeto.
---

# Regras de Git (Commit e PR)

## 1: Política de execução
- Só executar commit/push quando o usuário pedir explicitamente.
- Proibido usar `git add .` ou equivalentes amplos sem necessidade.

## 2: Padrão de mensagem de commit
- Use apenas código de emoji em texto (`:sparkles:`, `:bug:`), sem emoji unicode.
- Formato obrigatório:
  - `:emoji_code: tipo: descrição sucinta`
- Referências técnicas (arquivo, função, rota, variável) devem estar entre crases.
- Idioma: manter consistência em pt-BR.

## 3: Tabela de tipos
- `:tada:` `init`
- `:books:` `docs`
- `:bug:` `fix`
- `:sparkles:` `feat`
- `:bricks:` `ci`
- `:recycle:` `refactor`
- `:zap:` `perf`
- `:boom:` `breaking`
- `:lipstick:` `feat`
- `:test_tube:` `test`
- `:bulb:` `docs`
- `:card_file_box:` `data`
- `:broom:` `cleanup`
- `:wastebasket:` `remove`

## 4: Template obrigatório de commit

Use exatamente este molde:

```txt
:emoji_code: tipo: descrição objetiva referenciando `arquivo`, `função` ou `rota`
```

### Exemplo completo 1 (commit)

```txt
:bug: fix: corrige validação do campo `ean` em `components/ModalScannerBarras.tsx`
```

### Exemplo completo 2 (commit)

```txt
:bricks: ci: ajusta build do serviço `backend` no `.docker/compose.yaml`
```

## 5: Regras de corpo de PR
- Nunca usar caminhos absolutos ou protocolos `file:///`, `vscode://` ou equivalentes.
- Sempre usar links markdown com caminho relativo: `[arquivo](caminho/relativo)`.
- Não usar links markdown aninhados.
- O texto do PR deve ser objetivo, verificável e baseado no diff real.

## 6: Template obrigatório de PR

Use exatamente esta estrutura:

```md
# [tipo] Título do PR

## Visão geral
- Problema:
- Objetivo:
- Abordagem:

## Alterações realizadas
- [arquivo](caminho/relativo): descrição objetiva da mudança.
- [arquivo](caminho/relativo): descrição objetiva da mudança.

## Como validar
1. Comando de setup.
2. Comando de execução.
3. Comando de teste/checagem.

## Riscos e impactos
- Risco principal:
- Mitigação:
- Pendências:
```

### Exemplo completo 1 (PR)

```md
# [fix] Corrige leitura de código de barras no modal

## Visão geral
- Problema: leitura de EAN com caracteres extras quebrava o fluxo de busca.
- Objetivo: normalizar entrada e impedir erro de validação no scanner.
- Abordagem: sanitização antes da validação e ajuste de mensagens de erro.

## Alterações realizadas
- [components/ModalScannerBarras.tsx](components/ModalScannerBarras.tsx): normaliza valor lido antes de validar tamanho e formato.
- [services/buscaProdutoService.ts](services/buscaProdutoService.ts): adiciona proteção para EAN inválido sem disparar requisição.

## Como validar
1. `bash dev.sh`
2. Abrir modal de scanner e testar EAN com espaços e hífens.
3. Verificar que somente EAN válido dispara busca e que erro amigável é exibido.

## Riscos e impactos
- Risco principal: bloquear algum formato de entrada aceito anteriormente.
- Mitigação: manter sanitização mínima e teste manual com casos antigos.
- Pendências: criar teste automatizado para cenários de EAN inválido.
```

### Exemplo completo 2 (PR)

```md
# [ci] Otimiza imagem Python e padroniza serviço backend

## Visão geral
- Problema: imagem Python estava grande e o serviço `processor` tinha nome pouco claro.
- Objetivo: reduzir tamanho da imagem e padronizar nomenclatura para `backend`.
- Abordagem: atualizar Dockerfile Python para `uv` e renomear serviço no compose e scripts.

## Alterações realizadas
- [.docker/Dockerfile.python](.docker/Dockerfile.python): troca base para `python:3.12-slim` e instala dependências via `uv pip`.
- [.docker/compose.yaml](.docker/compose.yaml): renomeia serviço `processor` para `backend`.
- [premium.sh](premium.sh): ajusta `docker compose exec` para usar o serviço `backend`.

## Como validar
1. `docker compose -f .docker/compose.yaml down --rmi all -v --remove-orphans`
2. `bash dev.sh --build`
3. `bash premium.sh trial` e validar geração de token sem erro.

## Riscos e impactos
- Risco principal: scripts antigos ainda referenciando `processor`.
- Mitigação: busca global e atualização de todas as referências.
- Pendências: revisar documentação externa fora do repositório, se existir.
```
