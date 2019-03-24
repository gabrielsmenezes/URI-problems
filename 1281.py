n = int(input())


while n > 0:

	produtosDaFeira = {}

	m = int(input()) #numero de produtos na feira

	for i in range(1,m+1):
		
		entrada = input().split(" ")
		produtosDaFeira[entrada[0]] = float(entrada[1])

	p = int(input())

	valorTotal=0

	for i in range(1,p+1):
		entrada = input().split(" ")
		valorTotal = valorTotal + (produtosDaFeira[entrada[0]] * int(entrada[1]))

	print("R$ %0.2f" % valorTotal)
	n = n -1