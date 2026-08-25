def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)

assert calcular_desconto(200,50) == 100.00, "Erro: metade de 200 deveria ser 100"

assert calcular_desconto(30, 10) == 27.0, "Erro: 10% de 30 deveria dar 27"

assert calcular_desconto(0, 10) == 0.0, "Erro: Produto de preço zero deve continuar zero"

print("Parabéns! Todos os asserts passaram.")
