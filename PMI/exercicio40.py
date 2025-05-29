numero1 = int(input("Digite dois números inteiros: "))
numero2 = int(input())

if numero1 > numero2:
    primo = numero2 +1
    n = int()
    while primo < numero1:
        n = 2
        while n <= primo:
            if n == primo:
                print(primo, end=" ")
                break
            elif primo % n == 0:
                break
            else:
                n = n + 1
        primo = primo + 1

if numero2 > numero1:
    primo = numero1 +1
    n = int()
    print("Os números primos entre esses dois números são:", end=" ")
    while primo < numero2:
        n = 2
        while n <= primo:
            if n == primo:
                print(primo, end=" ")
                break
            elif primo % n == 0:
                break
            else:
                n = n + 1
        primo = primo + 1



