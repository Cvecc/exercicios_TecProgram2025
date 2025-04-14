#Crie uma classe Aluno com um atributo protegido _nota e um método protegido modificar_nota(nota) para alterar a nota.
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self._nota = nota
    
    def _modificar(self, nota):
        self._nota = nota

    def exibir(self):
        print(f"Nome do aluno: {self.nome}.")
        print(f"Nota: {self._nota}.\n")

aluno1 = Aluno("Ulisses", 9)
aluno2 = Aluno("Paulo", 4)
aluno3 = Aluno("Ary", 7)

aluno1.exibir()
aluno2.exibir()
aluno3.exibir()

aluno3._modificar(10)
aluno3.exibir()