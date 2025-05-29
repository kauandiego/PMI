from decimal import Decimal

print("Quantos kg de alimento possui?")
alimento = Decimal(input())
i = int(0)
while alimento >= Decimal("0.05"):
    alimento = alimento - Decimal("0.05")
    i = i + 1
print("A pessoa terá comida o suficiente para %s dias!" % (i))