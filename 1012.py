entrada = input().split(" ")

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

# a) a area do triangulo retangulo que tem A por base e C por altura. 
areaDoTriangulo = (A * C) / 2
# b) a area do circulo de raio C. (pi = 3.14159)
areaDoCirculo = (C * C) *  3.14159
# c) a area do trapezio que tem A e B por bases e C por altura.
areaDoTrapezio = ((A+B) / 2) * C
# d) a area do quadrado que tem lado B.
areaDoQuadrado = B * B
# e) a area do retangulo que tem lados A e B. 
areaDoRetangulo = A * B

print("TRIANGULO: %0.3f" % round(areaDoTriangulo, 3))
print("CIRCULO: %0.3f" % round (areaDoCirculo, 3))
print("TRAPEZIO: %0.3f"% round (areaDoTrapezio, 3))
print("QUADRADO: %0.3f"% round (areaDoQuadrado, 3)) 
print("RETANGULO: %0.3f" % round (areaDoRetangulo, 3))