from math import sin, cos, tan, radians
"""
Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e 
tangente desse ângulo
"""

ang = float(input('Digite o ângulo desejado: '))

seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print(f'O ângulo de {ang} tem o seno de {seno:.2f}')
print(f'O ângulo de {ang} tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {ang} tem a tangente de {tangente:.2f}')