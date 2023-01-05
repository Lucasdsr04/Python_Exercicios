"""
Faça um programa que leia a 
largura e a altura de uma 
parede em metros, calcule sua
área e a quantidade de tinta 
necessária para pinta-la sabendo
que cada litro de tinta pinta
uma área de 2m²
"""

altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))

area = altura * largura 

print(f'A parede tem {area} m² então você precisará de {(area+0.99)//1} litros de tinta para pintá-la')