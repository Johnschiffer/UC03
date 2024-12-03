# Exercício 5: Contar Números Pares
# Escreva um programa que receba 10 números inteiros e
# conte quantos deles são pares.

pares = []
for i in range(10):
    num = int(input("Digite um numero: "))

    if (num % 2 == 0):
        pares.append(num)

print(f'Os numeros pares são: {pares}')