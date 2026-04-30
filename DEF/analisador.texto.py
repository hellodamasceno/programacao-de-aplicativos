def contar_caracteres(palavra):
    if len(palavra) <5:
        print("Nome curto, minímo 5 caracter! ")
    else:
        print("Nome cadastrado! ") 
nome = input("Digite o nome para acesso: ")
contar_caracteres(nome)        