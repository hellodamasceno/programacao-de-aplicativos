valor_da_compra = int(input("digite o valor total da compra: "))
prime = input("É prime? ")
frete = 50.00

if valor_da_compra >= 500.00 or (prime == "sim" and valor_da_compra >= 100.00) :
    frete = 00.00

valor_final = valor_da_compra - frete
