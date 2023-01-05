"""
Faça um programa que leia um número
inteiro qualquer e mostre na tela
a sua tabuada
"""

n1 = int(input('Digite um número inteiro: '))

for x in range (10):
    print(f'{n1} x {x+1} = {n1*(x+1)}')
