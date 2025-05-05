#Crie um dicionário para armazenar números de telefone e permita que o usuário consulte um contato.

class Telefone:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    
    def exibir(self):
        print(f"Nome: {self.nome}\nTelefone: {self.telefone}")
    
contatos = {
    "Júlia": Telefone("Júlia", "(19)98765-4321"),
    "Claudio": Telefone("Claudio", "(10)12345-6789")
}

busca = input("Digite o nome do contato: ")

if busca in contatos:
    contatos[busca].exibir()

else:
    print("O contato não existe.")