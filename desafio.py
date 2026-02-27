nome = input ("digite seu nome: ")
valor_total_da_compra = float (input("digite o valor total da compra: "))
entrega = int (input("qual a distancia da entrega? "))
cupom = input("digite o cupom de desconto: ")
frete = 40.00

if valor_total_da_compra >= 1000.00 and cupom == "S" :
    multiplicacao =  valor_total_da_compra * 0.20
    subtraçao = valor_total_da_compra - multiplicacao
    print("Parabéns! Você ganhou um Mousepad Gamer de brinde!")

elif valor_total_da_compra > 500.00 and valor_total_da_compra < 1000.00 and cupom == "S":
    multiplicacao = valor_total_da_compra * 0.10
    subtraçao = valor_total_da_compra - multiplicacao

elif  entrega <= 50 and valor_total_da_compra > 200.00:
    frete = 0.00
    subtraçao = valor_total_da_compra + frete 
else:
    total = subtraçao + frete     
print ("olá", nome)
print ("valor total ", valor_total_da_compra)
print("valor do desconto", cupom )
print("valor final ", valor_total_da_compra )
