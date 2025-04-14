#Crie uma classe Cliente com o atributo nome e um método estático validar_cpf(cpf) que retorna True se o CPF for válido. Use esse método no método de instância cadastrar_cliente().
class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def cadastrar_cliente(self, cpf):
        if Cliente.validar_cpf(cpf):
            self.cpf = cpf
            print(f"\nCPF do cliente {self.nome} é válido. Cadastro realizado com sucesso.")
        
        else:
            print(f"\nO CPF {cpf} é inválido. Cadastro do cliente {self.nome} não realizado.")

    @staticmethod
    def validar_cpf(cpf):
        if len(cpf) != 11:
            return False
        
        if cpf == cpf[0]*11:
            return False

        return True
        
cadastro1 = Cliente("Júlio")
cadastro2 = Cliente("Esther")
cadastro3 = Cliente("Godfrey")
cadastro1.cadastrar_cliente("71936847202")
cadastro2.cadastrar_cliente("8729537105")
cadastro3.cadastrar_cliente("47691083203")
Cliente.validar_cpf("71936847202")
Cliente.validar_cpf("8729537105")
Cliente.validar_cpf("47691083203")