#Crie uma classe Aluno com os atributos nome e nota. Adicione um método de classe alterar_nome() que altera o nome de todos os alunos de uma lista.
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    @classmethod
    def alterar_nome(cls, lista, novo_nome):
        for aluno in lista:
            aluno.nome = novo_nome


aluno1 = Aluno("Luiz", 7)
aluno2 = Aluno("Bárabar", 10)
aluno3 = Aluno("José", 6.75)
aluno4 = Aluno("Paula", 4.5)

lista = [aluno1, aluno2, aluno3, aluno4]

print("\nAntes")
for aluno in lista:

    print("Nota:", aluno.nome)
    print("Nota:", aluno.nota, "\n")

Aluno.alterar_nome(lista, "Luisa")

print("\nDepois")
for aluno in lista:
    
    print("Nome:", aluno.nome)
    print("Nota:", aluno.nota, "\n")