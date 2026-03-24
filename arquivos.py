lista_pendentes = ["Relatorio.pdf", "Foto.png", "Planilha.xlsx"] 
lista_concluidos = []


lista_concluidos.append(lista_pendentes[0])
lista_pendentes.pop(1)

print(f"Lista atualizada: {lista_concluidos}, {lista_pendentes}")