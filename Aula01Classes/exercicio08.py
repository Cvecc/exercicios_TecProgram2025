#Crie uma classe Funcionario com o atributo de classe bonus. Adicione um método de classe modificar_bonus(valor) que altera o valor do bônus.

class Funcionario:
    bonus = 500
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def salario_final(self):
        return self.salario + Funcionario.bonus
    
    def exibir(self):
        print(f"Funcionário: {self.nome}")
        print(f"Salário: R${self.salario: .2f}")
        print(f"Salário com bônus: R${self.salario_final(): .2f}\n")

    @classmethod
    def modificar_bonus(cls, valor):
        cls.bonus = valor
    @classmethod
    def exibir_novo(cls):
        print(f"\nNovo bônus: R${Funcionario.bonus: .2f}\n")
        


funcionario1 = Funcionario("Kuzco", 2000)
funcionario2 = Funcionario("Larissa", 4000)
funcionario1.exibir()
funcionario2.exibir()

Funcionario.modificar_bonus(800)
Funcionario.exibir_novo()
funcionario1.exibir()
funcionario2.exibir()