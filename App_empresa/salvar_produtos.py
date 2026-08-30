from Validacao import validar_int, validar_str,sim_nao
from arquivos import ler_arquivo, salvar_arquivos


def gerar_id(produtos):
    if produtos:
        return produtos[-1]["id"] + 1
    return 1


def Novo_produto (produtos):
    id_produto = gerar_id(produtos)

    nome = validar_str("Qual é o nome da peça?\n")
    print("-" * 30)

    largura = validar_int("Informe a largura em mm: ")
    print("-" * 30)

    altura = validar_int("Informe a altura em mm: ")
    print("-" * 30)

    profundidade = validar_int("Informe a profundidade em mm: ")
    print("-" * 30)

    obs = input("Existe alguma observação?\n")
    print("-" * 30)

    dados = {
        "id": id_produto,
        "nome": nome,
        "largura": largura,
        "altura": altura,
        "profundidade": profundidade,
        "obs": obs if obs else None,
    }

    produtos.append(dados)

    return produtos


def cadasta_produto():
     while True:
            
            produtos = ler_arquivo()
            produtos = Novo_produto(produtos)
            salvar_arquivos(produtos)

            if not sim_nao("Deseja cadastrar mais algum produto? "):
               break
