casos = int(input())

while casos > 0:

	entrada = input()

	parte1 = entrada.split('k')[0]
	parte2 = entrada.split('k')[1]

	numeroDeA = parte1.count('a')
	numeroDeB = parte2.count('a')


	print('k', end='')

	count = 0

	while count < numeroDeB*numeroDeA:
		
		print('a', end='')
		count=count+1
	print()
	casos = casos - 1