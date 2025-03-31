#Crie uma classe Pessoa com o atributo idade. Adicione um método de instância verificar_maioridade() que verifica se a pessoa é maior de idade.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def verificar_maioridade(self):
        if self.idade >= 18:
            print(f"{self.nome} possui {self.idade} anos, portanto, é MAIOR de idade.\n")
        
        else: 
            print(f"{self.nome} possui {self.idade} anos, portanto, é MENOR de idade.\n")

pessoa1 = Pessoa("Bárbara", 5)
pessoa2 = Pessoa("Paulo", 89)
pessoa3 = Pessoa ("Ulisses", 18)

pessoa1.verificar_maioridade()
pessoa2.verificar_maioridade()
pessoa3.verificar_maioridade()