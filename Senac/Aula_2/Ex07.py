# Exercício 7: Média salarios
# Escreva um programa para ler o salário
# e o sexo de vários funcionários
# (defina uma cláusula para terminar a leitura)
# ao término, informar a média de salário de homens
# e mulheres


salarioM = salarioF = contagemM = contagemF = somaM = somaF = mediaM = mediaF = 0
# somaM = 0
# somaF = 0
# contagemM = 0
# contagemF = 0
sexo = ''

while True:
    
    sexo = (input("Homem ou Mulher?: h/m "))    

    if sexo == 'h':
        salarioM = float(input("Digite seu sálario: "))
        somaM += salarioM
        contagemM += 1
    
    if sexo == 'm':
        salarioF = float(input("Homem ou Mulher?: h/m "))
        somaF += salarioF
        contagemF += 1

    continuar = (input("Continuar S/N ")).strip().upper()

    if continuar == 'N':
        break
    
mediaM = somaM / contagemM
mediaF = somaF / contagemF

print(f'A média salarial dos homens: {mediaM}')
print(f'A média salarial dos mulheres: {mediaF}')

    

