# ==========================================
# ESTÁGIO 1: BASE E DEPENDÊNCIAS (CACHE)
# ==========================================
FROM eclipse-temurin:21-jdk-alpine AS base

LABEL maintainer="Ambiente java spring boot"
LABEL description="Ambiente de desenvolvimento Java com Spring Boot"

WORKDIR /app

# Adicione pacotes base necessários

# ==========================================
# ESTÁGIO 2: DESENVOLVIMENTO (Docker)
# ==========================================
FROM base AS dev

EXPOSE 8080

# O código é provido via Bind Mount, o spring-boot run cuida do reload (spring-boot-devtools)
CMD ["sh", "-c", "./mvnw spring-boot:run -Dspring-boot.run.jvmArguments='-Dspring.devtools.restart.enabled=true'"]

# ==========================================
# ESTÁGIO 3: PRODUÇÃO (Deploy)
# ==========================================
FROM base AS prod

COPY . .

# Comando de build de produção 
RUN ./mvnw clean package -DskipTests

EXPOSE 8080

CMD ["java", "-jar", "target/app.jar"]
