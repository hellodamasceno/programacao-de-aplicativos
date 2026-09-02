
def classificar_temperatura(temperatura):
    
    if temperatura < 15:
        return "Frio"
    
    elif temperatura <= 25:
        return "Agradável"
    else:
        return "Quente"



assert classificar_temperatura(5) == "Frio"

assert classificar_temperatura(15) == "Agradável"

assert classificar_temperatura(20) == "Agradável"

assert classificar_temperatura(25) == "Agradável"

assert classificar_temperatura(25.1) == "Quente"

print("Todos os 5 asserts executaram com sucesso! Nenhuma falha encontrada.")
