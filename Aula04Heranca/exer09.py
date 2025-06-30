#Crie Personagem com vida e forca. Crie Guerreiro e Mago, cada um com habilidade própria.
class Personagem:
    def __init__(self, vida, forca):
        self.vida = vida
        self.forca = forca

class Guerreiro(Personagem):
    def habilidade(self):
        return "Ataca com espadão"

class Mago(Personagem):
    def habilidade(self):
        return "Lança bola de fogo"

guerreiro= Guerreiro(vida=150, forca=60)
mago= Mago(vida=80, forca=100)

print(f"\nGuerreiro: {guerreiro.habilidade()}")
print(f"\nMago: {mago.habilidade()}")