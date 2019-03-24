casosDeTeste = int(input())

impares = list()

pares = list()

while casosDeTeste > 0:

	numero = int(input())

	if numero % 2 == 0:
		pares.append(numero)
	else:
		impares.append(numero)

	casosDeTeste = casosDeTeste - 1

pares.sort()

impares.sort(reverse=True)

for numero in pares:
	print(numero)
for numero in impares:
	print(numero)