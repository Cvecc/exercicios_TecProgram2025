#Crie uma superclasse Pagamento e as subclasses PagamentoCartao, PagamentoPix e PagamentoBoleto. Utilize uma lista para simular o processamento de diferentes pagamentos.
class Pagamento:
    def processar_pagamento(self, valor):
        raise NotImplementedError("Método não implementado na subclasse.")

class PagamentoCartao(Pagamento):
    def processar_pagamento(self, valor):
        print(f"\nProcessando pagamento no cartão no valor de R$ {valor:.2f}")
        print("Pagamento autorizado.")

class PagamentoPix(Pagamento):
    def processar_pagamento(self, valor):
        print(f"\nProcessando pagamento via PIX no valor de R$ {valor:.2f}")
        print("Pagamento realizado com sucesso.")

class PagamentoBoleto(Pagamento):
    def processar_pagamento(self, valor):
        print(f"\nGerando boleto no valor de R$ {valor:.2f}")
        print("Boleto gerado. Aguarde compensação.")

pagamentos = [
    PagamentoCartao(),
    PagamentoPix(),
    PagamentoBoleto()
]

for pagamento in pagamentos:
    pagamento.processar_pagamento(500.00)
    print("-" * 50)