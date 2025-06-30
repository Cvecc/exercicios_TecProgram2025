#Crie Forma com calcular_area(). Crie Quadrado e Círculo e sobrescreva com cálculos reais.
import math
class Forma:
    def calcular_area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

forma1 = Quadrado(6)
forma2 = Circulo(8)

print(f"Área do quadrado: {forma1.calcular_area():.2f}")
print(f"Área do círculo: {forma2.calcular_area():.2f}")