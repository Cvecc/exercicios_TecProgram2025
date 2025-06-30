#Crie uma função calcular_media(notas) que recebe uma lista de notas e retorna a média.

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    soma = sum(notas)
    media = soma / len(notas)
    return media

notas = input("Digite as notas separadas por espaço: ").split()

notas = [float(nota) for nota in notas]

resultado = calcular_media(notas)
print(resultado)