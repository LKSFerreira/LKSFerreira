# Integração Mercado Pago - Sem Susto 💳

Este documento serve como guia técnico para a implementação do sistema de pagamentos via PIX utilizando o SDK/API do Mercado Pago.

## 1. Arquitetura: Strategy Pattern

Para garantir que o app não fique "preso" a um único gateway, implementamos o padrão **Strategy**.

### Tipagem Genérica (`tipos.ts`)
```typescript
export type StatusPagamento = 'pendente' | 'aprovado' | 'falha' | 'expirado';

export interface RespostaCriacaoPagamento {
  pagamento_id: string;
  codigo_qr: string;
  codigo_copia_e_cola: string;
  status: StatusPagamento;
}

export interface ProvedorPagamento {
  gerarPix(plano_id: string): Promise<RespostaCriacaoPagamento>;
  consultarStatus(pagamento_id: string): Promise<StatusPagamento>;
}
```

> [!IMPORTANT]
> O provedor deve traduzir os status específicos do gateway (ex: `approved`) para o enum `StatusPagamento` da aplicação, evitando vazamento de abstração.

## 2. Fluxo de Implementação (Mercado Pago)

### Passo 1: Credenciais
As chaves devem ser configuradas no `.env.local`:
- `VITE_MP_PUBLIC_KEY`: Localizada no Dashboard do Mercado Pago (Credenciais de Produção/Teste).
- `MP_ACCESS_TOKEN`: Token de acesso para chamadas de API (Server-side/Vercel Proxy).

### Passo 2: Endpoint `/api/pagamentos/pix` (Serverless Function)
Devido a restrições de CORS e segurança, a criação do pagamento deve ocorrer via Vercel Function:
1. Recebe o plano (Café, Lanche, etc).
2. Valida o valor conforme `monetizacao.md`.
3. Chama `POST https://api.mercadopago.com/v1/payments`.
4. Retorna QR Code e ID do pagamento para o frontend.

### Passo 3: Polling Seguro no Frontend
O frontend utilizará `setInterval` com regras estritas de parada:
1. **Unmount:** Limpar intervalo ao desmontar modal.
2. **Timeout:** Cessar requisições após 15 minutos (tempo de expiração do PIX).
3. **Status Final:** Parar polling ao receber `aprovado`, `falha` ou `expirado`.

```typescript
useEffect(() => {
  if (!pagamento_id) return;
  const timeout_limite = Date.now() + 15 * 60 * 1000; // 15 min

  const interval = setInterval(async () => {
    if (Date.now() > timeout_limite) {
      clearInterval(interval);
      setErro('Tempo esgotado');
      return;
    }
    const status = await servico.consultarStatus(pagamento_id);
    if (status !== 'pendente') clearInterval(interval);
    processarNovoStatus(status);
  }, 5000);

  return () => clearInterval(interval);
}, [pagamento_id]);
```

## 3. Segurança e Boas Práticas
- **Sandbox:** Durante o desenvolvimento, utilize usuários de teste do Mercado Pago.
- **Validação de Valor:** Nunca confie no valor enviado pelo frontend; o backend deve ter uma tabela de preços fixa associada aos nomes dos planos.
- **Idempotência:** Utilize a chave de idempotência na API do MP para evitar cobranças duplicadas em caso de retry.

## 4. Referências
- [Documentação Oficial PIX Mercado Pago](https://www.mercadopago.com.br/developers/pt/docs/checkout-api/integration-configuration/pix)
- [SDK JS (Frontend)](https://www.mercadopago.com.br/developers/pt/docs/checkout-api/integration-configuration/billing-details)
