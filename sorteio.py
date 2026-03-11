id = int(input("digite seu ID:"  ))
valor_da_compra = int(input("digite o valor total da compra:"))

if id % 2 == 0  and valor_da_compra >= 500.00 :
    print(f"Parabéns, usuário {id}! Você ganhou um cupom para sua compra de R$ {valor_da_compra}")
else:
    print(f"obrigado pela compra, usuário {id}. Continue acompanhando nossas promoções!")    