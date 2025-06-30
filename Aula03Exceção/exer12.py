#Crie uma classe Pessoa que recebe o nome e a idade como parâmetros. No método verificar_maioridade, use try-except para garantir que a idade seja um número inteiro.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def verificar_maioridade(self):
        try:
            idade_int = int(self.idade)
            if idade_int >= 18:
                print(f"{self.nome} é maior de idade.")
            else:
                print(f"{self.nome} é menor de idade.")
        except ValueError:
            print(f"Erro: a idade de {self.nome} deve ser um número inteiro.")


p1 = Pessoa("Bárbara", 20)
p1.verificar_maioridade()

p2 = Pessoa("Alberto", "dez")
p2.verificar_maioridade()
