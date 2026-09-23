vogais = input("Digite a letra: ")

match vogais:
    case "A" | "E"| "I" | "O" | "U":
        print("É uma vogal!")
    case _:
        print("Não é vogal! ")
            