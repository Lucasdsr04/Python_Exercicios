"""
Escreva um programa que pergunte o salário de um 
funcionário e calcule o valor do seu aumento.
para salários superiores a R$1.250.00 calcule aumento de 10%
para salários inferiores ou iguais, 15% de aumento 
"""

wage = float(input('Digite seu sálario: R$'))

if (wage > 1250):
    print(f'Seu salário de R${wage} vai aumentar para R${wage * 1.10:.2f}')
else:
    print(f'Seu salário de R${wage} vai aumentar para R${wage * 1.15:.2f}')

