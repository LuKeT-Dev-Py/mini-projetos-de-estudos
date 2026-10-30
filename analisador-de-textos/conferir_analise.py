from Analisar_txt import analisar_texto

def resultados_iguais(obtido, esperado):
    if obtido == esperado:
        return True
    else:
        return False

def opcao_permitida(opcao):
    permitidas = (1, 0)
    if opcao in permitidas:
        return True
    else:
        return False

