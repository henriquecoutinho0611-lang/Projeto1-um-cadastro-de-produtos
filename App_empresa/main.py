from Buscar_produtos import lista_produtos,buscar
from Validacao import sim_nao, validar_int
from editar import editar_produtos
from salvar_produtos import cadasta_produto
from apagar import apagar
                  


def main():
    while True: 
     try:
      print("="*30)
      print(" 1 - para buscar\n 2 - para cadastrar\n 3 - para lista todos os produtos\n 4 - para editar um produto\n 5 - para apagra ")
      print("="*30)
      condicao = validar_int("")
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
     elif condicao == 5:
       apagar()    
     else:
        print("Opção inválida")

     print("-"*30)   
     if not sim_nao("Deseja continuar? "):
      print("Muito obrigado")
      print()
      break    

if __name__ == "__main__": 
   main() 
