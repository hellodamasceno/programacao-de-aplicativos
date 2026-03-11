codigo_pacote = int(input("Digite o codigo do pacote:"))
peso = float(input("Digite o peso: "))

if peso > 50:
    print("Carga Pesada")

elif peso < 5 and codigo_pacote % 10 == 0:
    print("Entrega Expressa")
else:
    status = "Entrega Padrão"

print(f"Pacote {codigo_pacote}: {peso}")
