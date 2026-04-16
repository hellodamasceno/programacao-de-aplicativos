nomes = ["Hello", "Jose", "Maria", "Lauana"]
nome_antigo = input("Digite o nome que deseja mudar: ")
nome_novo = input("Digite o nome novo: ")
  

for i in range(len(nomes)):
    if nomes[nome_antigo] == nome_antigo:
        nomes[nome_novo] = nome_novo

print("Lista atualizada: ", nomes)         