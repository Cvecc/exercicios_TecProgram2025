#Peça para o usuário digitar um número positivo. Se ele digitar um valor negativo, peça novamente até ele digitar corretamente.

num = int(input("Digite um número positivo: "))

while num < 0:
    num = int(input("Por favor, digite um número positivo: "))

print("Você digitou o número positivo:", num)