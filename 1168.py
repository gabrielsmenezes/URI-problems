mapaDeLeds = [6, 2, 5, 5, 4, 5 ,6 , 3, 7, 6]


casos = int(input())

while casos > 0:

	entrada = input()

	numeroDeLeds = 0

	for digito in entrada:
		# print(int(digito), end='')
		numeroDeLeds = numeroDeLeds + mapaDeLeds[int(digito)]	

	print(numeroDeLeds, 'leds')

	casos = casos - 1