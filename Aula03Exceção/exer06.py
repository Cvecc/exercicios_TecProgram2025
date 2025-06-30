#Crie uma função para abrir e ler um arquivo de texto. Garanta que o arquivo seja fechado usando finally.
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)

except FileNotFoundError:
    print("O arquivo não foi encontrado")

finally:
    print("Operação finalizada.")