from Validacao import validar_str, validar_int, sim_nao
from Buscar_produtos import buscar_arquivo
from arquivos import salvar_arquivos, ler_arquivo

def editar_produtos():
    while True:
        encontrados = buscar_arquivo()

        if encontrados:
          
            produto_encontrado = encontrados[0]
            produtos = ler_arquivo()
        else:
            print("Produto não encontrado")

            for produto in produtos:
                if produto["id"] == produto_encontrado["id"]:

                    print("-" * 30)
                    print(f"ID: {produto['id']}")
                    print(f"Nome: {produto['nome']}")
                    print(f"Largura: {produto['largura']}mm")
                    print(f"Altura: {produto['altura']}mm")
                    print(f"Profundidade: {produto['profundidade']}mm")
                    if produto['obs']:
                        print(f"OBS: {produto['obs']}")
                    print("-" * 30)

                    if sim_nao("Deseja editar o nome do produto? "):
                        produto.update({"nome": validar_str("Informe o novo nome: ")})

                    if sim_nao("Deseja editar a largura do produto? "):
                        produto.update({"largura": validar_int("Informe a nova largura: ")})

                    if sim_nao("Deseja editar a altura? "):
                        produto.update({"altura": validar_int("Informe a nova altura: ")})

                    if sim_nao("Deseja editar a profundidade? "):
                        produto.update({"profundidade": validar_int("Informe a nova profundidade: ")})

                    if sim_nao("Deseja editar a observação? "):
                        produto.update({"obs": validar_str("Informe a nova observação: ")})

                    salvar_arquivos(produtos)
                    print("Produto editado com sucesso")
                    break

        if not sim_nao("Deseja editar mais algum produto? "):
            break