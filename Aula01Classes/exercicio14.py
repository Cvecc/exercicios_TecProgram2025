#Crie uma classe Banco com um atributo de classe taxa_juros. Adicione um método estático calcular_juros(saldo) que calcula os juros sobre um saldo, considerando a taxa de juros da classe.
 
class Banco:
    taxa_juros = 0.1
    @staticmethod
    def calcular_juros(saldo):
        return saldo*Banco.taxa_juros
 
juros1 = Banco.calcular_juros(1000)
juros2 = Banco.calcular_juros(5000)
juros3 = Banco.calcular_juros(400)
 
print(f"Os juros sobre o saldo é de: R${juros1}")
print(f"\nOs juros sobre o saldo é de: R${juros2}")
print(f"\nOs juros sobre o saldo é de: R${juros3}")