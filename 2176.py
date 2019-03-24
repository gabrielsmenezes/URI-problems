entrada = input()

contadorUm = 0

for caractere in entrada:
	if caractere == "1":
		contadorUm = contadorUm + 1

if contadorUm % 2 == 0:
	entrada = entrada+"0"
else:
	entrada = entrada+"1"

print(entrada)