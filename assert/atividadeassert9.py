def buscar_nome(lista, nome):
    return nome in lista

def tem_senha_valida(senha):
    return len(senha) >= 8
assert buscar_nome(["Ana", "Carlos", "Beatriz"], "Carlos") is True


assert buscar_nome([], "Ana") is False
assert tem_senha_valida("") is False

print("Todos os asserts executaram com sucesso! Nenhuma falha encontrada.")