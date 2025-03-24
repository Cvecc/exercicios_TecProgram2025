#Exercício 3: Atributos de Instância

#Tarefa: Crie uma classe Produto com os atributos nome e preco. Crie uma instância de Produto e modifique o atributo preco.
#Objetivo: Compreender que atributos de instância são específicos de cada objeto.

class Produto:
    def __init__(self, nome_produto, preco_produto):
        self.nome = nome_produto
        self.preco = preco_produto

    def exibir(self):
        print(f"Nome do produto: {self.nome}\nPreço do produto: {self.preco}")
    
produto1 = Produto("Ovo de galinha", 12)
produto1.exibir()

produto1.preco = 20
produto1.exibir()