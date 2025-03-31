#Crie uma classe Conta com o atributo saldo e o método verificar_saldo(), que retorna uma mensagem diferente dependendo do valor do saldo.
class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def verificar_saldo(self):
        if self.saldo > 0:
            print(f"O saldo do titular {self.titular}, no valor de R${self.saldo}, está positivo.\n")
        
        else:
            print(f"O saldo do titular {self.titular}, no valor de R${self.saldo}, está negativo.\n")

conta1 = Conta("Amy", 890)
conta2 = Conta("Huan", -70)

conta1.verificar_saldo()
conta2.verificar_saldo()