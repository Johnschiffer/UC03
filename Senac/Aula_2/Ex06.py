# Exercício 6: Média de Números Positivos
# Escreva um programa que receba números inteiros até que
# o usuário digite 0. Calcule e exiba a média dos números
# positivos digitados.


num = 1
soma = 0
contagem = 0
while (num >= 1):
      num = int(input("Digite um numero: "))
      
      if num == 0:
        break
      
      if (num >= 0):
        soma += num
        contagem += 1
    
        
media = soma / contagem
print(media)