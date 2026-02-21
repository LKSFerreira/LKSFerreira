# ==========================================
# ESTÁGIO 1: BASE E DEPENDÊNCIAS (CACHE)
# ==========================================
FROM alpine:latest AS base

LABEL maintainer="Ambiente c++"
LABEL description="Ambiente de desenvolvimento C++"

WORKDIR /app

# Instala compiladores e ferramentas de build
RUN apk add --no-cache g++ gcc make cmake gdb musl-dev

# ==========================================
# ESTÁGIO 2: DESENVOLVIMENTO (Docker)
# ==========================================
FROM base AS dev

# Aqui NÃO copiamos o código. Ele vem pelo Bind Mount (volumes do compose.yaml).
# Mantém o container vivo para a IDE.
CMD ["tail", "-f", "/dev/null"]

# ==========================================
# ESTÁGIO 3: PRODUÇÃO (Deploy)
# ==========================================
FROM base AS prod

# Aqui aplicamos a Etapa 2 da "dica de ouro": copiamos o código final.
COPY . .

# Comando de compilação hipotético
# RUN cmake . && make

# Executável gerado
CMD ["./app"]
