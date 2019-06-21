class Time:
    def __init__(self, vitorias, empates, saldo):
        self.vitorias = int(vitorias)
        self.empates = int(empates)
        self.saldo = int(saldo)
        self.pontos = (self.vitorias * 3) + self.empates

entrada = input().split(" ")

Cormengo = Time(entrada[0], entrada[1], entrada[2])

Flaminthians = Time(entrada[3], entrada[4], entrada[5])

vencedor = "="

if (Cormengo.pontos > Flaminthians.pontos):
    vencedor = "C"
elif (Flaminthians.pontos > Cormengo.pontos):
    vencedor = "F"
else:
    if(Cormengo.saldo > Flaminthians.saldo):
        vencedor = "C"
    elif(Flaminthians.saldo > Cormengo.saldo):
        vencedor = "F"
print(vencedor)