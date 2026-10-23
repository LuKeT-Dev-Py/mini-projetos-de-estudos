from  Modulos.titulo import  pedir_titulo
from Modulos.persistencia import salvar_leituras, carregar_leituras
import json

menu = [
    '1 — Cadastrar título',
    '2 — Listar títulos',
    '0 — Sair'
]
pode_iniciar = True
try:
    caminho = "leituras_treino_quarta.json"
    lista = carregar_leituras(caminho)
except FileNotFoundError:
    print('Dados não encontrados lista nova criada.')
    lista = []
except json.JSONDecodeError:
    print(f'caminho: {caminho}, não pode ser lido.')
    pode_iniciar = False


while pode_iniciar:
    print(menu)
    escolha = input('Escolha o numero que deseja do menu: ')
    print(' ')
    try:
        escolha = int(escolha)
    except ValueError:
        print('Digite um numero valido.\n')
        continue
    if escolha in [0, 1, 2]:
        if escolha == 1:
            add = pedir_titulo()
            lista.append(add)
            salvar_leituras(lista, caminho)
        elif escolha == 2:
            if lista == []:
                print("Nenhum título cadastrado.\n")
                continue
            print(lista)
            print(f'Quantidade cadastrada: {len(lista)}\n')
        elif escolha == 0:
            break
    else:
        print('Numero invalido tente novamente.\n')




