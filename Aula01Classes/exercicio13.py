#Crie uma classe Produto com os atributos nome e preco. Adicione um método aplicar_desconto(desconto) que aplica um desconto ao preço do produto.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def aplicar_desconto(self, desconto):
        return self.preco - (self.preco*desconto)
    
    def exibir(self, desconto):
        novo_preco = self.aplicar_desconto(desconto)
        print(f"Nome do produto: {self.nome}")
        print(f"Preço do produto: R${self.preco: .2f}")
        print(f"Preço final com desconto: R${novo_preco: .2f}")

produto1 = Produto("Calculadora", 45)
produto1.exibir(0.10)


