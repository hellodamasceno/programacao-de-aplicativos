cliente = input("Nome do Cliente: ")
valor_total_da_compra = float(input("Valor da Compra: R$ "))
distancia = int(input("Distância: "))
cupom = input("Possui cupom?: ")

desconto = 0.0

if valor_total_da_compra >= 1000.0 and cupom == "S":
    desconto = valor_total_da_compra * 0.20
elif valor_total_da_compra > 500.0 and cupom == "S":
    desconto = valor_total_da_compra * 0.10










print ("olá", nome)
print ("valor total ", valor_total_da_compra)
print("valor do desconto", cupom )
print("valor final ", valor_total_da_compra )
