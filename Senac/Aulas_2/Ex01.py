# Exercício 1: Par ou Ímpar
# Escreva um programa que receba um número inteiro e verifique se ele é par ou ímpar, exibindo o resultado.

num1 = int(input("Digite um numero: "))

if (num1 %2 == 0):
    print(f'O {num1} é par')

else:
    print(f'O {num1} é ímpar')
