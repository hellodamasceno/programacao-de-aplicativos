mercadoria = int(input("Digite o numero: "))

match mercadoria:
    case 1 | 2:
        print("Alimentos Perecíveis")
    case 3 |4:
        print("Bebidas")    
    case 5:
        print("Produtos de limpeza") 
    case _:
        print("Codigo não cadastrado")       