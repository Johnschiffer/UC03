# Exercício 8 : Cálculo IRPF
# Escreva um programa para ler o salário de um funcionário,
# e calcular o IRPF que precisa ser descontado do salário.
# No Brasil, a tabela do Imposto de Renda para pessoas físicas
# (IRPF) é progressiva, ou seja, as alíquotas aumentam conforme
# a renda do contribuinte. A tabela é ajustada anualmente e varia
# de acordo com a faixa de salário. Para o ano de 2024, as faixas
# de tributação do Imposto de Renda para pessoas físicas são as seguintes:
# Até R$ 2.112,00: isento (não paga imposto de renda)
# De R$ 2.112,01 até R$ 2.826,65: 7,5% (aplica-se sobre o valor que exceder a R$ 2.112,00)
# De R$ 2.826,66 até R$ 3.751,05: 15% (aplica-se sobre o valor que exceder a R$ 2.826,65)
# De R$ 3.751,06 até R$ 4.664,68: 22,5% (aplica-se sobre o valor que exceder a R$ 3.751,05)
# Acima de R$ 4.664,68: 27,5% (aplica-se sobre o valor que exceder a R$ 4.664,68)

salarioAtual = 0
salario = float(input("Digite seu sálario: "))

if salario <= 2111:
    desc = salario * 0.075
    salarioAtual = salario - salarioAtual
    print(f'Você não tem desconto IR')

elif salario <= 2826:
    desc = salario * 0.075
    salarioAtual = salario - salarioAtual
    print(f'O desconto será de 7.5% {desc} e ficará R$ {salarioAtual}')

elif salario <= 3751:
    desc = salario * 0.15
    salarioAtual = salario - salarioAtual
    print(f'O desconto será de 15% {desc} e ficará R$ {salarioAtual}')

elif salario <= 4664:
    desc = salario * 0.225
    salarioAtual = salario - salarioAtual
    print(f'O desconto será de 22.5% {desc} e ficará R$ {salarioAtual}')

elif salario <= 4664:
    desc = salario * 0.275
    salarioAtual = salario - salarioAtual
    print(f'O desconto será de 27.5% {desc} e ficará R$ {salarioAtual}')
    