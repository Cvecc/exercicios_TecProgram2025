#Crie uma classe Carro com os atributos modelo e cor. Defina valores padrão para esses atributos caso não sejam passados durante a criação da instância.
class Carro:
    def __init__(self, modelo = "Sedan", cor="Prata"):
        self.modelo = modelo
        self.cor = cor
    
    def exibir(self):
        print(f"\nModelo do Carro: {self.modelo}\nCor do Carro: {self.cor}")
    
carro1 = Carro("SUV", "Preto")
carro2 = Carro()
carro3 = Carro()

carro3.exibir()
carro1.exibir()
carro2.exibir()