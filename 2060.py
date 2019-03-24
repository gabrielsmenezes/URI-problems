n = int(input())

entrada = input().split(" ")

lista = []

for x in range(0, len(entrada)):
	lista.append(int(entrada[x]))

for i in range(2,6):
	contador = 0
	for j in range(0,len(lista)):
		if lista[j] % i == 0:
			contador = contador + 1
	print(contador, "Multiplo(s) de", i)