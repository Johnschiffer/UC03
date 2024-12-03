# Exercício 9: Contagem de Parcelas
# Crie um programa que calcule o valor total de uma compra feita em várias parcelas.
# Pergunte ao usuário quantas parcelas ele deseja e o valor de cada uma.
# Se o total ultrapassar R$ 1.000,00, acrescente 5% de juros.
compra = float(input("Digite o valor da compra: "))
parcelas = int(input("Quantas parcelas deseja?: "))

if compra > 1000:
    compra += compra * 0.05
    # compra = juros

print(f'O valor da compra é de R$ {compra}\n'
      f'Quantida de parcelas {parcelas}\n'
      f'Valor das parcelas R$ {(compra / parcelas)}')