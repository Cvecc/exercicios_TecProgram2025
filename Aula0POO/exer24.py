#Crie um dicionário que funcione como um mini tradutor.
class Tradutor:
    def __init__(self):
        self.traduz = {
            "olá" : "hello",
            "gato" : "cat",
            "cachorro" : "dog",
            "cavalo" : "horse",
            "rato" : "rat",
            "avelã" : "hazel"
        }

    def traduzir(self, palavra):
        traducao = self.traduz.get(palavra.lower())
        if traducao:
            print(f"\n'{palavra}' em inglês é: '{traducao}'.")
        else:
            print(f"A palavra '{palavra}' não está no tradutor.")
    
    def adicionar(self, palavra, traducao):
        self.traduz[palavra.lower()] = traducao.lower()
        print(f"Adicionado: '{palavra}' -> '{traducao}.")

tradutor = Tradutor()

while True:
    opcao = input("\n[1] Traduzir palavra\n[2] Adicionar nova palavra\n[3] Sair\nEscolha uma opção: ")
    
    if opcao == "1":
        palavra = input("Digite a palavra em português: ")
        tradutor.traduzir(palavra)
    elif opcao == "2":
        palavra = input("Digite a nova palavra em português: ")
        traducao = input("Digite a tradução em inglês: ")
        tradutor.adicionar(palavra, traducao)
    elif opcao == "3":
        break
    else:
        print("Opção inválida.")