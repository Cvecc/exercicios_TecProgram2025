#Crie uma classe Pessoa com um atributo de classe total_pessoas. Cada vez que uma nova instância for criada, o total_pessoas deve ser incrementado. Teste a alteração com várias instâncias.
class Pessoa:
    total_pessoas = 0
    def __init__(self, nome):
        self.nome = nome
        Pessoa.total_pessoas += 1
    
    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Pessoas no total: {Pessoa.total_pessoas}")

pessoa1 = Pessoa("Otávio")
pessoa1.exibir()

pessoa2 = Pessoa("Yara")
pessoa2.exibir()

pessoa3 = Pessoa("Tadeu")
pessoa3.exibir()

pessoa4 = Pessoa("Heitor")    
pessoa4.exibir()

pessoa5 = Pessoa("Gabriela")
pessoa5.exibir()