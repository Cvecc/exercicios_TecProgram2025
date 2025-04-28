#Crie uma função que solicita ao usuário digitar um número inteiro. Garanta o tratamento de erro para valores inválidos.

try:
    valor = int(input("Digite um valor: "))

except ValueError as error:
    print(f"Error: {error}")