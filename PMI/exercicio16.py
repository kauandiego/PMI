print("Quantas horas trabalhadas?")
horas = int(input())
print("Quanto recebe por hora?")
valorhora = float(input())
print("Qual o percentual de desconto sobre o salário?")
desconto = float(input()) / 100
print("Quantos dependentes?")
dependente = int(input())

salario = (horas * valorhora) * (1 - desconto) + (100 * dependente)

print("Salario equivale a %s" % (salario))