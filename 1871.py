
entrada = input().split(" ")
a = int(entrada[0])
b = int(entrada[1])

while( a != 0 and b != 0):
    resultado = a + b
    resultado = str(resultado)
    resultado = resultado.replace('0','')
    print(resultado)
    
    entrada = input().split(" ")
    a = int(entrada[0])
    b = int(entrada[1])