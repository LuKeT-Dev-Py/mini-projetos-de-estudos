# Quiz no terminal

Aplicação em Python com duas perguntas sobre a linguagem. Ao final, apresenta a pontuação e quantas entradas inválidas foram digitadas.

## O que faz

- Apresenta uma pergunta por vez, com alternativas `a`, `b` e `c`.
- Aceita maiúsculas e remove espaços nas extremidades.
- Pede nova tentativa quando a alternativa não existe.
- Avança após uma resposta válida, correta ou incorreta.
- Soma um ponto por acerto e reinicia os contadores a cada execução.

## Como executar

Requer Python 3, sem dependências externas. Execução verificada com Python 3.12.14.

A partir da raiz do repositório:

```bash
cd quiz-no-terminal
python3 main.py
```

No Windows, dentro da mesma pasta: `py main.py` ou `python main.py`.

## Exemplo

Digite `z` na primeira pergunta: o programa registra uma entrada inválida e pede outra tentativa. Em seguida, responda `b` e, na segunda pergunta, `a`:

```text
Pontuação: 2/2
Entradas inválidas: 1
```

Na primeira pergunta, `a` ou `c` são respostas válidas, mas incorretas: o programa segue sem somar pontos.

## Código e verificação

O código está em [main.py](main.py). O exercício pratica listas, entrada de dados, condicionais, laços, contadores e métodos de string.

O exemplo acima foi conferido por execução em Python 3.12.14. Os cenários já registrados no projeto são:

| Entradas, na ordem | Pontuação | Entradas inválidas |
| --- | --- | --- |
| `b`, `a` | 2/2 | 0 |
| `a`, `a` | 1/2 | 0 |
| `c`, `b` | 0/2 | 0 |
| Somente espaços, `z`, ` B `, `x`, ` A ` | 2/2 | 3 |

## Limitações

As duas perguntas estão fixas no código, e os resultados não são salvos. Não há uma suíte de testes automatizados incluída.
