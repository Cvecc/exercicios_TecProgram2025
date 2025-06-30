#Uma loja oferece parcelamento de um produto, mas cobra 10% de juros ao parcelar. Peça ao usuário o preço do produto e o número de parcelas e calcule o valor total e o valor de cada parcela.

preco_produto=float(input("Digite o valor do produto"))
numero_parecelas= float(input("Digite a quantidade de parcelas"))
valortotal= preco_produto * 1.1
valorparecela= valortotal / numero_parecelas
print("O valor de cada parecela é igual a",valorparecela,"e o valor total da compra é igual a",valortotal)