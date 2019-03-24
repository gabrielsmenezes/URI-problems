entrada = input().split(' ')

P1 = int(entrada[0])
C1 = int(entrada[1])
P2 = int(entrada[2])
C2 = int(entrada[3])

esq = P1 * C1
dire = P2 * C2

if esq > dire:
	print('-1')
elif dire > esq:
	print('1')
else:
	print('0')