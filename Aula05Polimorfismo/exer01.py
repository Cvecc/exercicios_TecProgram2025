#Crie duas classes, Carro e Moto, que tenham um método acelerar(). Cada classe deve exibir uma mensagem diferente.
class Carro:
    def acelerar(self):
        print("\nCarro acelerando.")
class Moto:
    def acelerar(self):
        print("\nMoto acelerando.")

veiculos=[Carro(), Moto()]

for veiculo in veiculos:
    veiculo.acelerar()