casa = int(1)
quantidade = int(1)
total = int(0)

while casa <=64:
    total = total + quantidade
    quantidade = quantidade * 2
    casa = casa + 1

print("O total de grãos é %s" % (total))