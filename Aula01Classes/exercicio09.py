#Crie uma classe Loja com o atributo de classe desconto. Adicione um método de classe aplicar_desconto() que modifica o valor do desconto para todas as instâncias.

class Loja:
    desconto = 0.1
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco

    def produto_desconto(self):
        self.reduz = self.preco*Loja.desconto
        self.final = self.preco - self.reduz
    
    def exibir(self):
        self.produto_desconto()
        print(f"Produto: {self.produto}")
        print(f"Preço do produto: R${self.preco: .2f}")
        print(f"Preço final com desconto: R${self.final: .2f}\n")
    
    @classmethod
    def aplicar_desconto(cls, novo):
        cls.desconto = novo
    @classmethod
    def exibir_novo(cls):
        print(f"\nNovo desconto de: {Loja.desconto}\n")

produto1 = Loja("Garrafa", 15)
produto2 = Loja("Travesseiro", 50)
produto1.exibir()
produto2.exibir()

Loja.aplicar_desconto(0.15)
Loja.exibir_novo()
produto1.exibir()
produto2.exibir()