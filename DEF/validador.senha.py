
def senha_valida (senha):
    tentativa = input("Digite a senha: ")


    if len(senha)>= 6:
        print("Acesso liberado")
    else:
        print("Acesso negado ")

    while  tentativa <6:
        tentativa = float(input("Digite a senha: "))

    if senha_valida == tentativa:
     print("Senha cadastrada com sucesso! ")
    else:
        print("Senha incorreta ")         

senha_valida("acesso.") 