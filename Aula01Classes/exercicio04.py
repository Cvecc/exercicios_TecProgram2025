#Crie uma classe Animal com um atributo de classe categoria. Modifique esse atributo na classe e observe como ele afeta todas as instâncias.

class Animal:
    categoria= "Mamífero"
    def __init__(self, nome):
        self.nome = nome
    def exibir(self):
        print(f"Nome do animal: {self.nome}\nCategoria: {self.categoria}\n")

nome1 = Animal("Cavalo")
nome2 = Animal("Bicho-preguiça")
nome3 = Animal("Leão")

nome1.exibir()
nome2.exibir()
nome3.exibir()

Animal.categoria = "Lindo"

nome1.exibir()
nome2.exibir()
nome3.exibir()