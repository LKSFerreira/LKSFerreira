---
trigger: always_on
---

# Regras Específicas para Python

Este arquivo define todas as regras específicas para projetos Python.

## 1. Ambiente Virtual e Execução (Windows/Git Bash)

O projeto roda em Windows utilizando Git Bash. Você deve usar **exclusivamente** os executáveis do ambiente virtual `.venv`.

**Regras de Caminho e Execução:**
*   Use barras normais (`/`) nos caminhos.
*   **Python**: Use sempre `.venv/Scripts/python.exe`
*   **Pip**: Use sempre `.venv/Scripts/pip.exe`
*   **Pytest**: Use sempre `.venv/Scripts/pytest.exe`

**Gerenciamento de Dependências:**
*   Nunca use apenas `pip install`.
*   Bibliotecas de Produção: Instale e adicione ao `requirements.txt`.
*   Bibliotecas de Desenvolvimento: Instale e adicione ao `requirements-dev.txt`.
*   *Atenção*: Comandos de instalação (`pip install`) devem ter `SafeToAutoRun: false`.

**Exemplos de Comandos Corretos:**

```bash
    # Executar script
    .venv/Scripts/python.exe main.py

    # Instalar dependência
    .venv/Scripts/pip.exe install psutil

    # Rodar testes
    .venv/Scripts/pytest.exe tests/ -v
```

## 1.1 Ambiente Dev Container (Docker)

Quando executando dentro de um Dev Container, **NÃO** use ambiente virtual. O container já fornece isolamento.

**Regras de Execução no Dev Container:**
*   **Python**: Use `python` ou `python3`
*   **Pip**: Use `pip` ou `pip3`
*   **Pytest**: Use `pytest`

**Exemplos de Comandos no Dev Container:**

```bash
    # Executar script
    python main.py

    # Instalar dependência
    pip install psutil

    # Rodar testes
    pytest tests/ -v
```

> **Como identificar?** Se o terminal estiver dentro do container (indicado pelo VS Code), use os comandos do Dev Container.

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
