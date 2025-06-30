#Crie Professor e Pesquisador. Crie Cientista que herda ambos e usa trabalhar() com os dois comportamentos.        
class Professor:
    def trabalhar(self):
        return "Dar aula"
        
class Pesquisador:
    def trabalhar(self):
        return "Pesquisar"
    
class Cientista(Professor, Pesquisador):
    def trabalhar(self):
        return f"\nCientista: {Professor.trabalhar(self)} e {Pesquisador.trabalhar(self)}"

cientista = Cientista()
professor = Professor()
print(f"\nProfessor: {professor.trabalhar()}")
print(cientista.trabalhar())