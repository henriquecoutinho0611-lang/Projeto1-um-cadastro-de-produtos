

def cacular(caculo):
 if caculo[1] == '+':
    valor = caculo[0] + caculo[2]
 elif caculo[1] == '-':
    valor = caculo[0] - caculo[2]
 elif caculo[1] == '*':
   valor = caculo[0] * caculo[2]
 elif caculo[1] == '/':
    valor = caculo[0] / caculo[2]
 return valor



while True:
 caculo = []*3

 try:

  resposta = input('digite sua operacao:  ').split()


 
  caculo.append(float(resposta[0]))
  caculo.append(resposta[1])
  caculo.append(float(resposta[2]))
  print(f'resutado:  {cacular(caculo)}')     
  
 except ValueError:
  print("operacao invalida")

 if input(" aperte qual quer tecla para sair ou s para fazer mas uma vez: ").lower() !='s':
  break