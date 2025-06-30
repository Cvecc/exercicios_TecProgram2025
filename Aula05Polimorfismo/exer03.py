#Modele um sistema de envio de mensagens com as classes Email, SMS e Whatsapp. Todas devem ter o método enviar_mensagem().
class Envio:
    def __init__(self,destinatario,conteudo):
        self.destinatario = destinatario
        self.conteudo = conteudo 
    def enviar_mensagem(self):
        raise NotImplementedError("Método não implementado pelas subclasses.")
    
class Email(Envio):
    def enviar_mensagem(self):
        print(f"\nEnviando Email para {self.destinatario}: {self.conteudo}")

class SMS(Envio):
    def enviar_mensagem(self):
        print(f"\nSMS enviado para {self.destinatario}: {self.conteudo}")

class Whatsapp(Envio):
    def enviar_mensagem(self):
        print(f"\nWhatsapp enviado para {self.destinatario}: {self.conteudo}")

mensagens = [
    Email("pedro@email.com", "Olá, Pedro. Anexo enviado."),
    SMS("+5519674413532", "Código: 123F5G"),
    Whatsapp("+5510934456789", "Para quando é o trabalho?")
]

for mensagem in mensagens:
    mensagem.enviar_mensagem()  
    