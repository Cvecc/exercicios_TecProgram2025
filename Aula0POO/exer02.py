#Crie um sistema para controlar o estoque de produtos. O programa deve pedir a quantidade inicial de um produto, a quantidade vendida e a quantidade recebida. Calcule a quantidade final em estoque.

quantidade_inicial= float(input("Digite a quantidade inicial"))
quantidade_recebida= float(input("Digite o valor da quantidade recebida"))
quantidade_vendida= float(input("Digite a quantidade vendida"))
quantidade_final= quantidade_recebida + quantidade_inicial - quantidade_vendida

print(" A quantidade inicial é", quantidade_inicial)
print(" A quantidade recebida é", quantidade_recebida)
print("A quantidade vendida foi de", quantidade_vendida)
print("A quantidade total/final é de", quantidade_final)