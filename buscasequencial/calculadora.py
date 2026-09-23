num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))

operacao = input("Digite a operacao? (+ ou -):  ")

match operacao:
    case "-":
        resultado = num1 - num2
        print(f"Resultado subtração: {resultado}")
    case "+":
        resultado = num1 + num2
        print(f"Resultado soma {resultado}") 
    case _:
        print("Operação inválida")       