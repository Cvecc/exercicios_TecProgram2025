#Desafio: Peça ao usuário para digitar um número e informe se ele é primo.

num = int(input("\nDigite um número para descobir se é primo: "))
primo = num > 1 and all(num % i for i in range(2, num))
if primo:
  print(f"\nÉ n° primo.")
else:
  print("\nNão é n° primo")
