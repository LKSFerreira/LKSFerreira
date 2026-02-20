# ==========================================
# ESTÁGIO 1: BASE E DEPENDÊNCIAS (CACHE)
# ==========================================
FROM golang:1.22-alpine AS base

LABEL maintainer="Ambiente go"
LABEL description="Ambiente de desenvolvimento Go"

WORKDIR /app

# Instala dependências do sistema necessárias para o Go
RUN apk add --no-cache git build-base

# Copia os arquivos de dependência PRIMEIRO para aproveitar o cache do Docker
# Descomente e ajuste conforme o projeto usa go mod
# COPY go.mod go.sum ./
# RUN go mod download

# ==========================================
# ESTÁGIO 2: DESENVOLVIMENTO (DevContainer)
# ==========================================
FROM base AS dev

# Instala ferramentas úteis para desenvolvimento, como o reflex para hot-reload
RUN go install github.com/cespare/reflex@latest

EXPOSE 8080

# Comando para manter o container rodando e reagindo a mudanças (hot-reload)
# O código real será injetado via Bind Mount do compose.yaml
CMD ["sh", "-c", "reflex -r '\\.go$' -s -- sh -c 'go run ./'"]

# ==========================================
# ESTÁGIO 3: PRODUÇÃO (Deploy)
# ==========================================
FROM base AS prod

# Aqui copiamos o código para dentro da imagem
COPY . .

# Faz o build da aplicação
RUN go build -o main .

EXPOSE 8080

CMD ["./main"]
