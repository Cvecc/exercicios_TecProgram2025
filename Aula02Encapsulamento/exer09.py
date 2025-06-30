#Implemente uma classe Livro com atributos públicos titulo e autor, e um atributo privado __isbn com um método get_isbn() para acesso.
class Livro:
    def __init__(self,titulo,autor,isbn):
        self.titulo = titulo
        self.autor = autor
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn
    
livro1= Livro("O Jardim Secreto", "Frances Hodgson Burnett", 123456789)
print(livro1.titulo, livro1.autor, livro1.get_isbn())