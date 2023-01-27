"""
Faça um programa que leia o nome completo de uma
pessoa. Mostrando em seguida o primeiro e 
o último nome separadamente
"""

nome = str(input('Digite seu nome: ')).strip()

n = nome.split()

print(f'Primeiro nome: {n[0]}')
print(f'Último nome: {n[len(n) - 1]}')
