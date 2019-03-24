def ordena(vetor):
	for i in range(0,len(vetor)-1):
		for j in range(1,len(vetor)):
			if vetor[j-1] < vetor[j]:
				aux = vetor[j-1]
				vetor[j-1] = vetor[j]
				vetor[j] = aux
	return vetor

numeroDeCasosDeTeste = int(input())
while numeroDeCasosDeTeste > 0:
	fila = []
	numeroDeAlunos = int(input())

	entrada = input().split(" ")	
	for i in range(0, len(entrada)):
		fila.append(int(entrada[i]))


	ordenada = ordena(fila.copy())
	naoTrocou = 0
	for i in range(0,len(fila)):
		if fila[i] == ordenada[i]:
			naoTrocou = naoTrocou + 1
	print(naoTrocou)
	
	numeroDeCasosDeTeste = numeroDeCasosDeTeste - 1