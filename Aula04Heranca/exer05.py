#Crie Pessoa com nome e idade. Crie Aluno que herda de Pessoa, adicionando matricula.
class Pessoa:
    def __init__(self,nome,idade):
        self.nome= nome
        self.idade= idade

class Aluno(Pessoa):
    def __init__(self, nome, idade,matricula):
        super().__init__(nome, idade)
        self.matricula= matricula

    def detalhes(self):
        print(f"\nAluno(a) {self.nome} \nIdade:{self.idade} anos.\nMatricula: {self.matricula}")

aluno1=Aluno("Patrick", 14, 12345)
aluno2=Aluno("Gabriela", 17, 54321)

aluno1.detalhes()
aluno2.detalhes()