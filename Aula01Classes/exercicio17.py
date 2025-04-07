#Crie uma classe Aluno com os atributos nome e nota. Crie várias instâncias e modifique os atributos de cada uma de forma independente.
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    def exibir(self):
        print(f"Nome do aluno: {self.nome}.")
        print(f"Nota: {self.nota}.\n")
    
aluno1 = Aluno("Bárbara", 8.5)
aluno2 = Aluno("Alberto", 5)
aluno3 = Aluno("Luiz", 7)
aluno4 = Aluno("Rosa", 10)    

aluno1.exibir()
aluno2.exibir()
aluno3.exibir()
aluno4.exibir()

aluno1.nota = 10
aluno2.nota = 5.5
aluno3.nome = "João"
aluno3.nota = 3
aluno4.nome = "Carlota"
aluno4.nota = 9

aluno1.exibir()
aluno2.exibir()
aluno3.exibir()
aluno4.exibir()