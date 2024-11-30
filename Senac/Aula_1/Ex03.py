# Exercício 3

# A padaria Sópão vende diariamente uma certa quantidade de pães franceses e uma quantidade
# de broas. Cada pãozinho custa R$ 0,80 e a broa custa R$ 2,50. Do total arrecadado,
# 43% corresponde aos custos de fabricação. Do restante, Seu joão guarda 15% numa conta
# de poupança e 15% ele converte em Euros para sua viagem Anual.
# Sabe-se que 1 Euro custa R$ 4,60. Com base nestes fatos, faça um progrma para ler
# as quantidades de pães e de broas, calcular a venda total de pãos e broas,
# o custo de fabricação, quanto irá guardar na poupança e quantos euros irá comprar.
# Ao final exibir os dados calculados.

paes = int(input("Quantos paes foram vendidos: "))
broas = int(input("Quantos broas foram vendidos: "))
print("-"*30)

valor_paes = paes * 0.80
valor_broas = broas * 2.50
valor_total = valor_paes + valor_broas

custo = valor_total * 0.43
restante = valor_total - custo
poupanca = restante * 0.15
viagem = (restante * 0.15) / 4.60

print(f'O valor total das vendas: R${valor_total:.2f}\n'
      f'O valor do custo de fabricação: R${custo:.2f}\n'
      f'O valor da poupança: R${poupanca:.2f}\n'
      f'O valor para a viagem já convertido para euro: R${viagem:.2f}')

print("-"*30)
