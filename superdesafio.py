livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []
escolha_usuario= input ("Digite o nome de um livro: ")


if escolha_usuario in livros_disponiveis :
    indice = livros_disponiveis.index(escolha_usuario)
    livros_emprestados.append(escolha_usuario)
    livros_disponiveis.pop(indice)
    print("Empréstimo realizado com sucesso!")
    print(F"Lista atualizada: DISPONIVEIS: {livros_disponiveis} , EMPRESTADOS: {livros_emprestados}")

else:
    print("Desculpe, este livro não está no acervo ")
print("-------------------------------------")

devolução = input("Digite o nome do livro para devolução: ")

if devolução in livros_emprestados:
    indice2 = livros_emprestados.index(devolução)
    livros_disponiveis.append(devolução)
    livros_emprestados.pop(indice2)
    print("Devolução concluida")
    print(f"Lista atualizada: EMPRESTADOS: {livros_emprestados}, DISPONIVEIS: {livros_disponiveis}")

else:
    print("Este livro não consta como emprestado.")    


del livros_disponiveis[0:2]   
print ("Relatorio final: ", livros_disponiveis)