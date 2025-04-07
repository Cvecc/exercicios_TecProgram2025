#Crie uma classe Curso com o atributo de instância nome e o atributo de classe quantidade_cursos. Adicione um método de classe alterar_quantidade_cursos() que modifica o valor de quantidade_cursos.
class Curso:
    quantidade_cursos = 0
    def __init__(self, nome):
        self.nome = nome
    
    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Quantidade de cursos: {Curso.quantidade_cursos}\n")

    @classmethod
    def alterar_quantidade(cls, nova):
        cls.quantidade_cursos = nova

curso1 = Curso("Ana")
curso2 = Curso("Bete")
curso1.exibir()
curso2.exibir()

Curso.alterar_quantidade(3)
curso1.exibir()

Curso.alterar_quantidade(7)
curso2.exibir()