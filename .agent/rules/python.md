---
trigger: always_on
---

# Regras Específicas para Python

Este arquivo define todas as regras específicas para projetos Python.

## 1. Gerenciamento de Dependências com `uv`

Este projeto adotou o **uv** (Astral) como gerenciador padrão.

**Regras de Execução:**
*   Use `uv` para tudo relacionado a pacotes e execução.
*   **Não** use `pip` ou `virtualenv` diretamente.
*   **Não** edite `pyproject.toml` manualmente para adicionar dependências.

**Comandos Padrão:**

```bash
    # Adicionar lib de produção
    uv add numpy

    # Adicionar lib de dev
    uv add --dev pytest

    # Rodar script
    uv run main.py

    # Rodar testes
    uv run pytest
```

## 1.1 Ambiente Dev Container

No Docker, o `uv` já está configurado.

**Comandos no Container:**
```bash
    # Se precisar adicionar algo rápido (mas idealmente use uv add fora e rebuilde)
    uv add pacote
```

> **Nota:** O Dockerfile cuida da instalação inicial (`uv sync`).

## 2. Padrão de Documentação (Docstrings)

O agente deve seguir estritamente o formato **ReStructuredText (RST)** padrão Sphinx.

**Estrutura Obrigatória:**
1.  **Resumo**: O que o método/classe faz.
2.  **Detalhamento (Opcional)**: Regras de negócio e validações.
3.  **Exemplo**: Bloco de código funcional (`.. code-block:: python`).
4.  **Notas (Opcional)**: Avisos (`.. note::`).
5.  **Typing**: Uso obrigatório de _Type Hints_ nos argumentos e retorno.

**Template Canônico (Referência Absoluta):**

```python
    from typing import List, Optional, Dict

    class GerenciadorUsuarios:
        """
        Gerencia operações de usuários com validações.

        Uma descrição detalhada e didática pode ser escrita aqui a fim de explicar o contexto,
        ou qualquer outros por menores que sejam necessários.
        
        **Exemplo:**
        
        .. code-block:: python
        
            gerenciador = GerenciadorUsuarios("MeuApp")
            usuario = gerenciador.criar_usuario("lucas@email.com", "Lucas", 25)
            print(usuario['nome'])  # Output: Lucas
        
        .. note::
           Esta classe não persiste dados. Use pickle ou JSON para salvar o estado.
        """
        
        def criar_usuario(
            self, 
            email: str, 
            nome: str, 
            idade: int,
            tags: Optional[List[str]] = None
        ) -> Dict[str, any]:
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
                print(usuario['id'])  # Output: 1
            """
            # ... implementação ...
```
