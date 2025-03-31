#Crie uma classe Carro com os atributos modelo e cor. Defina valores padrão para esses atributos caso não sejam passados durante a criação da instância.
class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
    
    