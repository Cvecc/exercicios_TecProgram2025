#Crie uma classe Aluno onde cada aluno pode ter múltiplas notas (armazenadas em uma lista).
#Implemente um método para calcular a média do aluno.
#Permita adicionar novas notas dinamicamente.

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        try:
            nota = float(nota)
            self.notas.append(nota)
            print(f"Nota {nota} adicionada para o aluno {self.nome}.")
        except ValueError:
            print("Nota inválida. Por favor, digite um número.")

    def calcular_media(self):
        if self.notas:
            media = sum(self.notas) / len(self.notas)
            return media
        else:
            return 0.0

    def exibir_informacoes(self):
        print(f"\nAluno: {self.nome}\nNotas: {self.notas}\nMédia: {self.calcular_media():.2f}")

alunos = {}

while True:
    print("\n[1] Cadastrar novo aluno.")
    print("[2] Adicionar nota a aluno existente.")
    print("[3] Ver informações de um aluno.")
    print("[4] Sair.")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        if nome in alunos:
            print("Aluno já cadastrado.")
        else:
            alunos[nome] = Aluno(nome)
            print("Aluno cadastrado com sucesso.")

    elif opcao == "2":
        nome = input("Digite o nome do aluno: ")
        if nome in alunos:
            nota = input("Digite a nota: ")
            alunos[nome].adiciona1r_nota(nota)
        else:
            print("Aluno não encontrado.")

    elif opcao == "3":
        nome = input("Digite o nome do aluno: ")
        if nome in alunos:
            alunos[nome].exibir_informacoes()
        else:
            print("Aluno não encontrado.")

    elif opcao == "4":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida.")
