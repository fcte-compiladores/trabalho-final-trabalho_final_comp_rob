# Compilador C para Python

Este projeto é um compilador simples que traduz um subconjunto da linguagem C para Python. Ele foi desenvolvido utilizando PLY (Python Lex-Yacc) para análise léxica e sintática, e um gerador de código que converte a AST em código Python equivalente.

## Funcionalidades
- Suporte a declaração de variáveis, arrays e structs
- Controle de fluxo: `if`, `else`, `while`, `for`, `do-while`
- Operadores aritméticos, relacionais, lógicos e de atribuição composta (`+=`, `-=`, etc.)
- Funções e parâmetros
- Entrada e saída: `printf` e `scanf`
- Geração de código Python a partir da AST
- Testes unitários e integrados com pytest

## Instalação
1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd trabalho-compilador
   ```
2. Instale as dependências (recomenda-se usar um ambiente virtual):
   ```bash
   pip install -r requirements.txt
   ```
   Ou, se estiver usando o [uv](https://github.com/astral-sh/uv):
   ```bash
   uv pip install -r requirements.txt
   ```

## Como usar
Para compilar um arquivo C e gerar o código Python correspondente:

```bash
python main.py caminho/para/arquivo.c
```
O código Python será salvo no mesmo diretório, com o mesmo nome e extensão `.py`.

Exemplo:
```bash
python main.py exemplos/exemplo.c
# Gera exemplos/exemplo.py
```

## Rodando os testes
Para executar todos os testes automatizados:

```bash
pytest -v
```
Ou, se estiver usando o uv:
```bash
uv run pytest -v
```

## Estrutura do Projeto
- `main.py` — Script principal para compilar arquivos C para Python
- `src/lexer.py` — Analisador léxico (tokens)
- `src/parser.py` — Analisador sintático (gramática)
- `src/ast_nodes.py` — Definições dos nós da AST
- `src/code_generator.py` — Geração de código Python a partir da AST
- `tests/` — Testes unitários e integrados

## Observações
- O compilador suporta apenas um subconjunto da linguagem C, focado em estruturas e comandos mais comuns.
- O código gerado em Python busca ser funcionalmente equivalente ao original em C, mas pode não ser idêntico em todos os detalhes.

---
Desenvolvido para fins didáticos. 