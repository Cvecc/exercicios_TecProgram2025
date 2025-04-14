#Crie uma classe ContaBancaria com um atributo de classe taxa_juros e um método estático calcular_juros(saldo) que calcula os juros sobre o saldo da conta.
class ContaBancaria:
    juros = 0.3

    
    @staticmethod
    def calcular_juros(saldo):
        return saldo*ContaBancaria.juros
    
valor1 = ContaBancaria.calcular_juros(54000)
valor2 = ContaBancaria.calcular_juros(7680)

print("\nSaldo: R$54000.00")
print(f"Valor dos juros sobre o saldo: R${valor1: .2f}")

print("\nSaldo: R$7680.00")
print(f"Valor dos juros sobre o saldo: R${valor2: .2f}\n")