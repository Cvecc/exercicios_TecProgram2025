#Crie uma função que recebe a idade de uma pessoa. Se a idade for menor que 0, use raise para lançar uma exceção personalizada.

def validar_idade():
    idade = int(input("Digite uma idade: "))
    if idade < 0:
        raise ValueError("Digite uma idade maior do que zero.")
    print(f"Idade válida: {idade}")

try:
    validar_idade()
except ValueError as error:
    print(error)