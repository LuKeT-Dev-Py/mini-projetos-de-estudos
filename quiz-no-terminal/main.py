print('Qual instrução devolve um valor de uma função?\n'
    'A — print\n'
    'B — return\n'
    'C — input')
correto = 'b'
aceito = ['a', 'b', 'c']
pontos = 0
entradas_invalidas = 0

while True:
    resposta = input('Qual sua resposta: ').strip().lower()
    if resposta in aceito:
        if resposta == correto:
            print('Resposta correta!\n')
            pontos += 1
            break
        else:
            print('Resposta incorreta.\n')
            break
    else:
        print('Resposta invalida, tente novamente.\n')
        entradas_invalidas += 1
        continue

print('Qual método adiciona um elemento ao final de uma lista?\n'
    'A — append\n'
    'B — strip\n'
    'C — lower')
correto2 = 'a'
aceito2 = ['a', 'b', 'c']

while True:
    resposta2 = input('Qual sua resposta: ').strip().lower()
    if resposta2 in aceito2:
        if resposta2 == correto2:
            print('Resposta correta!\n')
            pontos += 1
            break
        else:
            print('Resposta incorreta.\n')
            break
    else:
        print('Resposta invalida, tente novamente.\n')
        entradas_invalidas += 1
        continue

print(f'Pontuação: {pontos}/2')
print(f'Entradas inválidas: {entradas_invalidas}')
