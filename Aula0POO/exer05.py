"""
Crie um programa que calcule o salário líquido de um funcionário. O salário bruto é dado pelo usuário, e o programa deve descontar:
INSS (10%)
Imposto de Renda (IR) de acordo com a faixa salarial:
Até R$ 2.000,00: isento
De R$ 2.001,00 até R$ 5.000,00: 10%
Acima de R$ 5.000,00: 20%
"""

salario_bruto = float(input("Digite o valor do seu salário bruto: R$ "))
inss = salario_bruto * 0.10

if salario_bruto <= 2000:
    imposto = 0
elif 2001 <= salario_bruto <= 5000:
    imposto = salario_bruto * 0.10
else:
    imposto = salario_bruto * 0.20

salario_liquido = salario_bruto - imposto - inss

print("O seu salário líquido é de", salario_liquido, "reais")