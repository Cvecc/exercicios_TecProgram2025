#Modele um sistema de transporte com as classes Onibus, Bicicleta e Carro, cada uma com o método custo_viagem(distancia).
class Transporte:
    def __init__(self, nome):
        self.nome = nome

    def custo_viagem(self, distancia):
        raise NotImplementedError("Método não implementado nas subclasses.")

class Onibus(Transporte):
    def __init__(self):
        super().__init__("Ônibus")

    def custo_viagem(self, distancia):
        return distancia * 0.60

class Bicicleta(Transporte):
    def __init__(self):
        super().__init__("Bicicleta")

    def custo_viagem(self, distancia):
        return 0 

class Carro(Transporte):
    def __init__(self, preco_combustivel_por_km):
        super().__init__("Carro")
        self.preco_combustivel_por_km = preco_combustivel_por_km

    def custo_viagem(self, distancia):
        return distancia * self.preco_combustivel_por_km

distancia = 380
transportes = [
    Onibus(),
    Bicicleta(),
    Carro(preco_combustivel_por_km=0.70)
]

for meio in transportes:
    custo = meio.custo_viagem(distancia)
    print(f"\n{meio.nome} || Custo para {distancia} km: R${custo:.2f}")