
def sim_nao(texto):
    while True:
     resposta = input(texto).lower().strip().split()

     if resposta in ("n", "nao"):
         return False
     if resposta in ("s", "sim"):
        return True

     print("Opção inválida")
     


def validar_int(texto, minimo=0):
    while True:
        try:
            valor = int(input(texto))
        except ValueError:
            print("Digite apenas números")
            continue

        if valor <= minimo:
            print("Número inválido")
            continue

        return valor

def validar_str(texto):
    while True:
     resposta = input(texto).lower().strip()
     if resposta: 
      return resposta
     else:
      print("Inválido")
     continue
     
     
