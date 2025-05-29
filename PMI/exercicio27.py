print("Quantas voltas tem o circuito?")
voltas = int(input())
print("Quanto mede o circuito em metros?")
medida = float(input())
print("Qual a duração do circuito em minutos?")
tempo = int(input())
total = voltas * medida
velocidademedia = total / tempo
print(velocidademedia)