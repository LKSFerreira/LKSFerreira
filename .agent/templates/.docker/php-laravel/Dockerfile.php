# ==========================================
# ESTÁGIO 1: BASE E DEPENDÊNCIAS (CACHE)
# ==========================================
FROM php:8.2-fpm-alpine AS base

LABEL maintainer="Ambiente php laravel"
LABEL description="Ambiente de desenvolvimento PHP para Laravel"

WORKDIR /var/www/html

# Instala dependências do sistema e do PHP
RUN apk add --no-cache \
    curl \
    libpng-dev \
    libxml2-dev \
    zip \
    unzip \
    oniguruma-dev \
    postgresql-dev \
    && docker-php-ext-install pdo_pgsql mbstring exif pcntl bcmath gd \
    && apk add --no-cache pcre-dev $PHPIZE_DEPS \
    && pecl install redis \
    && docker-php-ext-enable redis

# Instala Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# ==========================================
# ESTÁGIO 2: DESENVOLVIMENTO (Docker)
# ==========================================
FROM base AS dev

EXPOSE 8000

# Como o código vem via Bind Mount, apenas rodamos o artisan serve
CMD ["php", "artisan", "serve", "--host=0.0.0.0", "--port=8000"]

# ==========================================
# ESTÁGIO 3: PRODUÇÃO (Deploy)
# ==========================================
FROM base AS prod

# Copia o código para dentro da imagem
COPY . .

# Comando de produção (ajuste se usar Nginx ou apenas o artisan)
CMD ["php", "artisan", "serve", "--host=0.0.0.0", "--port=8000"]
