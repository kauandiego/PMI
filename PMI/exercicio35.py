numero1 = int(input("Digite dois números inteiros: "))
numero2 = int(input())

if numero1 > numero2:
    inter = numero2 + 1
    totalimpar = int(0)
    while inter < numero1:
        if inter % 2 !=0:
            totalimpar = totalimpar + inter
        inter = inter + 1
    print("A soma dos números ímpares entre %s e %s é: %s" % (numero2, numero1, totalimpar))
if numero2 > numero1:
    inter = numero1 + 1
    totalimpar = int(0)
    while inter < numero2:
        if inter % 2 !=0:
            totalimpar = totalimpar + inter
        inter = inter + 1
    print("A soma dos números ímpares entre %s e %s é: %s" % (numero1, numero2, totalimpar))