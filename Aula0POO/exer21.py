#Crie um programa onde o usuário pode adicionar itens a uma lista de compras e exibir os itens ao final.

listadecompras=[]
while True:
  compra= input("Adicione a sua lista de compra aqui:")

  if compra.lower()== 'sair':
      break

  listadecompras.append(compra)

print("Sua lista de compras:")
for compra in listadecompras:
  print(compra)