# Supabase Learning & Implementation Log 📘

Este documento registra todo o processo de aprendizado, configuração e decisões tomadas durante a implementação do Supabase no projeto **Sem Susto**.

> **Objetivo Crítico:** Implementar banco de produção seguro, performático e **SEM CUSTOS SURPRESA** (Free Tier Only).

---

## 1. Princípios de Segurança e Custos 🛡️💸

### 💰 Proteção Contra Cobranças (Spend Cap)
O maior medo é a fatura de R$ 100k. Para evitar isso:
1.  **Plano Free Tier:** Manter-se estritamente nos limites (500MB database, 5GB bandwidth).
2.  **Spend Cap (Limite de Gastos):** O Supabase tem um "Spend Cap" ativado por padrão no plano Free. Isso significa que se excedermos o limite, **o serviço para**, mas não cobra.
    *   *Ação:* Verificar explicitamente se o Spend Cap está ATIVO no painel.
3.  **Monitoramento:** Configurar alertas de uso (se possível via dashboard).

### 🔐 Segurança (Row Level Security - RLS)
O Supabase expõe o banco via API. Sem RLS, **qualquer um pode ler/escrever tudo**.
1.  **Regra de Ouro:** NENHUMA tabela pública sem RLS ativado.
2.  **Política Inicial (Leitura):** Public (`anon`) pode ler `produtos`.
3.  **Política Inicial (Escrita):** Apenas `service_role` (backend) ou Admin pode escrever.
4.  **Chaves de API:**
    *   `ANON_KEY`: Pode ir para o frontend (com RLS configurado).
    *   `SERVICE_ROLE_KEY`: **JAMAIS** expor no frontend. Apenas variáveis de ambiente do servidor (`.env.local` e Vercel).

---

## 2. Checklist de Implementação 🚀

### A. Configuração do Projeto
- [ ] Criar conta/organização no Supabase.
- [ ] Criar projeto na região **São Paulo (sa-east-1)** (Melhor latência).
- [ ] Guardar credenciais (`Project URL`, `Anon Key`, `Service Role Key`, `Database Password`) no gerenciador de senhas.

### B. Banco de Dados
- [ ] Rodar migrations SQL existentes (estrutura idêntica ao dev local).
- [ ] Verificar se tabelas criadas estão com RLS habilitado por padrão.
- [ ] Importar dataset `produtos` (30k itens).

### C. Integração Aplicação
- [ ] Instalar SDK: `npm install @supabase/supabase-js`.
- [ ] Configurar `RepositorioProdutosSupabase.ts`.
- [ ] Testar conexão.

---

## 3. Diário de Bordo (Log) 📝

### [Data Atual] - Início
*   Documento criado.
*   Definido foco em **Spend Cap** e **RLS**.

---

## 4. Casos de Estudo e Prevenção (Security Hardening) 🛡️

### O Caso "OpenClaw" e Vazamento de Chaves
Usuários relataram incidentes (como no caso OpenClaw/OpenAI wrappers) onde chaves de API com permissões de administração total foram expostas por erro simples:
1.  **Erro:** Commitar chaves no GitHub ou expô-las no Client-Side.
2.  **Consequência:** Atacantes usaram as chaves para consumir cotas (R$ 100k+) ou roubar dados.
3.  **No nosso contexto:** Expor a `SERVICE_ROLE_KEY` no frontend permitiria que qualquer um apagasse nosso banco inteiro ("Bypass RLS").

### 🚫 Os 3 Pecados Capitais do Supabase
Para não acordarmos com uma dívida de 100k, **JAMAIS** faremos isso:

1.  **Service Role no Frontend:**
    *   *Errado:* `import { createClient } from '@supabase/supabase-js'; const supabase = createClient(url, SERVICE_KEY);`
    *   *Certo:* Apenas `ANON_KEY` no frontend. `SERVICE_ROLE` morre no servidor (`.env.local` não commitado).

2.  **RLS Desativado (O "Portão Aberto"):**
    *   Mesmo com `ANON_KEY`, se o RLS estiver *OFF* ou mal configurado, qualquer um lê tudo.
    *   *Regra:* Toda tabela deve ter RLS habilitado (`ALTER TABLE produtos ENABLE ROW LEVEL SECURITY;`).

3.  **Políticas RLS "Permissivas Demais":**
    *   *Perigoso:* `CREATE POLICY "Public Access" ON produtos FOR ALL USING (true);` (Permite Delete/Update para qualquer um).
    *   *Seguro:* `For SELECT USING (true)` (Apenas leitura). Escrita só para Admin.

### ✅ Checklist de Blindagem (Antes do Deploy)
- [ ] **Lint de Secrets:** Verificar se não há chaves hardcoded no código (`git grep "eyJ"`).
- [ ] **RLS Audit:** Rodar script verificando se todas as tabelas têm RLS ativo.
- [ ] **Network Restrictions:** Se possível, restringir acesso ao banco apenas aos IPs da Vercel (Supabase Pro, mas bom saber).
- [ ] **Backup:** Garantir que o script de seed local (`produtos_higienizados.json`) seja nossa fonte de verdade e backup frio.

---

## 5. Glossário Rápido
*   **GTIN:** Global Trade Item Number (Código de Barras).
*   **RLS:** Row Level Security (Segurança a nível de linha no Postgres).
*   **PITR:** Point in Time Recovery (Backup - geralmente pago, não teremos no free).
