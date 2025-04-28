#Crie uma classe Aluno com atributos nome e nota. Implemente um método para validar que nota seja um número entre 0 e 10.
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def validar(self):
        if self.nota <0 or self.nota>10:
            raise ValueError("A nota deve ser de 0 - 10")
        print(f"Nota cadastrada com sucesso: {self.nota}")

try:
    aluno1 = Aluno("Clara", 10)
    aluno1.validar()

    aluno2 = Aluno("Bárbara", 100)
    aluno2.validar()

except ValueError as error:
    print(error)
