def situacao_faltas(faltas):

    if 0 <= faltas <= 4:
        return "Regular"
    elif 5 <= faltas <= 10:
        return "Atenção"
    elif faltas >= 11:
        return "Reprovado por falta"
    else:
        return "Número de faltas inválido"

assert situacao_faltas(0) == "Regular"
assert situacao_faltas(4) == "Regular"
assert situacao_faltas(5) == "Atenção"
assert situacao_faltas(10) == "Atenção"
assert situacao_faltas(11) == "Reprovado por falta"

print("Todos os asserts passaram com sucesso!")