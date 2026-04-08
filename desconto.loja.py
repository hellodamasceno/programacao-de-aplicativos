valor_compra = float(input("Digite o valor da compra: "))
desconto = 0.0

if valor_compra > 100:
    multiplicacao = valor_compra * 0.10
    sub = valor_compra - multiplicacao
    print(f"Valor da compra com desconto: {sub}")
    
else:
    print(f"Voce não atingiu o valor para o desconto, valor da compra: {valor_compra}")    
