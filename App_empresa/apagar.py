from Buscar_produtos import buscar_arquivo
from arquivos import ler_arquivo,salvar_arquivos
from Validacao import sim_nao,validar_int


def apagar():
  while True: 
    encontados = buscar_arquivo()
    produtos = ler_arquivo()

    if  encontados:
        for i, encontado in enumerate(encontados, start=1):
            print(f"{i} - {encontado['nome']}")

        try:        
         i = validar_int("qual deseja apagar ")
         apagar = encontados[i - 1]
        except IndexError:
         print("opicao invalida")
         continue

        for produto in produtos:
         if produto["id"] == apagar["id"]:
                
                print("-" * 30)  
                print(f"ID: {produto['id']}")  
                print(f"Nome: {produto['nome']}")  
                print(f"Largura: {produto['largura']}mm")  
                print(f"Altura: {produto['altura']}mm")  
                print(f"Profundidade: {produto['profundidade']}mm")  
                if produto['obs']:  
                    print(f"OBS: {produto['obs']}")  
                print("-" * 30)

                if sim_nao("deseja deletar o produto "):
                    produtos.remove(produto)
                    salvar_arquivos(produtos)
                print("produto apagado com suceso")

    else:
        print("produto nao encontado ")

    if not sim_nao("deseja apagar mas algun produto "):
        break                    

            


                


            

