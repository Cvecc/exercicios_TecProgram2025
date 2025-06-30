#Crie uma classe Produto que receba nome e preço. Se o preço for negativo, levante uma exceção no método __init__.
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        print(f"Produto: {self.nome}\nPreço: R${self.preco}")
    

try:
    nome = input("Insira o nome do produto: ")
    preco = float(input("Insira o preco do produto: R$"))
    produto = Produto(nome, preco)
    print(produto)

except ValueError as error:
    print(error)
