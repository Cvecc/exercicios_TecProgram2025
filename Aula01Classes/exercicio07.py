#Crie uma classe Aluno com os atributos nome e nota. Adicione um método de instância situacao() que retorna "Aprovado" se a nota for maior ou igual a 6 e "Reprovado" caso contrário.

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def situacao(self):
        if self.nota >= 6:
            return print(f"Aluno: {self.nome}\nNota: {self.nota}\nSituação: Aprovado.\n")
        
        else:
            return print(f"Aluno: {self.nome}\nNota: {self.nota}\nSituação: Reprovado.\n")

aluno1 = Aluno("Paulo", 8)
aluno2 = Aluno("Yasmin", 5)

aluno1.situacao()
aluno2.situacao()