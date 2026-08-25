def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    return "Reprovado"

assert situacao_aluno(8.5) == "Aprovado"

assert situacao_aluno(6) == "Aprovado"

assert situacao_aluno(4) == "Recuperação"

assert situacao_aluno(3.5) == "Reprovado"


assert situacao_aluno(5.9) == "Recuperação"

assert situacao_aluno(3.9) == "Reprovado"


print("Todos os testes da situação do aluno passaram com sucesso!")
