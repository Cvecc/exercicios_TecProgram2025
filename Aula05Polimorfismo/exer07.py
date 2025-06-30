#Crie uma classe Arquivo com um método abrir(). Crie subclasses ArquivoTexto, ArquivoImagem e ArquivoVideo.
class Arquivo:
    def __init__(self, nome):
        self.nome = nome

    def abrir(self):
        raise NotImplementedError("Método não implementado pelas subclasses.")

class ArquivoTexto(Arquivo):
    def __init__(self, nome):
        super().__init__(nome)

    def abrir(self):
        print(f"\nAbrindo o arquivo de texto: {self.nome}")

class ArquivoImagem(Arquivo):
    def __init__(self, nome):
        super().__init__(nome)

    def abrir(self):
        print(f"\nExibindo a imagem: {self.nome}")

class ArquivoVideo(Arquivo):
    def __init__(self, nome):
        super().__init__(nome)

    def abrir(self):
        print(f"\nReproduzindo o vídeo: {self.nome}")

arquivos = [
    ArquivoTexto("arqiuvo.txt"),
    ArquivoImagem("foto.jpg"),
    ArquivoVideo("filme.mp4")
]

for arquivo in arquivos:
    arquivo.abrir()