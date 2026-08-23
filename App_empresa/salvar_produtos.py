import json

salvar = []

try:
 with open('salva.json', 'r' ) as arquivo:
     salvar = json.load(arquivo)
except (FileNotFoundError,json.JSONDecodeError):
     salvar = []


while True:
  if salvar :
       id = salvar[-1]['id'] + 1
  else:
       id = 1


  nome = input('qual o Nome da preca:\n ')
  print('-' *30)
  while True:
     try:
      largura = float(input( 'informe a largura em mm:\n ' ))
      print('-'*30)
     except ValueError:
      print('numero invalido')
      continue
     break

  while True:
         try:
          altura = float(input( 'informe a altura em mm:\n ' ))
          print('-'*30)
         except ValueError:
          print('numero invalido')
          continue
         break
  
  while True:
        try:
         profudidade = float(input( 'informe a profundodade em mm\n ' ))
         print('-' *30 )
        except ValueError:
         print('numero invalido')
         continue
        break
    
  obs = input('exite alguma obsevacao\n ')
  print('-'*30 ) 
  dados = { 'id': id,
            'nome':nome,
            'largura': largura,
            'altura' : altura,
            'profudidade': profudidade,
            'obs' : obs
               }

  salvar.append(dados)
 
  
  if input('deseja adicionara mais algun produtor (n/s)\n').lower() !='s':
   break
  
with open('salva.json', 'w') as arquivo:
 json.dump(salvar,arquivo, indent=4)

print('-'*40 )
print('produto salvo com sucesso')