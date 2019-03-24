def intParaBinario(n):
	remstack = Stack()
	
	while decNumber > 0:
		rem = decNumber % 2
		remstack.push(rem)
		decNumber = decNumber // 2
	return remstack
entrada = input().split(" ")
A = intParaBinario(entrada[0])
B = intParaBinario(entrada[1])

print(A)
print(B)