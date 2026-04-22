def avaliar_desempenho(nota):

    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
       return "Bom"
    elif nota >5:
        return "Regular"
    else:
        return "Insuficiente"    


nota_usuario= float(input("Digite a nota: "))

mensagem=avaliar_desempenho(nota_usuario) 
print(mensagem)