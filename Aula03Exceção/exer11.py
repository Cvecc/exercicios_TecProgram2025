#Crie uma classe base Veiculo e uma classe derivada Carro. No construtor de Carro, valide que a quantidade de portas seja maior que zero.
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        if portas <= 0:
            raise ValueError("A quantidade de portas deve ser maior que zero.")
        self.portas = portas

    def exibir_info(self):
        super().exibir_info()
        print(f"Portas: {self.portas}")

try:
    carro = Carro("Toyota", "SUV", 4)
    carro.exibir_info()
except ValueError as erro:
    print(f"Erro ao criar carro: {erro}")
