nomes = ["Julia", "Hello", "Aline", "José"]
notas = [8, 6, 3, 2]

for n in notas:
    if n >=6:
        indice = notas.index(n)
        print(nomes[indice])
