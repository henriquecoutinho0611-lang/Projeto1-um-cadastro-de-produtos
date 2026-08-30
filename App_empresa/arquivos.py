import json
import os

PASTA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(PASTA,"salvar.json")


# Lê o arquivo JSON e devolve a lista de produtos.
def ler_arquivo():
    try:
        with open(ARQUIVO, "r", encoding="utf8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
     return [] 

# Salva a lista de produtos dentro do arquivo JSON.
def salvar_arquivos(produtos):  
   with open(ARQUIVO, "w", encoding="utf8") as arquivo:
      json.dump(produtos, arquivo, indent= 4, ensure_ascii=False)
