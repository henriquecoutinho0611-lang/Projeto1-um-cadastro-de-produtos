from arquivos import ler_arquivo, salvar_arquivos



def sair():
    resposta = input("Deseja cadastrar outro produto? (s/n) ").lower().strip()

    if resposta in ("n", "nao"):
        return "nao"
    if resposta in ("s", "sim"):
        return "sim"

    print("Opcao invalida")
    return None


def ler_numero(texto, minimo=0):
    while True:
        try:
            valor = float(input(texto))
        except ValueError:
            print("Digite apenas numeros")
            continue

        if valor < minimo:
            print("Numero invalido")
            continue

        return valor


def gerar_id(produtos):
    if produtos:
        return produtos[-1]["id"] + 1
    return 1


def Novo_produto (produtos):
    id_produto = gerar_id(produtos)

    nome = input("Qual o nome da peca?\n")
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
        "profudidade": profundidade,
        "obs": obs,
    }

    produtos.append(dados)
    return produtos


def main():
    while True:
        produtos = ler_arquivo()
        produtos = Novo_produto(produtos)
        salvar_arquivos(produtos)

        if sair() == "nao":
            break


if __name__ == "__main__":
    main()
