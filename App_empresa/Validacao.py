
# Faz uma pergunta de sim ou não e devolve True para sim e False para não.
def sim_nao(texto):
    while True:
     resposta = input(texto).lower().strip().split()

     if resposta in ("n", "nao"):
         return False
     if resposta in ("s", "sim"):
        return True

     print("Opção inválida")
     


# Lê um número inteiro digitado pelo usuário e valida se ele é maior que o mínimo.
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

# Lê um texto digitado pelo usuário e não deixa voltar vazio.
def validar_str(texto):
    while True:
     resposta = input(texto).lower().strip()
     if resposta: 
      return resposta
     else:
      print("Inválido")
     continue
     
     
