#Desenvolva uma classe ContaBancaria com um atributo privado __senha e métodos acessores para acessar o saldo e realizar operações.
class ContaBancaria:
    def __init__(self, senha, saldo):
        self.__senha = senha
        self.saldo = saldo
    
    def verificar(self, senha):
        return self.__senha == senha

    def exibir_saldo(self, senha):
        if self.verificar(senha):
            return print(f"\nSaldo: R${self.saldo: .2f}")
        
        else:
            return print("\nSenha incorreta.")
        
conta1 = ContaBancaria(8888, 5800)
conta2 = ContaBancaria(444, 6900)

conta1.exibir_saldo(8888)
conta2.exibir_saldo(44)
conta2.exibir_saldo(444)