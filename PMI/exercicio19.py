print("Digite 2 números reais")
num1 = float(input())
num2 = float(input())

if num1 > num2:
    print("O número %s é o maior valor" % (num1))
elif num1 == num2:
    print("Os valores são iguais!")
else:
    print("O número %s é o maior valor" % (num2))