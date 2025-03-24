#Crie uma classe Pessoa com um método estático validar_idade(idade) que retorna True se a idade for maior ou igual a 18 e False caso contrário.

class Pessoa:
    @staticmethod
    def validar_idade(idade):
        if idade >= 18:
            return print(f"Idade:",idade, "\nTrue\n")
        
        else:
            print(f"Idade:",idade, "\nFalse\n")

idade1 = Pessoa.validar_idade(20)
idade2 = Pessoa.validar_idade(15)
idade3 = Pessoa.validar_idade(45)
idade4 = Pessoa.validar_idade(10)