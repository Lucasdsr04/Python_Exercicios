"""
Crie um programa que leia o nome de uma
pessoa e diga se ela tem 'Silva' no nome
"""

nome = str(input('Digite seu nome: ')).strip()

silva = "SILVA" in nome.upper()

print(f'Tem "Silva" no nome: {silva}')