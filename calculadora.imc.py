altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = (peso /altura**2)

if (peso /altura**2) >25:
    print(imc)
    print("SOBREPESO")