#Modifique o programa anterior para contar quantas tentativas o usuário precisou até acertar.

import random

numero_secreto = random.randint(1, 10)


tentativas = 0


while True:
    resposta= int(input("Adivinhe o número entre 1 e 10: "))
    tentativas += 1

    if resposta == numero_secreto:
        print("Parabéns! Você acertou em", tentativas, "tentativas!")
        break
    else:
        print("Errou, tente novamente.")