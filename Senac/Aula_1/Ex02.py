# Exercício 2

# Um determinado prêmio de loteria saiu para um bolão de três amigos. Uma lei garante
# que todo prêmio de loteria deva pagar um imposto de 7% para os cofres estaduais.
# Do total descontado o imposto, os amigos irão dividir o prêmio da seguinte maneira:
# O primeiro ganhador recebera 46%;
# O segundo recebera 32%;
# O terceiro recebera o restante; Faça um programa que leia o valor total do prêmio,
# calcule o desconto, o valor que cada um tem direito e imprima o total do prêmio,
# o premio descontado o imposto e a quantia recebida por cada um dos ganhadores.


premio = float(input("Digite o valor do premio: "))

imposto = premio * 0.07
premio_desc = premio - imposto

ganhador1 = premio_desc * 0.46
ganhador2 = premio_desc * 0.32
ganhador3 = premio_desc - ganhador1 - ganhador2

print(f"Premio: R$ {premio:.2f}\nDesconto: R$ {imposto:.2f}\nGanhar 1: R$ {ganhador1:.2f}\nGanhar 2: R$ {ganhador2:.2f}\nGanhar 3: R$ {ganhador3:.2f}")
