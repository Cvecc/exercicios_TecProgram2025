#Crie um sistema de streaming com as classes Filme e Musica, ambas com o método reproduzir().
class Streaming:
    def __init__(self,nome):
        self.nome = nome 
    def reproduzir(self):
        raise NotImplementedError("Método não implementado pelas subclasses.")
    
class Filme(Streaming):
    def __init__(self, nome):
        super().__init__(nome)
    def reproduzir(self):
        print(f"\nReproduzindo Filme: {self.nome}")

class Musica(Streaming):
    def __init__(self, nome):
        super().__init__(nome)
    def reproduzir(self):
        print(f"\nReproduzindo a música: {self.nome}")

sistema = [Filme("Harry Potter e a Pedra Filosofal."), Musica("No Mercy.")]

for Streaming in sistema:
    Streaming.reproduzir()