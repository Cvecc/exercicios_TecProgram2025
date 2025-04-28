#Crie uma função que valida um CPF. Se tiver menos de 11 caracteres, lance uma exceção.
def validar_cpf():
    cpf = input("Digite o CPF: ")
    if len(cpf) != 3:
        raise ValueError("CPF deve conter 11 caracteres.")
    print(f"CPF: {cpf} Cadastrado com sucesso.")

try:
    validar_cpf()
except ValueError as error:
    print(error)