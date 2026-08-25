def dobrar(numero):
 	return numero * 2

assert dobrar(3) == 6
assert dobrar(0) == 1
assert dobrar(-2) == -4

# o assert da linha 5 falhou, pq todo numero multilicado por zero é zero então deveria retornar zero.
#esperava 0 na resposta.
