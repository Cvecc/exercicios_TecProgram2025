#Peça para o usuário digitar um número e exiba a tabuada dele de 1 a 10.

tabuada= int(input("Digite o numero da tabuada que deseja descobrir"))
for i in range(1,11):
  resultado= tabuada * i
  print("O valor da tabuda (1 ao 10) do:",tabuada,"é", resultado)