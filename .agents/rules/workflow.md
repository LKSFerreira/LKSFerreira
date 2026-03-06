---
trigger: always_on
---

# Fluxo de Trabalho Obrigatório:

> **ESTA REGRA É INVIOLÁVEL.**
> Nenhuma linha de código ou modificação de arquivo pode ser iniciada sem passar estritamente por todas as etapas abaixo, na ordem exata.

## Etapas de Execução:

### 1: Análise (Discovery)
- Estude o contexto, os requisitos e o impacto da mudança solicitada.
- Vasculhe o projeto: leia os arquivos relevantes, a documentação existente em `.metadocs/` e as regras de negócio.
- **Ação:** Formule mentalmente (ou no bloco `<thinking>`) o problema raiz.

### 2: Discussão (Debate)
- Apresente a sua análise técnica ao usuário de forma clara e direta.
- Discuta alternativas, *trade-offs* (prós e contras) e decisões de arquitetura.
- Tire dúvidas, aponte possíveis gargalos (edge cases) e alinhe as expectativas.
- **Ação:** Aguarde o feedback do usuário.

### 3: Refinamento (Ajuste)
- Incorpore o feedback recebido.
- Ajuste a proposta técnica até que ambos (Agente e Usuário) estejam 100% alinhados.
- Se a decisão mudar a arquitetura do sistema, documente essa decisão nos arquivos da pasta `.metadocs/`.

### 4: Aprovação (Gatekeeper)
- Crie um plano de implementação detalhado (passo a passo do que será alterado).
- **PARE E AGUARDE a aprovação explícita do usuário** antes de executar qualquer comando ou escrever qualquer código.
- Sem aprovação = Sem código.

### 5: Execução (Code)
- Implemente **SOMENTE** o que foi aprovado no plano.
- Siga o plano à risca. Se durante a execução você encontrar um bloqueio não previsto, pare a execução e retorne à etapa 2 (Discussão). Desvios não autorizados são proibidos.

---

## Regra de Ouro:

```text
PROIBIDO: Analisar → Implementar
CORRETO:  Analisar → Discutir → Refinar → Aprovar → Implementar
```
