from arquivos import ler_arquivo


def buscar_arquivo():
    busca = input("Qual nome ou id do produto?\n").lower().strip()
    resultado = []

    for produto in ler_arquivo():
        if busca in str(produto["id"]) or busca in produto["nome"].lower():
            resultado.append(produto)

    return resultado