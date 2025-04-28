#Crie uma exceção personalizada chamada ErroSaldoInsuficiente para ser usada na classe ContaBancaria
class ErroSaldoInsuficiente(Exception):
    pass

class ValorNegativo(Exception):
    pass

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def saque(self, valor):
        if valor > self.saldo:
            raise ErroSaldoInsuficiente("Saldo Insuficiente")
        if valor < 0:
            raise ValorNegativo("Valor do saque não pode ser negativo.")
        self.saldo -= valor
        return self.saldo

try:

    conta1 = ContaBancaria(500)
    print(conta1.saque(50))

    conta2 = ContaBancaria (50)
    print(conta2.saque(500))#vai gerar o erro "Saldo insuficiente" e então interromperá o programa.

    conta3 = ContaBancaria(500)
    print(conta2.saque(-50))

except ErroSaldoInsuficiente as error:
    print(error)

except ValorNegativo as error:
    print(error)