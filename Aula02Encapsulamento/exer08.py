#Crie uma classe Funcionario que encapsule o atributo privado __salario e tenha um método informar_salario() que retorna o valor.

class Funcionario:
    def __init__(self,nome,salario):
        self.nome= nome
        self.__salario= salario

    def informar_salario(self):
        return self.__salario
    
funcionario1= Funcionario("Bruna",2000)

print(funcionario1.nome)
print(funcionario1.informar_salario())