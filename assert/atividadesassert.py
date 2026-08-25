def eh_par(numero):
    return numero % 2 == 0

assert eh_par(4) == True, "Erro: 4 deveria ser considerado par"

assert eh_par(7) == False, "Erro: 7 não deveria ser considerado par"


assert eh_par(0) == True, "Erro: 0 deveria ser considerado par"


assert eh_par(-2) == True, "Erro: -2 deveria ser considerado par"
assert eh_par(-3) == False, "Erro: -3 não deveria ser considerado par"

print("Todos os testes passaram com sucesso!")