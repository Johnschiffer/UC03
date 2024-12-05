# Exercício 1: Saudações Personalizadas
# Crie uma função cumprimentar que receba o nome e a hora do dia,
#  e retorne uma mensagem personalizada. Bom dia, Boa tarde ou Boa noite.


def saudacao(nome, hora):
    if hora < 12:
        print(f'Bom dia, {nome}!')
    
    elif hora > 12 and hora < 18:
        print(f'Boa tarde, {nome}!')

    else:
        print(f'Boa noite,{nome}!')


name = input("Digite seu nome: ")
horas = int(input("Digite a hora atual: "))

saudacao(name, horas)
