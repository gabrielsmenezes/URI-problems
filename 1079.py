n = int(input())

while(n > 0):
	entrada = input().split(" ")
	peso = [2, 3, 5]
	
	for i in range(0,len(entrada)):
		entrada[i] = float(entrada[i]) * peso[i]

	media = (entrada[0] + entrada[2] + entrada[1]) / 10

	print(round(media, 1))

	n = n - 1