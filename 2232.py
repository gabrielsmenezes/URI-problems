numCasos = int(input())

while numCasos > 0:
	numDeLinhas = int(input())

	soma = 0

	for x in range(0,numDeLinhas):
		soma = soma + 2**x

	print(soma)

	numCasos = numCasos - 1