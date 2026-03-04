valor_da_compra = int(input("digite o valor total da compra: "))
prime = input("É prime? ")
frete = 50.00

if valor_da_compra >= 500.00 or (prime == "sim" and valor_da_compra >= 100.00) :
    print("frete grátis! ")
    frete = 0.0
    print("valor total da compra:" , valor_da_compra)

valor_da_compra = valor_da_compra + frete
print("valor total da compra: ", valor_da_compra)