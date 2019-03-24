def fatorial(x):
	resultado = 1
	while (x > 0):
		resultado = resultado * x
		x = x -1
	return resultado


entrada = int(input())
fat = entrada
numeroDeFatoriais = 0

while(entrada > 0 and fat > 0):
	aux = fatorial(fat)
	if aux <= entrada:
		numeroDeFatoriais = numeroDeFatoriais + 1
		entrada = entrada - aux
	else:
		fat = fat - 1

print(numeroDeFatoriais)