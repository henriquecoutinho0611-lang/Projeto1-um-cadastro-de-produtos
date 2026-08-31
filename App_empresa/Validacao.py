
# Faz uma pergunta de sim ou não.
# Retorna True quando o usuário digita "s" ou "sim".
# Retorna False quando o usuário digita "n" ou "nao".
def sim_nao(texto):
    while True:
        resposta = input(texto).lower().strip()

        if resposta in ("n", "nao"):
            return False

        if resposta in ("s", "sim"):
            return True

        print("Opção inválida")


# Pede um número inteiro para o usuário.
# Continua perguntando até receber um número maior que o valor mínimo.
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


# Pede um texto para o usuário.
# Continua perguntando se o usuário deixar a resposta vazia.
def validar_str(texto):
    while True:
        resposta = input(texto).strip()

        if resposta:
            return resposta

        print("Inválido")
