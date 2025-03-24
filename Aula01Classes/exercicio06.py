#Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método de instância depositar(valor) que aumenta o saldo da conta.

class ContaBancaria:
    def __init__(self, titular, saldo_antes=0):
        self.titular = titular
        self.saldo = saldo_antes
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor: .2f} realizado com sucesso.")
        else: 
            print("O valor inserido deve ser positivo.")
    
    def exibir(self):
        print(f"Saldo da conta de {self.titular} é: R${self.saldo: .2f}\n")

conta1 = ContaBancaria("Igor", 5983)
conta2 = ContaBancaria("Eliza", 700)
conta1.exibir()
conta1.depositar(845)
conta1.exibir()

conta2.exibir()
conta2.depositar(0)
conta2.exibir()