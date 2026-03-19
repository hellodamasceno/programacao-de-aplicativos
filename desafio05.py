Autorizados = ["Alice", "Bob", "Carlos"]
usuario = input ("Digite o nome de um pesquisador: ")

if usuario in Autorizados:
    indice = Autorizados.index(usuario)
    print(f"Acesso Permitido! O pesquisador {usuario} está na posição {indice}.")
    
    remover = input("Deseja remover esse pesquisador da lista? ")
    if remover == "sim":
        autorizados.remove(usuario)
        print(f"Lista atualizada: {Autorizados}")

else:
    print(f"Acesso Negado! O pesquisador {usuario} não foi encontrado.")
    
    # Opção de cadastrar
    cadastrar = input("Deseja cadastrar esse novo pesquisador? ")
    if cadastrar == "sim":
        Autorizados.append(usuario)
        print(f"Lista atualizada: {Autorizados}")        

