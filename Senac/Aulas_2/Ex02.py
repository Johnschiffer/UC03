# Exercício 2: Soma de Números Positivos
# Escreva um programa que receba números inteiros do usuário até que um número negativo seja digitado. 
# Exiba a soma de todos os números positivos digitados.

num = 0
soma = 0
while (num >= 0):
      num = int(input("Digite um numero: "))

      if (num >= 0):
        soma += num
      
else:
    print(soma)
    