senha = input("Digite a senha: ")
numero_tentativas = int(input("Digite o numero de tentativas: "))
token = input ("Possui token? ")

if senha == "admin123" and (numero_tentativas % 3 or token == "vip"):
    print (f"tentativa nº {numero_tentativas}: ACESSO CONCEDIDO")
else:
    print (f"Tentativa nº {numero_tentativas}: ACESSO BLOQUEADO POR PROTOCOLO")    