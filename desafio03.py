saldo_inicial = 1000.00
nome = input("digite seu nome ")
print ("seja bem vindo, ", nome)
print ("opçoes de menu: 1-deposito, 2-saque, 3-extrato")
menu = int(input("digite as opçoes do menu "))

if menu == 1:
    valor = float(input("digite o valor: "))
    if valor > 0.00 : 
        valor_final = saldo_inicial + valor
        print ("valor final: ", valor_final)

elif menu == 2:
    valor = float(input("digite o valor: "))
    if valor > 0.0 and (valor <= saldo_inicial or valor == 100):
        valor_final = saldo_inicial - valor
        print ("valor final: ", valor_final)
    else :
        print("Saldo insuficiente! ")

        
elif menu == 3:
    print ("Seu saldo é: ", saldo_inicial)        
