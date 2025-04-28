#Crie uma classe Calculadora com método dividir(a, b). Lance erro se b for zero.
class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def dividir(self):
        if self.b==0:
            raise ZeroDivisionError("O valor de b não pode ser ZERO.")
        resultado = self.a/self.b
        return resultado
try:

    calc1 = Calculadora(10,5)
    calc2 = Calculadora(20,0)
    print(calc1.dividir())
    print(calc2.dividir())
except ZeroDivisionError as error:
    print(error)
