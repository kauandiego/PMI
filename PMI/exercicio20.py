print("Qual o valor do coeficiente A?")
coeA = float(input())
print("Qual o valor do coeficiente B?")
coeB = float(input())
print("Qual o valor do coeficiente C?")
coeC = float(input())
delta = coeB ** 2 - 4 * coeA * coeC

if delta < 0:
    print("A equação não possui nenhuma raíz real!")
elif delta == 0:
    raiz1 = (-coeB + delta ** 0.5) / (2 * coeA)
    print("A equação possui somente uma raíz e ela vale %s" % (raiz1))
else:
    raiz1 = (-coeB + delta ** 0.5) / (2 * coeA)
    raiz2 = (-coeB - delta ** 0.5) / (2 * coeA)
    print("Há duas raízes reais. As raízes reais são %s e %s" % (raiz1, raiz2))

