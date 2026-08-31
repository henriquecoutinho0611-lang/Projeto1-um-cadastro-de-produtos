from Buscar_produtos import buscar_arquivo
from arquivos import ler_arquivo, salvar_arquivos
from Validacao import sim_nao, validar_int


# Apaga um produto que já está salvo no arquivo JSON.
# Primeiro busca o produto, depois confirma antes de remover.
def apagar():
    while True:
        encontrados = buscar_arquivo()
        produtos = ler_arquivo()

        if encontrados:
            # encontrados: lista com os produtos que bateram com a busca.
            # O enumerate mostra uma numeração para o usuário escolher.
            for i, encontrado in enumerate(encontrados, start=1):
                print(f"{i} - {encontrado['nome']}")

            try:
                escolha = validar_int("Qual deseja apagar? ")
                produto_escolhido = encontrados[escolha - 1]
            except IndexError:
                print("Opção inválida")
                continue

            # produtos: lista completa que veio do JSON.
            # O remove precisa acontecer nessa lista completa.
            for produto in produtos:
                if produto["id"] == produto_escolhido["id"]:
                    print("-" * 30)
                    print(f"ID: {produto['id']}")
                    print(f"Nome: {produto['nome']}")
                    print(f"Largura: {produto['largura']}mm")
                    print(f"Altura: {produto['altura']}mm")
                    print(f"Profundidade: {produto['profundidade']}mm")

                    if produto["obs"]:
                        print(f"OBS: {produto['obs']}")

                    print("-" * 30)

                    if sim_nao("Deseja apagar o produto? "):
                        produtos.remove(produto)
                        salvar_arquivos(produtos)
                        print("Produto apagado com sucesso")
        else:
            print("Produto não encontrado")

        if not sim_nao("Deseja apagar mais algum produto? "):
            break
