#Implemente uma classe Carro com um atributo protegido _modelo e um método atualizar_modelo(modelo) para alterar seu valor.
class Carro:
    def __init__(self, modelo):
        self._modelo = modelo

    def atualizar_modelo(self, modelo):
        self._modelo = modelo

carro1 = Carro("Jipe")
carro2 = Carro("Sedan")

print("\nModelo do carro: " + carro1._modelo)
print("\nModelo do carro: " + carro2._modelo)

carro2.atualizar_modelo("SUV")
print("\nNovo modelo: " + carro2._modelo)