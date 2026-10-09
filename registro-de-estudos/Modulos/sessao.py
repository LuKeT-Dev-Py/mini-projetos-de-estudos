def cadastrar_sessao():
    sessao = {}
    print('')
    while True:
        asssunto = input('Qual assunto estudou: ').strip()
        if asssunto == '':
            print('Assunto invalido.')
            continue
        break
    while True:
        duracao = input('Qual a duração em minutos(Apenas numero): ')
        try:
            duracao = int(duracao)
        except ValueError:
            print('Digite um valor valido!')
            continue
        if duracao == 0:
            print('Zero não é valido.')
            continue
        elif duracao <= 0:
            print('Digite um valor maior que 0.')
            continue
        sessao['assunto'] = asssunto
        sessao['minutos'] = duracao
        print('Sessão Confirmada.')
        return sessao


def listar_sessoes(sessoes):
    acumulador = 0
    if sessoes == []:
        print("Nenhuma sessão registrada.")
    for n in sessoes:
        print(f"{n['assunto']}: {n['minutos']} min")
        acumulador += n['minutos']
    print(f'Total estudado: {acumulador} min')

