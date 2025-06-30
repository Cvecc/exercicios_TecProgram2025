#Crie uma classe Biblioteca que contém uma classe aninhada Livro, com um atributo protegido _titulo.
class Biblioteca:
    class Livro:
        def __init__(self, titulo, autor, isbn):
            self._titulo = titulo         
            self.autor = autor
            self.__isbn = isbn           

        def get_isbn(self):
            return self.__isbn

        def get_titulo(self):
            return self._titulo        

livro1 = Biblioteca.Livro("O Jardim Secreto", "Frances Hodgson Burnett", 123456789)


print(livro1.get_titulo(), livro1.autor, livro1.get_isbn())