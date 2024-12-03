# # Exercício 3: Maior de Três Números
# # Escreva um programa que receba três números inteiros e determine
# # qual deles é o maior.


nuns = []

for i in range(3):
    nuns.append(int(input("Digite um numero: ")))
    nuns.sort()

print(f'O maior numero é {nuns[len(nuns)-1]}')