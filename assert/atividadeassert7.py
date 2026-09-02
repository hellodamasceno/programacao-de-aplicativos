def calcular_situacao_aluno(nota1, nota2):
   
    media = (nota1 + nota2) / 2
    
    
    if media > 7:
        return "Aprovado"
     
    elif media > 5:
        return "Recuperacao"
    else:
        return "Reprovado"