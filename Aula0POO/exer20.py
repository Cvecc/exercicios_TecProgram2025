#Crie um programa que armazena números de 1 a 10 em uma lista e exibe apenas os pares.

numeros= range(1,11)
par=[]
for num in numeros:
 if num % 2 ==0:
    par.append(num)
print(par)