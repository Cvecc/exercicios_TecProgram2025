#Crie uma função para calcular a média de uma lista de números. Use try-except para capturar erro de tipo, e no bloco else, imprima a média.

def calcular(lista):
    try:
        soma = sum(lista)
        quantidade = len (lista)

        media = soma/quantidade
    
    except TypeError:
        print("Erro: a lista deve conter apenas números.")
    
    else:
        print(f"A média das notas {lista} é: {media}.")

calcular([9, 10, 8])
calcular([2, 'a', 7])