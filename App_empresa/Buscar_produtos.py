from arquivos import ler_arquivo


def buscar_arquivo():
    busca = input("Qual nome ou id do produto?\n").lower().strip()
    resultado = []

    for produto in ler_arquivo():
        if busca in str(produto["id"]) or busca in produto["nome"].lower():
            resultado.append(produto)

    return resultado


def main():
    continuar = "s"

    while continuar == "s":
        produtos = buscar_arquivo()

        if produtos:
            for produto in produtos:
                print("-" * 30)
                print(f"ID: {produto['id']}")
                print(f"Nome: {produto['nome']}")
                print(f"Largura: {produto['largura']}")
                print(f"Altura: {produto['altura']}")
                print(f"Profundidade: {produto['profudidade']}")
                print(f"OBS: {produto['obs']}")
                print("-" * 30)
        else:
            print("Produto nao encontrado\n")

        continuar = input("Deseja buscar mais algum produto? (s/n) ").lower().strip()


if __name__ == "__main__":
    main()
