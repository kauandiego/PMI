print("Digite as 4 notas bimestrais do aluno")
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
media = (nota1 + nota2 + nota3 +nota4) / 4

print("A média do aluno é %s e ele está..." % (media))

if media >= 6:
    print("APROVADO")
elif media >= 3 and media < 6:
    print("De recuperação.")
else:
    print("Reprovado!?")