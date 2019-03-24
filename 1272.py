def filtraPalavras(palavrasComEspacos):
	i = 0
	palavras = list()
	while True:
		while i < len(palavrasComEspacos) and palavrasComEspacos[i] == ' ':
			i = i + 1

		j = i

		while j < len(palavrasComEspacos) and palavrasComEspacos[j] != ' ':
			j = j + 1
		if palavrasComEspacos[i:j] != '':
			palavras.append(palavrasComEspacos[i:j])
		i = j

		if i == len(palavrasComEspacos):
			break
	return palavras

numeroDeCasos= int(input())

while numeroDeCasos > 0:

	palavras = filtraPalavras(input())

	for palavra in palavras:
		print(palavra[0], end='')
	print()


	numeroDeCasos = numeroDeCasos - 1

