from math import sqrt
"""
Faça um programa que leia o comprimento do 
cateto oposto e do adjacente de um triângulo
retângulo, calcule e mostre o comprimento da
hipotenusa
"""

ca = float(input('Digite o comprimento do cateto adjacente: '))
co = float(input('Digite o tamanho do cateto oposto: '))

hip = sqrt(ca**2 + co**2)

print(f'A hipotenusa tem {hip:.2f} de comprimento')