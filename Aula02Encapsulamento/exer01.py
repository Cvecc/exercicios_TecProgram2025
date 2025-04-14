#Crie uma classe Produto com um atributo público nome e um método exibir_nome() que exibe o nome do produto.
class Produto:
    def __init__(self, nome):
        self.nome = nome
    
    def exibir(self):
        print(f"\nNome do produto: {self.nome}")

produto1 = Produto("Uva")
produto2 = Produto("Banana")
produto3 = Produto("Alface")
produto4 = Produto("Tomate")

produto1.exibir()
produto2.exibir()
produto3.exibir()
produto4.exibir()