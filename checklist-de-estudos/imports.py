def titulo_valido(titulo):
    titulo = titulo.strip()
    if titulo == '':
        return False
    else:
        return {"titulo": titulo, "concluida": False}
    
def adicionar_se_criada(tarefas, tarefa):

    if tarefa is False:
        return False
    else:
        tarefas.append(tarefa)
        return True

def situacao_tarefa(tarefa):
    if tarefa['concluida'] is True:
        return "Concluída"
    else:
        return 'Pendente'

def marcar_concluida(tarefas, numero):
    if numero > 0 and numero <= len(tarefas):
        tarefas[numero-1]["concluida"] = True
        return True
    else:
        return False