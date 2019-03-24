numeroDePessoas = int(input())

pessoas = input().split(' ')

menor = pessoas.copy()

menor.sort()

menor = menor[0]

print( str (pessoas.index(menor) + 1 ) )