#Crie um programa que calcule a comissão de um vendedor, com base nas vendas realizadas. O vendedor ganha 5% de comissão sobre as vendas, mas existe um bônus de R$ 200,00 se ele vender mais de R$ 10.000,00 no mês.
#Fórmula:
#Comissão = 5% do valor das vendas
#Se as vendas forem acima de R$ 10.000,00 adicionar o bônus de R$ 200.

venda = float(input("Digite o valor da(s) venda(s) em reais: "))
comissao = venda * 0.05

if venda >= 10000:
    comissao += 200

print("Comissão total:", comissao, "reais")