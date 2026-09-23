numero = int(input("Digite um numero de 1 a 4: "))

match numero:
    case 1:
        print("Tela cadastro")
    case 2:
        print("Tela consulta")
    case 3:
        print("Tela de relaórios")
    case 4:
        print("Saindo do sistema")    
    case _:
        print("Opção incoreta")            