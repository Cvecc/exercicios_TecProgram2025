#Peça ao usuário para digitar uma palavra e conte quantas vogais existem nela.

palavra= input("Digite uma palavra para saber quanras vogais há")
vogais = 'aeiouAEIOU'
contagem_vogais = sum(1 for letra in palavra if letra in vogais)
print("A palavra",palavra,"tem" ,contagem_vogais,"vogais.")