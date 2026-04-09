saldo = 500

print(f"saldo atual: {saldo}")
print("-----------------------------------------------")
print("1-Depositar") 
print("2-Sacar") 
print("3-Sair")  

opcao = int(input("Digite a opção desejada: "))
while  opcao != 3:
    if opcao == 1:
        valor = float(input("Digite o valor para depósito: "))
        saldo += valor
        print(f"Saldo após deposito: {saldo}")
    
    elif opcao == 2:
        saque = float(input("Digite o valor para saque: "))
        if saque > saldo:
            print ("Saldo insuficiente")
        

    elif opcao == 3:
        print("Saindo do programa")        
    
    opcao = int(input("Digite a opção desejada: "))