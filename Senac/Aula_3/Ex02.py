# Implemente uma função que receba dois números
# e uma operação (+, -, *, /) e devolva o resultado.


def calculadora(numero1: int, numero2: int, operacao: str):
    
    if operacao == '+':
        print(f'Soma: {numero1 + numero2}')
              
    elif operacao == '-':
        print(f'Subtração: {numero1 - numero2}')
    
    elif operacao == '*':
        print(f'Multiplicação: {numero1 * numero2}')

    elif operacao == '/':
        print(f'Divisão: {numero1 / numero2}')
                 
                 

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o primeiro segundo: "))
operation = (input("Qual operação +, -, *, /: "))



calculadora(num1, num2, operation)
