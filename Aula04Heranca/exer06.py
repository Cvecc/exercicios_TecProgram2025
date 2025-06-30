#Crie SerVivo, Animal, Passaro com métodos de identificação.
class SerVivo:
    def identificar(self):
        return "-- É um Ser vivo"

class Animal(SerVivo):
    def identificar(self):
        return "\nÉ um Animal"

class Passaro(Animal):
    def identificar(self):
        return "\nÉ um Pássaro"

print(SerVivo().identificar())
print(Animal().identificar())  
print(Passaro().identificar()) 