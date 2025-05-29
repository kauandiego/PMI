print("Quantas horas de viagem?")
horas = float(input())
print("A quantos km/h o carro viaja?")
velocidade = float(input())

km = velocidade * horas
gasosa = km / 12

print("São gastos %sL de gasolina" % (gasosa))