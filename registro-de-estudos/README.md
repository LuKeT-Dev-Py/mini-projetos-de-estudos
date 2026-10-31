# Registro de estudos

Aplicação de terminal para registrar assunto e duração das sessões de estudo e consultar o tempo total. Desenvolvida por João Antônio na prática de programação de 05 a 09/10/2026.

## O que faz

- Cadastra sessões com assunto preenchido e duração inteira maior que zero.
- Lista os registros e soma os minutos.
- Mostra uma mensagem de lista vazia e total de `0 min`.
- Solicita nova tentativa para entradas inválidas.

## Como executar

Requer Python 3.10 ou superior, sem dependências externas. Execução verificada com Python 3.12.14.

A partir da raiz do repositório:

```bash
cd registro-de-estudos
python3 main.py
```

No Windows, dentro da mesma pasta: `py main.py` ou `python main.py`.

| Opção | Ação |
| --- | --- |
| `1` | Cadastrar uma sessão |
| `2` | Listar sessões e mostrar o total |
| `0` | Sair |

## Exemplo

1. Cadastre `Python` por `20` minutos.
2. Cadastre `Revisão de funções` por `15` minutos.
3. Escolha `2`:

```text
Python: 20 min
Revisão de funções: 15 min
Total estudado: 35 min
```

Escolha `0` para encerrar. Você pode cadastrar outras sessões antes de sair; a quantidade não é limitada a dois registros.

## Código e aprendizado

| Arquivo | Responsabilidade |
| --- | --- |
| [main.py](main.py) | Menu e lista de sessões. |
| [Modulos/sessao.py](Modulos/sessao.py) | Cadastro, validações, listagem e soma dos minutos. |
| [Modulos/__init__.py](Modulos/__init__.py) | Identificação do pacote. |

`cadastrar_sessao()` retorna um dicionário que o principal adiciona à lista com `.append()`. `listar_sessoes(sessoes)` recebe essa lista e apresenta os registros e o total.

O projeto pratica funções, parâmetros, retorno, módulos, listas e dicionários, condicionais, laços, acumulador, métodos de string e tratamento de `ValueError`.

## Verificação e limites

O exemplo de duas sessões e total de 35 minutos foi conferido em Python 3.12.14. O [registro de verificação](VERIFICACAO.md) documenta também lista vazia, terceiro registro e entradas inválidas.

Os registros ficam apenas em memória e desaparecem ao encerrar. Edição, exclusão, filtro por assunto e salvamento em arquivo são possibilidades de evolução.
