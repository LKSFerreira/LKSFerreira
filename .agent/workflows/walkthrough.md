---
description: Salva o artefato de walkthrough e atualiza o histórico de documentação.
---

# Workflow: Sincronização de Walkthrough e Histórico

> **Atenção:** Siga os passos abaixo com precisão absoluta para manter a integridade da documentação e não quebrar o padrão existente.

## 1. Captura e Salvamento do Artefato
- Extraia o conteúdo exato do artefato gerado chamado `walkthrough`.
- Salve este conteúdo como um novo arquivo dentro do diretório `.metadocs/walkthrough/`.

## 2. Regra de Nomenclatura
- O nome do novo arquivo deve ser representativo e conter **no máximo 3 palavras** (ex: `setup_banco_dados.md` ou `refatoracao_auth.md`).
- **Ação Obrigatória:** Analise os arquivos já existentes no diretório `.metadocs/walkthrough/` e utilize estritamente o mesmo padrão de nomenclatura (snake_case) que já está sendo usado.

## 3. Atualização do Histórico
- Abra e analise as últimas inserções do arquivo `historico.md` (localizado na raiz ou em `.metadocs/`).
- Crie um resumo do arquivo que você acabou de salvar na Etapa 1.
- **Ação Obrigatória:** Adicione esse resumo ao `historico.md` seguindo **exatamente** o mesmo padrão visual e de formatação das entradas anteriores. 
- ⚠️ **Trava de Segurança:** É estritamente obrigatório que o resumo contenha um link Markdown válido apontando para o novo arquivo criado (ex: `[Resumo da feature](.metadocs/walkthrough/nome_do_arquivo.md)`).
