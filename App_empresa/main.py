import os


PASTA = os.path.dirname(os.path.abspath(__file__))


while True:
    print("-" * 30)

    opcao = input(
        "Digite 1 para buscar um produto, 2 para cadastrar um novo produto, 3 para finalizar\n"
    )

    if opcao == "1":
        exec(open(os.path.join(PASTA, "Buscar_produtos.py"), encoding="utf-8").read())

    elif opcao == "2":
        exec(open(os.path.join(PASTA, "salvar_produtos.py"), encoding="utf-8").read())

    elif opcao == "3":
        print("Obrigado, volte sempre")
        break

    else:
        print("Opcao invalida")
