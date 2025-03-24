#Crie uma classe Calculadora com um método estático somar(a, b) que retorna a soma de dois números.

class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b
    
calculo = Calculadora.somar(279, 682)
print(f"A soma dos números é: {calculo: .2f}")