# 🐳 Guia de Manutenção Docker (Sem Susto)

> Manual rápido para limpar, resetar e manter seu ambiente Docker saudável.

---

## 🎯 Quando usar este guia?

Use quando acontecer algo como:

- ❌ containers quebrados ou com comportamento estranho
- ❌ erro de dependências mesmo após rebuild
- ❌ imagem muito pesada sem motivo claro
- ❌ banco local "sujo" para testes
- ❌ necessidade de começar do absoluto zero

---

## 🧹 Nível 1: Limpeza só do projeto (recomendado primeiro)

Este comando remove **containers, imagens e volumes** apenas do `compose` deste projeto:

```bash
docker compose -f .docker/compose.yaml down --rmi all -v --remove-orphans
```

Depois, suba novamente:

```bash
bash dev.sh --build
```

✅ Ideal para resolver 80% dos problemas sem afetar outros projetos.

---

## 💥 Nível 2: Reset total do Docker na máquina

> ⚠️ Atenção: isso apaga recursos de **todos os projetos** Docker da máquina.

### 1) Parar todos os containers

```bash
docker ps -aq | xargs -r docker stop
```

### 2) Limpar sistema inteiro (imagens, containers, volumes, redes sem uso)

```bash
docker system prune -a --volumes -f
```

### 3) Limpar cache de build (builder)

```bash
docker builder prune -a -f
```

### 4) (Windows/WSL) Reiniciar o subsistema Linux

```bash
wsl --shutdown
```

✅ Resultado esperado: Docker fica praticamente como recém-instalado.

---

## 🔎 Comandos de diagnóstico úteis

### Ver tamanho das imagens

```bash
docker images
```

### Ver uso de espaço detalhado

```bash
docker system df
```

### Ver containers ativos

```bash
docker ps
```

### Ver logs do projeto

```bash
docker compose -f .docker/compose.yaml logs -f
```

---

## 🧠 Boas práticas para evitar sujeira

- ✅ Sempre subir com `bash dev.sh`
- ✅ Quando mudar Dockerfile/dependências de sistema: `bash dev.sh --build`
- ✅ Limpar projeto com `down --rmi all -v` antes de reset total
- ✅ Revisar periodicamente `docker system df`

---

## 🚨 Checklist rápido de recuperação

1. Rodar limpeza do projeto
2. Subir com `bash dev.sh --build`
3. Se persistir, executar reset total
4. Subir o projeto novamente

---

Feito com foco em produtividade e zero dor de cabeça. ✨
