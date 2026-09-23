
nota = input("Digite a nota em letra (A, B, C, D ou F): ").upper()

match nota:
    case "A" | "B":
        print("Excelente desempenho")
    case "C" | "D":
        print("Desempenho mediano")
    case "F":
        print("Reprovado")
    case _:  
        print("Conceito inválido")
