
def sim_nao(texto):
    while True:
     resposta = input(texto).lower().strip()

     if resposta in ("n", "nao"):
         return False
     if resposta in ("s", "sim"):
        return True

     print("Opcao invalida")
     


def ler_numero(texto, minimo=0):
    while True:
        try:
            valor = float(input(texto))
        except ValueError:
            print("Digite apenas numeros")
            continue

        if valor <= minimo:
            print("Numero invalido")
            continue

        return valor

def ler_texto(texto)
    while True:
     texto = str(input(texto)
     if texto 
      return texto
     else:
     print("texto inválido")
     
     
