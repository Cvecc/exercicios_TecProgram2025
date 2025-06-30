#Crie uma classe ContaBancaria que permita depósito e saque. Lance exceções para saques acima do saldo disponível.
class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor
        print(f"\nDepósito de R${valor} feito com sucesso.\nSaldo atual: R${self.saldo}.")
    
    def saque(self, valor):
        if valor > self.saldo:
            print(f"\nValor do saque: R${valor}\nSaldo: R${self.saldo}")
            raise ValueError("Saldo Insuficiente.")
        if valor < 0:
            raise ValueError("\nValor do saque não pode ser negativo.")
        self.saldo -= valor
        return print(f"\nSaque no valor de R${valor} feito com sucesso.\nSaldo atual: {self.saldo}")
        
try:
    conta1 = ContaBancaria(700)
    print(conta1.depositar(100))
    print(conta1.saque(750))

    conta2 = ContaBancaria(50)
    print(conta2.saque(200))

except ValueError as error:
    print(error)

try:
    conta3 = ContaBancaria(600)
    conta3.saque(-200)

except ValueError as error:
    print(error)