import json

def salvar_leituras(lista, caminho):
    with open(caminho, "w", encoding="utf8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=2)

def carregar_leituras(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        recuperado = json.load(arquivo)
        return recuperado