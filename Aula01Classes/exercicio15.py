#Crie uma classe ContaBancaria com o atributo privado __saldo e um método depositar(valor) que aumenta o saldo.

class ContaBancaria:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.__saldo = saldo
 
    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito no valor de R${valor: .2f} realizado.")
    
    def exibir(self):
        print(f"O valor do saldo do titular {self.nome} é: R${self.__saldo: .2f}\n")

conta1 = ContaBancaria("Jerônimo", 6759)
conta2 = ContaBancaria("Claudete", 2296)

conta1.exibir()
conta1.depositar(2350)
conta1.exibir()

conta2.exibir()
conta2.depositar(1900)
conta2.exibir()