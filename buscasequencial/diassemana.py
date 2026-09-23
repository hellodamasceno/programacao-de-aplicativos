nome_dia = input("Digite o dia da semana: ")
 
match nome_dia:
    case "Sabado" | "Domingo":
        print("Fim de semana")
    case "Segunda" | "Terça" | "Quarta"| "Quinta" | "Sexta":
        print("Dia util")
    case _:
        print("Texto invalido")    