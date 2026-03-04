---
trigger: model_decision
description: Regras para Python, gerenciamento com uv, tipagem moderna e docstrings RST.
---

# Regras Específicas para Python:

Este arquivo define todas as regras específicas para projetos Python.

## 1: Gerenciamento de Dependências com `uv`

Este projeto adotou o **uv** (Astral) como gerenciador de pacotes e ambientes padrão.

**Regras de Execução:**

- Use EXCLUSIVAMENTE o `uv` para tudo relacionado a pacotes, ambientes virtuais e execução.
- **NUNCA** use `pip`, `virtualenv` ou `poetry` diretamente.
- **Não** edite o `pyproject.toml` manualmente para adicionar dependências.

**Comandos Padrão:**

```bash
# Adicionar lib de produção
uv add numpy

# Adicionar lib de desenvolvimento
uv add --dev pytest

# Rodar script
uv run main.py

# Rodar testes
uv run pytest
```

## 1.1: Ambiente Dev Container:

No Docker, o `uv` já está configurado. O Dockerfile cuida da instalação inicial (`uv sync`).

**Comandos no Container:**

```bash
# Se precisar adicionar algo rápido (mas idealmente use uv add fora e rebuilde)
uv add pacote
```

## 2: Padrão de Código e Tipagem (Type Hints)

- **Tipagem Moderna (Python 3.10+)**: Use os tipos nativos (`list`, `dict`, `tuple`) em vez de importá-los do módulo `typing`.
- **Uniões**: Use o operador `|` (ex: `str | None` em vez de `Optional`).
- **Linting/Formatação**: Siga o padrão PEP 8. Assuma o uso do **Ruff** (também da Astral) para formatação e linting, caso precise sugerir correções de estilo.

## 3: Padrão de Documentação (Docstrings)

O agente deve seguir estritamente o formato **ReStructuredText (RST)** padrão Sphinx.

**Estrutura Obrigatória:**

1. **Resumo**: O que o método/classe faz.
2. **Detalhamento (Opcional)**: Regras de negócio e validações.
3. **Exemplo**: Bloco de código funcional (`.. code-block:: python`).
4. **Notas (Opcional)**: Avisos (`.. note::`).
5. **Typing**: Uso obrigatório de _Type Hints_ nos argumentos e retorno.

**Template Canônico (Referência Absoluta):**

```python
from typing import Any

class GerenciadorUsuarios:
    """
    Gerencia operações de usuários com validações.

    Uma descrição detalhada e didática pode ser escrita aqui a fim de explicar o contexto,
    ou quaisquer outros pormenores que sejam necessários.

    **Exemplo:**

    .. code-block:: python

        gerenciador = GerenciadorUsuarios("MeuApp")
        usuario = gerenciador.criar_usuario("lucas@email.com", "Lucas", 25)
        print(usuario)  # Output: Lucas

    .. note::
       Esta classe não persiste dados. Use pickle ou JSON para salvar o estado.
    """

    def criar_usuario(
        self,
        email: str,
        nome: str,
        idade: int,
        tags: list | None = None
    ) -> dict:
        """
        Cria e valida um novo usuário no sistema.

        O email deve conter ``@`` e a idade estar entre 18 e 120 anos.

        **Exemplo:**

        .. code-block:: python

            usuario = gerenciador.criar_usuario(
                "joao@exemplo.com",
                "João Silva",
                30
            )
            print(usuario)  # Output: 1
        """
        # ... implementação ...
```

## 3.1: Comentários Didáticos Inline

Este repositório é de **ESTUDOS**. Além das docstrings, o código deve conter **comentários inline didáticos** que sirvam como material de aprendizado para quem lê.

**Regras:**

1. Toda instrução não-trivial deve ter um comentário `#` acima explicando **o que faz** e **por quê**.
2. Blocos lógicos (loops, condicionais, `try/except`) devem ter um comentário de abertura contextualizando o bloco inteiro.
3. Variáveis com nomes curtos ou técnicos devem ter um comentário ao lado explicando seu propósito.
4. Imports de bibliotecas externas devem ter um comentário rápido explicando para que servem.
5. Comentários em **pt-BR**, com linguagem acessível a iniciantes.
6. Comentários complementam as docstrings, **NÃO** as substituem.

**Exemplo Prático:**

```python
# json = biblioteca padrão para ler e escrever arquivos JSON
import json

# pathlib = forma moderna e segura de lidar com caminhos de arquivos
from pathlib import Path

def carregar_configuracao(caminho: str) -> dict:
    """
    Lê um arquivo JSON e retorna seu conteúdo como dicionário.

    :param caminho: Caminho do arquivo JSON.
    :return: Conteúdo do arquivo como dicionário Python.
    """
    # Converte a string do caminho em um objeto Path (mais seguro e portável)
    arquivo = Path(caminho)

    # Verifica se o arquivo realmente existe antes de tentar abrir,
    # evitando um FileNotFoundError inesperado
    if not arquivo.exists():
        # Retorna um dicionário vazio como fallback seguro
        return {}

    # Abre o arquivo em modo leitura com encoding UTF-8
    # O bloco 'with' garante que o arquivo será fechado automaticamente,
    # mesmo se ocorrer um erro durante a leitura
    with open(arquivo, "r", encoding="utf-8") as f:
        # json.load() lê o conteúdo do arquivo e converte de JSON para dict
        dados = json.load(f)

    return dados
```
