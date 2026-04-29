print("----------BOAS VINDAS----------")
rua = input("Digite o nome da rua: ")
numero = int(input("Digite o numero da casa: "))
bairro = input("Digite o bairro: ")
cep = int(input("Digite o CEP: "))


def  gerar_etiqueta(rua, numero, bairro, cidade, cep, etiqueta):
    etiqueta = (f"Rua: {rua}, Numero: {numero}, Bairro: {bairro}, Cidade: {cidade}, CEP: {cep}")

    