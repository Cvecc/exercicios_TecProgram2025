#Crie uma classe Venda com um método estático calcular_imposto(valor) que retorna o valor do imposto sobre o valor passado.
class Venda:
    @staticmethod
    def calcular_imposto(valor):
        return valor*0.10

venda1 = Venda.calcular_imposto(1000)
venda2 = Venda.calcular_imposto(15000)

print("\nO valor do imposto sobre o valor da venda (no valor de R$1000) é de: R$", venda1)
print("\nO valor do imposto sobre o valor da venda (no valor de R$15.000) é de: R$", venda2)
