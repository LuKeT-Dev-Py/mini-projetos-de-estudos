from imports import *

tarefas = []
while True:
    titulo = input('Qual titulo da tarefa: ')
    tarefa = titulo_valido(titulo)
    retorno = adicionar_se_criada(tarefas, tarefa)
    if retorno and len(tarefas) == 2:
        break
    elif retorno:
        continue
    else:
        print('Título inválido. Tente novamente.\n')
        continue

for item in tarefas:
    print(f'{item['titulo']} - {situacao_tarefa(item)}')

while True:
    print('0 - Sair')
    menu = input('Qual tarefa deseja mudar: ')
    try:
        menu = int(menu)
        if menu == 0:
                break
    except ValueError:
        print('Escreva um numero inteiro valido!')
        continue
    m_c = marcar_concluida(tarefas, menu)
    if not m_c:
        print("A tarefa selecionada não existe.")
        continue
    for item in tarefas:
        print(f'{item['titulo']} - {situacao_tarefa(item)}')
    