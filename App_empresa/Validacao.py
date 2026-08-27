
def sim_nao(texto):
    while True:
     resposta = input(texto).lower().strip()

     if resposta in ("n", "nao"):
         return True
     if resposta in ("s", "sim"):
        return False

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
