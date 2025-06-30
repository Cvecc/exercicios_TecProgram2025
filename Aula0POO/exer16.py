#Crie uma função calculadora(a, b, operacao) que recebe dois números e uma operação (+, -, *, /) e retorna o resultado.

def calculadora(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")


resultado = calculadora(a, b, operacao)
print("Resultado:", resultado)