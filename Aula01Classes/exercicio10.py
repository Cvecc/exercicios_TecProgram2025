#Crie uma classe Pessoa com o método de classe criar_pessoa(nome, idade) que cria e retorna uma instância de Pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    @classmethod
    def criar_pessoa(cls):
        return cls("Larissa Arruda", 21)
    
pessoa1 = Pessoa.criar_pessoa()
print(pessoa1.nome)
print(pessoa1.idade)