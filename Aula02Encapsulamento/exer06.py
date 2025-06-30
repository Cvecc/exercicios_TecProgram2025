#Desenvolva uma classe Usuario que armazene a __senha de forma segura e tenha um método validar_senha(senha) que compara a senha.
class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.__senha = senha

    def validar_senha(self, senha):
        return senha == self.__senha

    def exibir(self):
        print(f"\nUsuário: {self.nome}")

usuario1 = Usuario("Joana", "minhasenha")
usuario2 = Usuario("Carlos", "1234")

usuario1.exibir()
print("Senha 'minhasenha' correta.", usuario1.validar_senha("minhasenha")) 
print("Senha 'errada' incorreta.", usuario1.validar_senha("errada"))      

usuario2.exibir()
print("Senha '1234' correta.", usuario2.validar_senha("1234"))