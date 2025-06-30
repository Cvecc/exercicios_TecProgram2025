#Crie uma classe Loja que mantém um atributo protegido _estoque e um método adicionar_produto(produto) para modificar o estoque.
class Loja:
    def __init__(self):
        self._estoque = []

    def adicionar_produto(self,produto):
        self._estoque.append(produto)
        
    def mostrar_estoque(self):
        return self._estoque
    
loja1 = Loja()

loja1.adicionar_produto("Escova")
loja1.adicionar_produto("Shampoo")

print(loja1.mostrar_estoque())