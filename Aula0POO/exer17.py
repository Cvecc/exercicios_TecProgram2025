#Crie uma função eh_par(numero) que recebe um número e retorna True se for par e False se for ímpar.

numero = float(input("Digite um número para descobrir se é par ou ímpar:"))

def eh_par(numero):
    if numero % 2 == 0:
        print("É par")
        return True
    else:
        print("Não é par")
        return False
eh_par(numero)