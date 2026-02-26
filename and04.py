nome_de_usuario = input ("digite seu nome de usuario: ")
codigo = input("digite seu codigo seceto: ")

if nome_de_usuario == "admin" and codigo == "999":
    print ("Acesso ao servidor liberado. Sistema online")
elif nome_de_usuario != "admin" and codigo !=  "999" :
    print ("Falha na autenticação. Alerta de segurança ligado")
