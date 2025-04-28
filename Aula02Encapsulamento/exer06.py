#Desenvolva uma classe Usuario que armazene a __senha de forma segura e tenha um método validar_senha(senha) que compara a senha.
class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.__senha = senha