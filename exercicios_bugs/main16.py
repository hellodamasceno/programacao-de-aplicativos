def menu():
    while True:
        print("1. cadastrar aluno")
        print("2. sair")
        opcao= input("Escolha: ")

        if opcao == "1":
            print("Cadastrando...")
        elif opcao == "2":
            print("Saindo do programa.")
        break
#o menu continua rodando pq não colocamos o break, para fechar o laco infinito            
menu()