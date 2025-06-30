#Crie uma função que recebe dois números e tenta retornar a divisão entre eles. Capture erro de divisão por zero.

class Divisao:
    def dividir(n1, n2):
        try:
            resultado = n1/n2
            return resultado
        
        except ZeroDivisionError:
            return "Erro: Não é possível dividir por zero."
        
print(Divisao.dividir(10, 2))
print(Divisao.dividir(5, 0))
print(Divisao.dividir(50, 5))