from Analisar_txt import analisar_texto, pedir_texto
from conferir_analise import resultados_iguais, opcao_permitida
menu = ['1 — Analisar texto',
        '0 - Sair']
while True:
    print(menu)
    try:
        escolha = int(input('Qual numero deseja escolher: '))   
    except ValueError:
        print('Digite um valor valido')
        continue
    if opcao_permitida(escolha):
        if escolha == 1:
            texto = pedir_texto()
            dict = analisar_texto(texto)
        elif escolha == 0:
            break
        else:
            print('Não deve chegar aqui.')
    else:
        print('Escolha uma opcão correta.')
        continue

    print(f'Palavras: {dict['palavras']}')
    print(f'Caracteres: {dict['caracteres']}')
