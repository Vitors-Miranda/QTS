import json
# xls extensa
#abrindo arquivo JSON
arquivo = open("c:/driver/lista.json", encoding='utf-8')
#Carregando os dados do arquivo
lista = json.load(arquivo)
#Percorrendo a lista
for item in lista:
    print("Nome: "+ item["Nome"])
    print("Email: "+ item["Email"])
    print("Nota 1: "+ str(item["nota1"]))
    print("Nota 2: "+ str(item["nota2"]))
    print("------------")
    