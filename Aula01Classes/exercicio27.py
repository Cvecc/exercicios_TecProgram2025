#Crie uma classe Produto com os atributos nome e preco. Adicione um método de instância mostrar_info() que retorna uma string com os dados do produto.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def mostrar_info(self):
        print(f"Nome do produto: {self.nome}")
        print(f"Preço do produto: R${self.preco: .2f}\n")

produto1 = Produto("Shampoo", 24.99)
produto2 = Produto("Escova de cabelo", 15)
produto3 = Produto("Celular", 2950)

produto1.mostrar_info()
produto2.mostrar_info()
produto3.mostrar_info()