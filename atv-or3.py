nome_de_usuario = input ("digite seu nome de usuario: ")
senha = input("digite a senha: ")

if (nome_de_usuario == "admin" or nome_de_usuario == "root") and senha == "12345" :
    print("Acesso liberado")
else :
    print("Acesso negado")
        