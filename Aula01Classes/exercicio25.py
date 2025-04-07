#Crie uma classe Produto com um atributo de classe desconto e um método estático aplicar_desconto(preco) que aplica o desconto no preço do produto.
class Produto:
    desconto = 0.1
    @staticmethod
    def aplicar_desconto(preco):
        novo_preco = preco - (preco*Produto.desconto)
        return novo_preco
    
produto1 = Produto.aplicar_desconto(70)
produto2 = Produto.aplicar_desconto(44.99)
produto3 = Produto.aplicar_desconto(60)

print(f"\nValor do produto: R$70,00\nValor com desconto de 10%: R${produto1: .2f}")
print(f"\nValor do produto: R$44,99\nValor com desconto de 10%: R${produto2: .2f}")
print(f"\nValor do produto: R$60,00\nValor com desconto de 10%: R${produto3: .2f}")