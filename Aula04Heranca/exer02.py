#Crie Funcionario com nome e salario. Crie Gerente, herdando de Funcionario e adicionando departamento.
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def detalhes(self):  
        print(f"\n{self.nome} ganha R${self.salario:.2f} | Departamento: {self.departamento}")

funcionario1 = Gerente("Renata", 5900.97, "TI")
funcionario2 = Gerente("Paula", 4200.50, "Contabilidade")

funcionario1.detalhes()
funcionario2.detalhes()