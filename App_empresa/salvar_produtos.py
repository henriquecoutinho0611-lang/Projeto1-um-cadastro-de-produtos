from Validacao import ler_numero, ler_texto



def gerar_id(produtos):
    if produtos:
        return produtos[-1]["id"] + 1
    return 1


def Novo_produto (produtos):
    id_produto = gerar_id(produtos)

    nome = ler_texto("Qual o nome da peca?\n")
    print("-" * 30)

    largura = ler_numero("Informe a largura em mm: ")
    print("-" * 30)

    altura = ler_numero("Informe a altura em mm: ")
    print("-" * 30)

    profundidade = ler_numero("Informe a profundidade em mm: ")
    print("-" * 30)

    obs = input("Existe alguma observacao?\n")
    print("-" * 30)

    dados = {
        "id": id_produto,
        "nome": nome,
        "largura": largura,
        "altura": altura,
        "profundidade": profundidade,
        "obs": obs,
    }

    produtos.append(dados)

    return produtos


