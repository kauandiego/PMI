investimento = float(input("Qual foi o valor do investimento\n"))
caso = int(input("Digite 1 para poupança e 2 para renda fixa\n"))

match caso:
    case 1:
        investimento = investimento * float(1.03)
        print(investimento)
    case 2:
        investimento = investimento * float(1.05)
        print(investimento)
