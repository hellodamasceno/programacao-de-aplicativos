def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"

assert situacao_aluno(8) == "Aprovado"
assert situacao_aluno(5.9) == "Reprovado"
assert situacao_aluno(0) == "Reprovado"
assert situacao_aluno(10) == "Aprovado"
assert situacao_aluno(-1) == "Reprovado" #texto importante

# O 6 e 5.9 é caso limite pq é one o sistema  muda de direção 