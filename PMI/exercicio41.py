dado1 = int(1)
dado2 = int(1)

while dado2 <7:
    while dado1 < 7:
        if dado1 + dado2 == 7:
            print(dado1, dado2)
            break
        else:
            dado1 = dado1 + 1
    dado2= dado2 + 1
    dado1= 1