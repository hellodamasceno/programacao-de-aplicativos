vagas =  ["Ocupado", "Livre", "Ocupado", "Livre"]
usuario =float(input("Digite o numero da vaga: "))

if usuario %2 == 0 and vagas == "Livre":
    print(f"Vaga {usuario} autorizado para estacionar")

else:
    print(f"Vaga {usuario} indisponivél ou fora de regras")