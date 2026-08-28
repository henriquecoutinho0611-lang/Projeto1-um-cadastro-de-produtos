from salvar_produtos import Novo_produto
from arquivos import salvar_arquivos, ler_arquivo
from Buscar_produtos import buscar_arquivo, lista_produtos
from Validacao import sim_nao, validar_int
from editar import editar_produtos

def cadasta_produto():
     while True:
            
            produtos = ler_arquivo()
            produtos = Novo_produto(produtos)
            salvar_arquivos(produtos)

            if not sim_nao("Deseja cadastrar mais algum produto? "):
               break

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

                  


def main():
    while True: 
     try:
      condicao = validar_int("1 para buscar\n2 para cadastrar\n3 para listar todos os produtos\n4 para editar um produto\n")
     except ValueError:
      print("Digite apenas números")
      continue
     if condicao == 1:
        buscar()
     elif condicao == 2:
       cadasta_produto()
     elif condicao == 3:
        lista_produtos()
     elif condicao == 4:
        editar_produtos()     
     else:
        print("Opção inválida")

     print("-"*30)   
     if not sim_nao("Deseja continuar? "):
      print("Muito obrigado")
      break    

if __name__ == "__main__": 
   main() 
