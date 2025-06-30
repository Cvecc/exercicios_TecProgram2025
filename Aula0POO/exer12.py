#O programa escolhe um número aleatório entre 1 e 10, e o usuário tem que adivinhar. Ele só para quando o número correto for digitado.

import random

numero_secreto = random.randint(1, 10)

while True:
    resposta= int(input("Adivinhe o número entre 1 e 10: "))

    if resposta == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Errou, tente novamente.")