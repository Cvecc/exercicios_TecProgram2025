#Crie Veiculo com marca e ano. Crie Carro e Moto, adicionando atributos e métodos específicos.
class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

    def trancar(self):
        return "Carro Trancado."

class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

    def buzinar(self):
        return "Moto buzinando."
    
carro1 = Carro("Chevrolet", 2023, 4)
moto1 = Moto("Honda", 2024, 250)

print(f"Carro: {carro1.marca}, Ano: {carro1.ano}, Portas: {carro1.portas}")
print(carro1.trancar())

print(f"Moto: {moto1.marca}, Ano: {moto1.ano}, Cilindradas: {moto1.cilindradas}")
print(moto1.buzinar())