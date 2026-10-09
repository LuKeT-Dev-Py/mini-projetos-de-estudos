# Registro de Estudos

Programa de terminal em Python para registrar o assunto e a duração das sessões de estudo e consultar o tempo total estudado.

Desenvolvido por João Antônio (LuKeT-Dev-Py) na prática semanal de programação de 05 a 09/10/2026.

## Funcionalidades implementadas

- Menu com as opções `1` cadastrar, `2` listar e mostrar total e `0` sair.
- Cadastro de uma sessão por escolha, sem limite fixo de dois registros.
- Assunto validado após remover espaços nas extremidades.
- Duração validada como número inteiro maior que zero.
- Nova tentativa quando uma entrada é inválida.
- Listagem com duração em minutos e soma do total.
- Mensagem para lista vazia e total de `0 min`.

## Conhecimentos aplicados

Listas, dicionários, funções, parâmetros, retorno, módulos, imports, condicionais, laços, acumulador, tratamento de `ValueError` e métodos de string.

`cadastrar_sessao()` retorna um novo dicionário. O programa principal o adiciona à lista com `.append()`. `listar_sessoes(sessoes)` recebe a lista e apresenta os registros e o total.

## Execução

Requer Python 3.10 ou superior. Não há dependências externas.

Na pasta que contém `main.py`, execute:

```bash
python3 main.py
```

No Windows, também pode usar `py main.py`.

Os arquivos do programa são `main.py` e `Modulos/sessao.py`. `Modulos/__init__.py` identifica o pacote.

## Exemplo de uso

1. Escolha `1` e registre `Python` por `20` minutos.
2. Escolha `1` e registre `Revisão de funções` por `15` minutos.
3. Escolha `2`. A listagem inclui:

```text
Python: 20 min
Revisão de funções: 15 min
Total estudado: 35 min
```

4. Escolha `0` para encerrar.

## Verificação

O cadastro, as validações, a lista vazia, os totais, o terceiro registro e as opções inválidas foram conferidos por execução. Veja `VERIFICACAO.md`.

## Limitações atuais

- Os registros ficam apenas na memória e desaparecem ao encerrar o programa.
- Não há edição ou exclusão de sessões.
- A interface funciona no terminal.

## Próximos passos

Possíveis melhorias: editar sessões, filtrar por assunto e salvar/carregar registros após estudar arquivos. Essas funcionalidades ainda não estão implementadas.

