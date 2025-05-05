#Crie um dicionário onde o usuário possa cadastrar alunos e suas notas.

class Cadastro:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def exibir(self):
        print(f"Aluno: {self.nome}\nNotas: {self.notas}")
    
alunos = {}

while True:
    saida = input("Deseja cadastrar um aluno? [s/n]: ")
    if saida.lower() == 'n':
        break

    nome = input("Digite o nome do aluno: ")
    try:
        notas = float(input(f"Digite a nota do aluno {nome}: "))
        alunos[nome] = Cadastro(nome, notas)
    except ValueError:
        print("Nota Inválida. Digite um número.")
        continue

print("\nAlunos Cadastrados:\n")
for aluno in alunos.values():
    aluno.exibir()