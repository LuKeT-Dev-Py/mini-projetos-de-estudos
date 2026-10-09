from Modulos.sessao import cadastrar_sessao, listar_sessoes

sessoes = []
menu = ['1-Cadastrar', '2-Listar e mostrar total', '0-Sair']

while True:
    print(menu)
    escolha = input('Digite qual escolha do menu deseja: ')
    try:
        escolha = int(escolha)
    except ValueError:
        print('Digite um valor inteiro valido.')
        continue
    if escolha == 1:
        sessao = cadastrar_sessao()
        sessoes.append(sessao)
        continue
    elif escolha == 2:
        listar_sessoes(sessoes)
        continue
    elif escolha == 0:
        break
    else:
        print('Digite uma opção válida: 0, 1 ou 2.')

