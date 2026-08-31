from Buscar_produtos import buscar_arquivo
from arquivos import ler_arquivo, salvar_arquivos
from Validacao import sim_nao, validar_int, validar_str


# Edita um produto que já está salvo no arquivo JSON.
# Primeiro busca o produto, depois deixa o usuário escolher qual resultado editar.
def editar_produtos():
    while True:
        encontrados = buscar_arquivo()
        produtos = ler_arquivo()

        if encontrados:
            # encontrados: lista com os produtos que bateram com a busca.
            # O enumerate mostra uma numeração para o usuário escolher.
            for i, produto in enumerate(encontrados, start=1):
                print(i, produto["nome"])

            try:
                escolha = validar_int("Qual deseja editar? ")
                produto_escolhido = encontrados[escolha - 1]
            except IndexError:
                print("Opção inválida")
                continue

            # produtos: lista completa que veio do JSON.
            # É essa lista completa que precisa ser salva depois da edição.
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

                    # Cada pergunta abaixo altera apenas o campo escolhido.
                    if sim_nao("Deseja editar o nome do produto? "):
                        produto.update({"nome": validar_str("Informe o novo nome: ")})

                    if sim_nao("Deseja editar a largura do produto? "):
                        produto.update({"largura": validar_int("Informe a nova largura: ")})

                    if sim_nao("Deseja editar a altura? "):
                        produto.update({"altura": validar_int("Informe a nova altura: ")})

                    if sim_nao("Deseja editar a profundidade? "):
                        produto.update(
                            {"profundidade": validar_int("Informe a nova profundidade: ")}
                        )

                    if sim_nao("Deseja editar a observação? "):
                        produto.update({"obs": validar_str("Informe a nova observação: ")})

                    # Salva a lista completa já com o produto alterado.
                    salvar_arquivos(produtos)
                    print("Produto editado com sucesso")
        else:
            print("Produto não encontrado")

        if not sim_nao("Deseja editar mais algum produto? "):
            break
