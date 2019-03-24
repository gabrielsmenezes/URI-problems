def verificarNotas(valor):
	marcador=[0,0,0,0]


	while int(valor / 50) > 0:
		resultado = int(valor / 50)
		valor = valor % 50
		marcador[0] = marcador[0] + resultado

	while int(valor / 10) > 0:
		resultado = int(valor / 10)
		valor = valor % 10
		marcador[1] = marcador[1] + resultado

	while int(valor / 5) > 0:
		resultado = int(valor / 5)
		valor = valor % 5
		marcador[2] = marcador[2] + resultado

	while int(valor / 1) > 0:
		resultado = int(valor / 1)
		valor = valor % 1
		marcador[3] = marcador[3] + resultado



	return marcador

valor = int(input())
numeroDoTeste = 0
while valor != 0:

	numeroDoTeste = numeroDoTeste + 1

	print("Teste", numeroDoTeste)
	vetor = verificarNotas(valor)
	for x in range(0,len(vetor) - 1):
		print(vetor[x], end=' ')
	print(vetor[len(vetor)-1])
	print("")

	valor = int(input())