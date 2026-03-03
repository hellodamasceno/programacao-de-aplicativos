média = int(input("informe sua média: "))
renda = float(input("infome sua renda: "))
escolaridade = input("veio de escola publica: ")

if média >= 8.0 and (renda >2000.00 or escolaridade == "SIM") :
    print("Ganhou a bolsa. ")
else:
    print("Não atende aos requisitos. ")    