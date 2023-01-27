"""
Escreva um programa que leia a velocidade de
um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado.
a multa vai custar R$7,00 por cada km acima do limite 
"""

vel = float(input('Digite sua velocidade em km/h: '))

if (vel > 80):
    print(f'Você foi multado em R${(vel - 80) * 7:.2f}, velocidade máxima permita "80km/h"')

else:
    print('Dentro do limite permitido, continue assim!')