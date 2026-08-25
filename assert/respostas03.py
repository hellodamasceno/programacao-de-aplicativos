def calcular_desconto(preco, percentual):
    return preco - (preco * (percentual / 100))

assert calcular_desconto(100, 10) == 90.0

assert calcular_desconto(200, 20) == 160.0

assert calcular_desconto(50, 50) == 25.0

print("Os testes passaram...")
