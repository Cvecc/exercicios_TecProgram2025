#Crie Funcionario com nome, salario. Crie Programador que usa super() e adiciona linguagem.
class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

class Programador(Funcionario):
    def __init__(self, nome, salario,linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem 

    def mostrar(self):
        print(f"\nFuncionário: {self.nome}\nSalário: R${self.salario}\nLinguagem: {self.linguagem}")

funcionario1= Programador("Aryanne","5500","Python")
funcionario1.mostrar()