#Crie uma classe Loja com métodos adicionar_produto, remover_produto e listar_produtos. Lance exceções ao tentar remover um produto que não existe.
class ProdutoNaoEncontrado(Exception):
    pass

class Loja:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def remover_produto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
        else:
            raise ProdutoNaoEncontrado(f"O produto: '{produto}' não foi encontrado.")
    
    def listar_produtos(self):
        return self.produtos

loja = Loja()
loja.adicionar_produto("Peruca")
loja.adicionar_produto("Blusa")
print(loja.listar_produtos())

try:
    loja.remover_produto("Creme")
except ProdutoNaoEncontrado as e:
    print(e)

loja.remover_produto("Peruca")
print(loja.listar_produtos())