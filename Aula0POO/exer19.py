#Crie um programa que solicita 3 notas do usuário, armazena em uma lista e calcula a média.

nota1= float(input("Digite a primeira nota:"))

nota2= float(input("Digite a segunda nota:"))

nota3= float(input("Digite a terceira nota:"))

notas= [nota1,nota2,nota3]

media= sum(notas) / 3

print("Sua média é igual a:", media)