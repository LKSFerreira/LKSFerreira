# ==========================================
# ESTÁGIO 1: BASE E DEPENDÊNCIAS (CACHE)
# ==========================================
FROM eclipse-temurin:21-jdk-alpine AS base

LABEL maintainer="Ambiente java"
LABEL description="Ambiente de desenvolvimento puro Java"

WORKDIR /app

# Dependências úteis para build/dev
RUN apk add --no-cache maven gradle bash bind-tools

# ==========================================
# ESTÁGIO 2: DESENVOLVIMENTO (DevContainer)
# ==========================================
FROM base AS dev

# Aqui NÃO copiamos o código. Ele vem pelo Bind Mount (volumes do compose.yaml).
# Mantém o container vivo para a IDE e aceita compilações interativas
CMD ["tail", "-f", "/dev/null"]

# ==========================================
# ESTÁGIO 3: PRODUÇÃO (Deploy)
# ==========================================
FROM base AS prod

# Aqui aplicamos a Etapa 2 da "dica de ouro": copiamos o código final.
COPY . .

# Comando de exemplo para compilar (ajuste conforme o projeto mude para Maven/Gradle)
# RUN javac Main.java

# Comando para executar a aplicação compilada
CMD ["java", "Main"]
