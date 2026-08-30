from arquivos import ler_arquivo
from Validacao import sim_nao

def buscar_arquivo():
    busca = input("Qual é o nome ou ID do produto?\n").lower().strip()
    resultado = []

    for produto in ler_arquivo():
        if busca in str(produto["id"]) or busca in produto["nome"].lower():
            resultado.append(produto)

    return resultado

def buscar():

      while True:
       buscar = buscar_arquivo()
       if buscar:
            for produto in buscar:
             print("-" * 30)
             print(f"ID: {produto['id']}")
             print(f"Nome: {produto['nome']}")
             print(f"Largura: {produto['largura']}mm")
             print(f"Altura: {produto['altura']}mm")
             print(f"Profundidade: {produto['profundidade']}mm")
             if produto['obs']:
              print(f"OBS: {produto['obs']}")
             print("-" * 30)
       else:
          print("Produto não encontrado\n ")

       if not sim_nao("Deseja buscar mais algum produto? "):
          break


def lista_produtos():
    for produto in ler_arquivo():
        print("-" * 30)
        print(f"ID: {produto['id']}")
        print(f"Nome: {produto['nome']}")
        print(f"Largura: {produto['largura']}mm")
        print(f"Altura: {produto['altura']}mm")
        print(f"Profundidade: {produto['profundidade']}mm")
        if produto['obs']:
         print(f"OBS: {produto['obs']}")
        print("-" * 30)
