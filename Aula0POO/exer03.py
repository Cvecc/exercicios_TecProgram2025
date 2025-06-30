#Crie um programa que calcule a pontuação total de um jogador em um jogo.
#A pontuação será dada por:
#10 pontos por cada vitória.
#5 pontos por cada empate.
#0 pontos por cada derrota.
#O programa deve calcular o total de pontos de acordo com o número de vitórias, empates e derrotas informados.
vitorias=float(input("\nDigite a quantidade de vitorias"))
derrotas= float (input("Digite a quantidade de derrotas"))
empates= float (input("Digite a quantidade de empates"))

pontosvitorias= vitorias*10
pontosempates= empates *5
pontosderrotas =  derrotas*0
pontuçãototal= pontosvitorias + pontosderrotas + pontosempates

print("\nO total de pontos foram de", pontuçãototal, "pontos!")