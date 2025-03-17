#Exercício 2: Atributos com Construtor

#Tarefa: Crie uma classe Carro com os atributos modelo e ano. Use o construtor __init__ para inicializar esses atributos e crie uma instância de Carro.
#Objetivo: Entender o uso de atributos dentro do construtor.

class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
    def exibir(self):
        print(f"\nModelo: {self.modelo}\nAno: {self.ano}")

carro1 = Carro("SUV", 2021)
carro2 = Carro("Sedan", 2018)

carro1.exibir()
carro2.exibir()