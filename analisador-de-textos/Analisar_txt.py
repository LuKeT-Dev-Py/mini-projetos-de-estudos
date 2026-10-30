def analisar_texto(texto):
    Sem_espaco = texto.strip()
    separado = Sem_espaco.split()
    numero_p = len(separado)
    numero_c = len(Sem_espaco)
    
    return {'palavras': numero_p, 'caracteres': numero_c}

def pedir_texto():
    while True:
        textop = input('Texto para analisar: ').strip()
        if textop:
            return textop
        else:
            print('Digite algum texto!')
            continue