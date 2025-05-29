print("Digite 2 números reais")
num1 = float(input())
num2 = float(input())

if num1 > num2:
    dif = num1 - num2
    print("A diferença entre os dois é de %s" % (dif))
elif num1 == num2:
    print("Não há diferença!")
else:
    dif = num2 - num1
    print("A diferença entre os dois é de %s" % (dif))