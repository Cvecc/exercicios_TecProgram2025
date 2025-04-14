#Crie uma classe ContaBancaria com o atributo saldo e o método saque(valor). O saque só deve ser realizado se o valor for menor que o saldo.
class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def exibir(self):
        print(f"\nSaldo atual: R${self.saldo: .2f}")
    
    def saque(self,valor):
        if valor < self.saldo:
            self.saldo -= valor
            return print(f"Foi realizado o saque no valor de R${valor: .2f}\nSaldo: R${self.saldo: .2f}")
        
        else:
            return print(f"Não é possível realizar o saque no valor de R${valor: .2f}. O valor inserido é maior que o saldo atual.\nSaldo: {self.saldo: .2f}")

conta1 = ContaBancaria(8967)
conta2 = ContaBancaria(4589)
conta3 = ContaBancaria(9000)

conta1.exibir()
conta1.saque(2050)

conta2.exibir()
conta2.saque(650)

conta3.exibir()
conta3.saque(10000)