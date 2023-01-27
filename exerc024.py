"""
Crie um programa que leia o nome de uma
cidade e diga se ela começa ou naõ com 
o nome 'SANTO'
"""

cidade = str(input('Digite o nome de uma cidade: ')).strip()
r = 'SANTO' in cidade.upper()
print(f'A cidade digitada possui "Santo" no nome: {r}')