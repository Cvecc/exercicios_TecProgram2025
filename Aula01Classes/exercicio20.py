#Crie uma classe Livro com um método de classe criar_livro(titulo, autor) que cria e retorna uma instância de Livro com base nos parâmetros passados.

class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def exibir(self):
        print(f"\nTítulo do livro: {self.titulo}\nAutor do livro: {self.autor}\n--------------------------------------")
    @classmethod
    def criar_livro(cls, titulo, autor):
        return cls(titulo, autor)

livro1 = Livro.criar_livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling")
livro2 = Livro("O Jardim Secreto","Frances Hodgson Burnett")

livro1.exibir()
livro2.exibir()