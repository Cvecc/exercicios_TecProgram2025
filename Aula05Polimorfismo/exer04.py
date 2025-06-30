#Crie um sistema de animais com as classes Passaro e Peixe, ambas com o método movimentar().
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def movimentar(self):
        raise NotImplementedError("Método não implementado nas subclasses.")

class Passaro(Animal):
    def movimentar(self):
        print(f"\nO pássaro {self.nome} está voando.")

class Peixe(Animal):
    def movimentar(self):
        print(f"\nO peixe {self.nome} está nadando.")

animais = [
    Passaro("Calopsita"),
    Peixe("Salmão")
]

for animal in animais:
    animal.movimentar()