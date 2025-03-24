#Crie uma classe Pessoa com os atributos nome e idade. Adicione um método de instância apresentar() que retorna uma string com o nome e a idade da pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Nome da pessoa {self.nome}\nIdade da pessoa: {self.idade}\n")

pessoa1 = Pessoa("Alberto", 46)
pessoa2 = Pessoa("Cláudia", 20)

pessoa1.apresentar()
pessoa2.apresentar()