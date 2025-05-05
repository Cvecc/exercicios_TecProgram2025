#Crie uma classe Produto com os atributos id_produto, nome e preco.
#Utilize um dicionário para armazenar os produtos.
#Permita adicionar e buscar produtos pelo ID.

class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
    
    def exibir(self):
        print(f"ID: {self.id_produto}\nNome do produto: {self.nome}\nPreço: R${self.preco: .2f}\n")

produtos = {}

def adicionar_produto():
    try:
        id_produto = int(input("Digite o ID do produto: "))
        if id_produto in produtos:
            print("ID já existe. Escolha outro.")
            return
        
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        produtos[id_produto] = Produto(id_produto, nome, preco)
        print("Produto adicionado com sucesso!")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números para ID e preço.")

def buscar_produto():
    try:
        id_produto = int(input("Digite o ID do produto para buscar: "))

        if id_produto in produtos:
            produtos[id_produto].exibir()
        else:
            print("Produto não encontrado.")
            
    except ValueError:
        print("ID inválido.")

while True:
    print("\n[1] Adicionar Produto\n[2] Buscar Produto por ID\n[3] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        buscar_produto()
    elif opcao == "3":
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")