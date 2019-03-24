diametro = int(input())

entrada = input().split()

altura = int(entrada[0])

largura = int(entrada[1])

profundidade = int(entrada[2])

if altura>=diametro and largura>=diametro and profundidade>=diametro:
	print('S')
else:
	print('N')