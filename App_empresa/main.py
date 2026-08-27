from salvar_produtos import Novo_produto
from arquivos import salvar_arquivos, ler_arquivo
from Buscar_produtos import buscar_arquivo
from Validacao import sim_nao

def cadasta_produto():
     while True:
            
            produtos = ler_arquivo()
            produtos = Novo_produto(produtos)
            salvar_arquivos(produtos)

            if sim_nao("deseja cadasta mais algum produto?  "):
               break

def buscar():

      while True:
       
       if buscar_arquivo:
            for produto in buscar_arquivo():
             print("-" * 30)
             print(f"ID: {produto['id']}")
             print(f"Nome: {produto['nome']}")
             print(f"Largura: {produto['largura']}")
             print(f"Altura: {produto['altura']}")
             print(f"Profundidade: {produto['profudidade']}")
             print(f"OBS: {produto['obs']}")
             print("-" * 30)
       else:
          print("Produto nao encontrado\n ")

       if sim_nao("deseja busca mais algun produto? "):
          break

                  


def main():
    while True: 
     try:
      condicao = int(input(" 1 para buscar\n 2 para salvar "))
     except ValueError:
      print(" Digite apenas números")
      continue
     if condicao == 1:
        buscar()
     elif condicao == 2:
       cadasta_produto()
     else:
        print(" Opção inválida ")

     print("-"*30)   
     if sim_nao(" Deseja continuar? "):
      break    

if __name__ == "__main__": 
   main() 