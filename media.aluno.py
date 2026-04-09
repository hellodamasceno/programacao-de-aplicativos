nota01 = float(input("Digite a nota 01: "))
nota02 = float(input("Digite a nota 02: "))
nota03 = float(input("Digite a nota 03: "))
nota04 = float(input("Digite a nota 04: "))
media = 0.0

lista = []

lista.append (nota01)
lista.append(nota02)
lista.append(nota03)
lista.append(nota04)

for nota in lista:
    media += nota

media_final = media / 4

print(f"Media: {media}")

if media_final >=7:
    print("Aprovado")
elif media_final >=5 and media_final  >6.9:
    print("Recuperação")
else:
    print("Reprovado")


