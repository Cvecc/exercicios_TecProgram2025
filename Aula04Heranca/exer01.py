#Crie a classe Animal com o método falar(). Crie Cachorro e Gato, sobrescrevendo falar() com seus respectivos sons.
class Animal:
    def falar(self):
        return "Som Qualquer"
    
class Cachorro(Animal):
    def falar(self):
        return "Au Au"
    
class Gato(Animal):
    def falar(self):
        return "Miau Miau"

print(Cachorro().falar())
print(Gato().falar())