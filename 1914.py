def function(entrada, paridade):
	if entrada[1] == paridade:
		print(entrada[0])
	else:
		print(entrada[2])



numeroDeCasosDeTestes = int(input())



while numeroDeCasosDeTestes > 0:
	entrada = input().split(" ")
	entrada2 = input().split(" ")

	soma = int(entrada2[0])+int(entrada2[1])

	if soma % 2 == 0:
		function(entrada, "PAR")
	else:
		function(entrada, "IMPAR")

	numeroDeCasosDeTestes = numeroDeCasosDeTestes - 1