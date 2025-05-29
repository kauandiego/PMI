print("Digite três valores na ordem crescente. Digite o primeiro?")
num1 = int(input())
print("Digite o segundo")
num2 = int(input())
print("Digite o terceiro.")
num3 = int(input())
print("Digite outro número, não precisando estar em ordem")
num4 = int(input())

if num4 > num3:
    print("Números em ordem: %s, %s, %s, %s" % (num1, num2, num3, num4))
elif num4 < num1:
    print("Números em ordem: %s, %s, %s, %s" % (num4, num1, num2, num3))
elif num4 > num1 and num4 < num2:
    print("Números em ordem: %s, %s, %s, %s" % (num1, num4, num2, num3))
elif num4 > num2 and num4 < num3:
    print("Números em ordem: %s, %s, %s, %s" % (num1, num2, num4, num3))