# import json

# frase = input("Digite uma frase: ")

# dados =  {
#     "Mensagem": frase
# }

# print(dados)

# with open("teste.json", 'w', encoding="utf-8") as arquivo:
#     json.dump(dados, arquivo)



import json 


dados = {
    "matematica": 8.5,
    "portugues": 9.0,
    "soma": 0

}

matematica = dados["matematica"]
portugues = dados["portugues"]

dados["soma"] = matematica + portugues



print("Soma das notas: ", dados["soma"])

with open("notas.json", 'w', encoding="utf-8") as L:
    json.dump(dados, L)