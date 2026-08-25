def pode_entrar(idade, acompanhado):
    if idade >= 18 or acompanhado:
        return True
    return False 

assert pode_entrar(25, False) == True, "Erro: maior de idade desacompanhado deveria entrar"

assert pode_entrar(16, False) == False, "Erro: Menor de idade deveria estar acompanhado"

assert pode_entrar(17, False) == False, "Erro: deveria estar acompanhado"

assert pode_entrar(30, True) == True, "Erro: Maior de idade desacompanhado deveria entrar"

print("Todos os testes de acesso passaram com sucesso!")