def pedir_titulo():
    while True:
        titulo = input('Digite o titulo do livro: ').strip()
        if titulo == '':
            continue
        else:
            return titulo