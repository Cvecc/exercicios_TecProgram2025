"""
Crie um programa que simule um desconto progressivo em uma compra. O cliente recebe:
10% de desconto se o valor da compra for até R$ 500.
15% de desconto se o valor da compra for entre R$ 501 e R$ 1000.
20% de desconto se o valor da compra for acima de R$ 1000.
O programa deve pedir o valor total da compra e aplicar o desconto correspondente.
"""

compra = float(input("Digite o valor da compra em reais:  "))

if compra < 500:
    desconto = compra * 0.10
elif 500 <= compra <= 1000:
    desconto = compra * 0.15
else:
    desconto = compra * 0.20

valor_final = compra - desconto

print("Seu desconto foi de", desconto,"reais")
print("O valor final da compra é ", valor_final,"reais")