termo = int(input("Até qual termo irá a sequência de Fibonacci? "))
n = int(1)
termoatual = int(0)
termoanterior1= int(1)
termoanterior2= int(0)
while n <= termo:
    if n == 1:
        print(1, end=" ")
        n = n + 1
    else:
        termoatual = termoanterior1 + termoanterior2
        termoanterior2 = termoanterior1
        termoanterior1 = termoatual
        print(termoatual, end=" ")
        n = n + 1
