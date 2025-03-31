#Crie uma classe Aluno com os atributos nome e nota. Crie várias instâncias e modifique os atributos de cada uma de forma independente.
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    def exibir(self):
        print(f"Nome do aluno: {self.nome}.")
        print(f"Nota: {self.nota}.\n")
    