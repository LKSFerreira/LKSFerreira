# 02 — Funcionalidades da Extensão Codex

> 🔗 Fonte oficial: [developers.openai.com/codex/ide/features](https://developers.openai.com/codex/ide/features)
> ⬅️ [Extensão IDE](./01_extensao_ide.md) | ➡️ [Configurações](./03_configuracoes_ide.md)

---

## 📄 Documentação Oficial

### 1. Prompting com Contexto do Editor

O Codex usa os arquivos abertos e o código selecionado como contexto. Referencie qualquer arquivo com `@`:

```
Use @example.tsx como referência para adicionar uma nova página "Recursos"
que contenha a lista de recursos definida em @resources.ts
```

**Dica**: Quanto mais contexto você fornecer, menores e mais precisos podem ser seus prompts.

### 2. Troca de Modelos

Use o seletor abaixo do campo de chat para alternar entre modelos. Cada modelo tem pontos fortes diferentes (velocidade vs. profundidade).

### 3. Esforço de Raciocínio (Reasoning Effort)

Controle quanto tempo o Codex "pensa" antes de responder:

| Nível | Quando Usar | Observação |
|-------|------------|------------|
| `low` | Tarefas simples e rápidas | Respostas mais curtas, menos tokens |
| `medium` | Uso diário (padrão recomendado) | Bom equilíbrio entre velocidade e qualidade |
| `high` | Tarefas complexas, debugging profundo | Consome mais tokens e pode ser mais lento |

### 4. Modos de Aprovação

| Modo | O que o Codex pode fazer | Precisa de aprovação para... |
|------|--------------------------|------------------------------|
| **Chat** | Apenas conversa e planeja | Não faz alterações |
| **Agent** (padrão) | Ler/editar arquivos, rodar comandos no diretório atual | Acessar rede ou alterar fora do diretório |
| **Agent (Full Access)** | Tudo, incluindo rede e comandos sem restrição | **Nada — autonomia total** ⚠️ |

### 5. Delegação para a Nuvem (Cloud Delegation)

1. Configure um [ambiente cloud](https://chatgpt.com/codex/settings/environments)
2. Escolha o ambiente e selecione **"Run in the cloud"**
3. Opções:
   - **Run from main** → ideal para começar algo novo
   - **Run from local changes** → ideal para concluir uma tarefa em andamento

O Codex mantém o contexto da conversa ao delegar para a nuvem.

### 6. Acompanhamento de Tarefas Cloud (Cloud Follow-up)

Após executar na nuvem, você pode:
- Visualizar as mudanças diretamente na IDE
- Pedir ajustes que rodem novamente na nuvem
- Aplicar as mudanças localmente para testar

### 7. Pesquisa Web (Web Search)

O Codex tem pesquisa web integrada que funciona em dois modos:

| Modo | Comportamento |
|------|--------------|
| `cached` (padrão) | Usa um índice mantido pela OpenAI — resultados pré-indexados |
| `live` | Busca páginas em tempo real (padrão no modo Full Access) |
| `disabled` | Desativa a pesquisa |

Configuração via `~/.codex/config.toml`:
```toml
web_search = "cached"   # padrão
# web_search = "live"   # buscas em tempo real
# web_search = "disabled"
```

### 8. Arrastar e Soltar Imagens

Segure `Shift` enquanto solta uma imagem no campo de prompt para incluí-la como contexto visual.

---

## 🎯 Exemplos Práticos

### Usando raciocínio alto para debugging complexo

```
[Selecione reasoning: high]

Analise @useAuth.ts e trace o fluxo completo de autenticação.
Há um bug onde o token expira mas o refresh não é acionado.
Identifique a causa raiz e sugira a correção mínima.
```

### Usando modo Chat para planejamento

```
[Modo: Chat]

Preciso migrar nosso sistema de pagamento de Stripe para Mercado Pago.
Liste os passos necessários, possíveis breaking changes, e
estime o esforço de cada etapa.
```

### Delegando tarefa pesada para a nuvem

```
[Modo: Agent → Run in the cloud → from local changes]

Refatore todos os componentes em @components/ para usar
o novo design system definido em @design-tokens.ts.
Atualize os testes unitários correspondentes.
```

---

## 📖 Explicação Didática

### Por que existem 3 modos de aprovação?

É uma questão de **confiança progressiva**:

1. **Chat**: Você está apenas pedindo conselhos. O Codex não toca em nada.
2. **Agent**: O Codex age no seu código, mas dentro de limites seguros. Se ele precisar instalar algo da internet ou mexer fora da pasta do projeto, ele **para e pergunta**.
3. **Full Access**: O Codex faz tudo sem perguntar. Útil para tarefas que exigem acesso à rede (ex: instalar dependências), mas use com **extrema cautela**.

### Cloud Delegation — quando usar?

Use quando:
- A tarefa é **grande demais** para rodar enquanto você trabalha
- Precisa de **muitas mudanças em vários arquivos** ao mesmo tempo
- Quer **continuar trabalhando** na IDE enquanto o Codex processa

### Web Search — cache vs. live

O modo `cached` é mais seguro porque evita que o Codex seja influenciado por conteúdo malicioso em páginas web (prompt injection). O modo `live` é necessário quando você precisa de informações **muito recentes** (ex: documentação de uma API lançada ontem).

---

> ⬅️ [Extensão IDE](./01_extensao_ide.md) | ➡️ [Configurações](./03_configuracoes_ide.md)
