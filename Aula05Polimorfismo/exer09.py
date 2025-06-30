#Modele um sistema de notificações com as classes NotificacaoEmail, NotificacaoSMS e NotificacaoPush.
class Notificacao:
    def __init__(self, destinatario, mensagem):
        self.destinatario = destinatario
        self.mensagem = mensagem

    def enviar(self):
        raise NotImplementedError("Método não implementado nas subclasses.")

class NotificacaoEmail(Notificacao):
    def enviar(self):
        print(f"\nEnviando EMAIL para {self.destinatario}: {self.mensagem}")

class NotificacaoSMS(Notificacao):
    def enviar(self):
        print(f"\nEnviando SMS para {self.destinatario}: {self.mensagem}")

class NotificacaoPush(Notificacao):
    def enviar(self):
        print(f"\nEnviando PUSH para {self.destinatario}: {self.mensagem}")

notificacoes = [
    NotificacaoEmail("fulano@email.com", "Você tem um novo e-mail."),
    NotificacaoSMS("+5591987654321", "Código de verificação: 12G63H"),
    NotificacaoPush("Fulano", "Você recebeu uma nova mensagem.")
]

for notificacao in notificacoes:
    notificacao.enviar()