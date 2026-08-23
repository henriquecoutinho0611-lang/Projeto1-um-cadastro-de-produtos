import json

def ler_arquivos():
 try:
    with open('salva.json', 'r') as arquivo:
        buscar = json.load(arquivo)
 except ValueError:
    print("arquivo nao encontado")
    return[]
 return buscar


def busca_arquivo():
  try:
    busca = input('Qual nome ou id do produto:\n ').lower()
    resutado = []
    for produto in ler_arquivos():

        if busca in str(produto['id']) or busca in produto['nome'].lower():
            resutado.append(produto)
            return resutado
        
  except ValueError:
     print(' Produto não encontrado ou nome incorreto ')

  return None
  

continuar = 's'

while continuar == 's':
 
 produtos = busca_arquivo()
 for produto in produtos:
  if produto:
    print('-' * 30)
    print(f"ID: {produto['id']}")
    print(f"Nome: {produto['nome']}")
    print(f"Largura: {produto['largura']}")
    print(f"Altura: {produto['altura']}")
    print(f"Profundidade: {produto['profudidade']}")
    print(f"OBS: {produto['obs']}")
    print('-' * 30)

 else:
    print(' Produto não encontrado\n ')

 continuar = input('Deseja buscar mais algum produto(s/n)' ).lower()