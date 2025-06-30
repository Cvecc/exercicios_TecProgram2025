#Crie uma classe Pessoa com um atributo público idade e um método validar_idade(), que retorna True se a idade for maior ou igual a 18.
class Pessoa:
    def __init__(self, idade):
        self.idade = idade  

    def validar_idade(self):
        return self.idade >= 18 

p1 = Pessoa(20)
p2 = Pessoa(15)

print(f"Pessoa 1 é maior de idade: {p1.validar_idade()}")
print(f"Pessoa 2 é maior de idade: {p2.validar_idade()}")
