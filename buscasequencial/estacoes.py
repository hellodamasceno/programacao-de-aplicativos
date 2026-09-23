numeros_mes = int(input("Digite o numero: "))

match numeros_mes:
    case 12 | 2 | 1:
        print("Verão")
    case 3 | 4 | 5:
        print("Outono")
    case 6 | 7 | 8:
        print("Inverno")
    case 9| 10| 11:
        print("Primaveira")   
    case _:
        print("Opçao invalida")       