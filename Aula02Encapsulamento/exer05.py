#Implemente uma classe Produto onde o atributo privado __preco pode ser acessado através de um método público get_preco().
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco
    
    def get_preco(self):
        print(f"\nNome do produto: {self.nome}\nPreço: R${self.__preco: .2f}")
    
produto1 = Produto("Arroz", 30)
produto2 = Produto("Feijão", 20)

produto1.get_preco()
produto2.get_preco()