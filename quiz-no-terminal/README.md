# Quiz no Terminal

## Objetivo

Praticar conceitos fundamentais de Python: listas, entrada de dados, condições, repetição e validação de entradas.

## Funcionalidades

- Apresenta duas perguntas, uma por vez, com alternativas.
- Remove espaços extras e aceita letras maiúsculas ou minúsculas.
- Solicita uma nova tentativa quando a alternativa não existe.
- Informa se uma resposta válida está correta ou incorreta.
- Soma um ponto por resposta correta.
- Exibe a pontuação final e a quantidade de entradas inválidas.
- Reinicia os dois contadores em zero a cada execução.

## Como executar

Na pasta do projeto, execute:

```bash
python main.py
```

Depois, siga as perguntas apresentadas no terminal.

## Exemplo

Na primeira pergunta, a alternativa correta é `b`.

Se o usuário digitar `z`, o programa informa que a entrada é inválida, acrescenta uma entrada inválida ao contador e solicita outra tentativa.

Se digitar `a` ou `c`, o programa informa que a resposta está incorreta e segue para a próxima pergunta, sem somar pontos.

Respondendo `z`, depois `b` e, na segunda pergunta, `a`, o resultado final será:

```text
Pontuação: 2/2
Entradas inválidas: 1
```

## Casos verificados

As entradas abaixo estão na ordem em que foram digitadas.

| Entradas | Pontuação final | Entradas inválidas |
|---|---|---|
| `b`, `a` | 2/2 | 0 |
| `a`, `a` | 1/2 | 0 |
| `c`, `b` | 0/2 | 0 |
| Somente espaços, `z`, ` B `, `x`, ` A ` | 2/2 | 3 |