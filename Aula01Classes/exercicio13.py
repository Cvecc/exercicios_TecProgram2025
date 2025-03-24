#Crie uma classe Produto com os atributos nome e preco. Adicione um método aplicar_desconto(desconto) que aplica um desconto ao preço do produto.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    @classmethod
    def aplicar_desconto(self, desconto):
        desconto = self.preco - (self.preco*0.10)