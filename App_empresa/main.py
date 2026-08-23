import os

while True:
 print('-'*30)

 opcao = input('Digite 1 para buscar um produto,  2 para cadastrar um novo produto, 3 Para finalizar\n')

 pasta = os.path.dirname(os.path.abspath(__file__))


 if opcao == '1':
  exec(open('Buscar_produtos.py').read()) 

 elif opcao == '2':
  exec(open('salvar_produtos.py').read())

 elif opcao == '3':
  print("Obrigado , volte sempre" )
  break
 
 else:
  print('Opção inválida')