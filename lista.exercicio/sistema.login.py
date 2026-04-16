senha = input("Digite a senha : ")
senha_correta = "1234"
tentativas = 1

while tentativas <3 and senha  != senha_correta:
    senha = input("Digite a senha novamente :")
    tentativas += 1
if senha == senha_correta:
    print("Acesso liberado") 

elif tentativas == 3:
    print("Acesso bloqueado")       
