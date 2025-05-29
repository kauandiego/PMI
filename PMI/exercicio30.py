anonascimento = int(input("Em que ano nasceu? "))
mesnascimento = int(input("Em que mês nasceu? "))
dianascimento = int(input("Em que dia nasceu? "))

anoatual = int(input("Em que ano estamos? "))
mesatual = int(input("Em que mês estamos? "))
diaatual = int(input("Em que dia estamos? "))

#anos e meses
if mesatual < mesnascimento:
    anos = int(anoatual - anonascimento - 1)
    if anos < 0:
        anos = 0
    meses = int(12 * anos + mesatual - 1)
elif mesatual == mesnascimento:
    if diaatual < dianascimento:
        anos = int(anoatual - anonascimento - 1)
        meses = int(12 * anos + mesatual - 1)
    else:
        anos = int(anoatual - anonascimento)
        meses = int(12 * anos + mesatual - 1)

#dias
contador = int(0)
anosbi = int(0)
while contador <= anos:
    if anonascimento % 4 == 0:
        anosbi = anosbi + 1
    contador = contador + 1
    anonascimento = anonascimento + 1
dias = int(0)
contador = int(1)
if mesatual > 1:
    while contador < mesatual:
        if contador < 8:
            if contador % 2 != 0:
                dias = int(dias + 31)
            if contador % 2 == 0:
                if contador == 2 and anoatual % 4 == 0:
                    dias = int(dias+29)
                elif contador == 2 and anoatual % 4 != 0:
                    dias =int(dias+28)
                else:
                    dias = int(dias+30)
        else:
            if contador % 2 != 0:
                dias = int(dias + 30)
            if contador % 2 == 0:
                dias = int(dias + 31)
        contador = contador + 1
    dias = int(int(diaatual + (365 * anos) - anosbi))
else:
    dias = int(diaatual + (365 * anos) - anosbi)

print("Você tem %s anos, %s meses e %s dias de vida!" % (anos, meses, dias))
