while True:
	try:
		entrada = input()
	except Exception as e:
		break;

	entrada = entrada.split(' ')

	alice = entrada[0]

	beto = entrada[1]

	clara = entrada[2]

	if alice == beto and beto == clara:
		print('*')
	elif alice == beto:
		print('C')
	elif beto == clara:
		print('A')
	elif alice == clara:
		print('B')