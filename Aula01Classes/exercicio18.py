#Crie uma classe Funcionario com um método salario() e uma classe Gerente que herda de Funcionario e sobrescreve o método salario() para retornar um valor maior.

class Funcionario:
    def __init__(self, nome, salario_):
        self.nome = nome
        self.salario_ = salario_
    
    def salario(self):
        return self.salario_
    
    def exibir(self):
        self.salario()
        print(f"Nome do Funcionário: {self.nome}")
        print(f"Salário: R${self.salario()}\n")

class Gerente(Funcionario):
    def __init__(self, nome, salario_, valor):
        self.nome = nome
        self.salario_ = salario_
        self.valor = valor

    def salario(self):
        return self.salario_ + self.valor
    
    def exibir(self):
        self.salario()
        print(f"Nome do Gerente: {self.nome}")
        print(f"Salário: R${self.salario()}\n")


funcionario1 = Funcionario("Tainá", 2700)
funcionario2 = Funcionario("Igor", 2800)
gerente1 = Gerente("Maria", 2800, 2000)

funcionario1.exibir()
funcionario2.exibir()
gerente1.exibir()