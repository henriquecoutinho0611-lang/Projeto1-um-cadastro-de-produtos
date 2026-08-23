import json

pessoa = []

try: 
 with  open('dados.json', 'r' ) as arquivo:
       pessoa = json.load(arquivo)
except (FileNotFoundError,json.JSONDecodeError):
    pessoa=[]       

while True:

    if pessoa:
     id = pessoa[-1]['id'] + 1    
    else:
        id = 1    

    nome = str(input("Qual o seu nome: ")).lower()

    email = str(input("Qual o seu E-mail: "))

    while True:
        try:
            telefone = input("Qual o seu telefone: ")

            if len(telefone) != 11:
                raise ValueError

        except ValueError:
            print("Telefone inválido")
            continue

        break

    while True:
        try:
            data = input("Data de nascimento (apenas números): ")

            if len(data) != 8:
                raise ValueError

        except ValueError:
            print("Data inválida")
            continue

        break

    dados = {
        "id": id,
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "data": data
    }

    pessoa.append(dados)

   

    resposta = input(
        "Deseja cadastrar mais alguém? (s/n): "
    ).lower()

    if resposta == "s":
        continue
    else:
        break


with open("dados.json", "w") as salvar:
 json.dump(pessoa,salvar,indent=4)
     
   

print("Fim da lista")