# Exercício 4: Tabuada
# Escreva um programa que exiba a tabuada de multiplicação
# de um número digitado pelo usuário, de 1 a 10.

num = int(input("Digite um numero: "))
contagem = 1

while contagem <= 10:
    print(f'{num} x {contagem} = {num * contagem}')
    contagem += 1

else:
    print("-------------------")