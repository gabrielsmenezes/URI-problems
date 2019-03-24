qtdProdComprados = int(input())

dic = {'1001' : 1.50, '1002' : 2.50, '1003' : 3.50, '1004' : 4.50, '1005' : 5.50}

soma = 0

while qtdProdComprados > 0:


	entrada = input().split(" ")

	soma = soma + (dic[entrada[0]] * int(entrada[1]))

	qtdProdComprados = qtdProdComprados - 1

print("%0.2f" % soma)