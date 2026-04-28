def converter_km_para_ms(velocidade_km):
    velocidade_km = velocidade_km / 3.6

velocidade = int(input("Qual a velocidade atual? "))

if velocidade >80:
    converter = converter_km_para_ms(velocidade)
    print(f"A velocidade convertida:  {converter}")
    print("Reduza a velocidade ")
else:
    print("Velocidade normal ")    

converter_km_para_ms()