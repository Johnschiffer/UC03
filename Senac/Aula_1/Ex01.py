# # Exercício 1

# # Faça um programa para calcular a quantidade de latas de tintas para pintar uma parede. 
# O programa deverá solicitar ao usuário, a altura (float) e o comprimento(float) da parede.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
# vendida em latas de 3,6 litros, que custam R$ 107,00. Informe ao usuário a quantidades de latas
# de tinta a serem compradas e o preço total.
import math

altura1 = float(input("Digite a altura da parede: "))
comprimento1 = float(input("Digite o comprimento da parede: "))

area1 = altura1 * comprimento1
litros1 = area1 / 3
latas1 = litros1 / 3.6
preco1 = math.ceil(latas1) * 107



print(f"Quantidade de latas: {math.ceil(latas1)} | Preço por lata: R$ {latas1:.2f}")
print(f"Preço total: R$ {preco1:.2f}")
