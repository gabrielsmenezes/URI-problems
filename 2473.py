valores = ['azar', 'azar', 'azar', 'terno', 'quadra', 'quina', 'sena']

entrada = input().split(' ')

apostaDoFlavinho = set()

for numero in entrada:
	apostaDoFlavinho.add(int(numero))

entrada = input().split(' ')

apostaGanhadora = set()

for numero in entrada:
	apostaGanhadora.add(int(numero))

numerosAcertadosPorFlavinho = apostaDoFlavinho.intersection(apostaGanhadora)

numeroDeAcertos = len(numerosAcertadosPorFlavinho)

print(valores[numeroDeAcertos])