"""
Desenvolta um programa que pergunte a distância de uma 
viagem em Km. Calcule o preço da passagem, cobrando R$0,50km
para viagens de até 200Km e R$0,45 para viagens mais longas.
"""

km = float(input('Digite a distância em km da sua viagem: '))

if (km < 200):
    print(f'Sua passagem custará R${km * 0.50:.2f}')

else:
    print(f'Sua passagem custará R${km * 0.45:.2f}')