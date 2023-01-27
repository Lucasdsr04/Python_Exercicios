"""
Faça um programa que leia uma frase 
pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez 
"""

nome = str(input('Digite seu nome: ')).strip()

a1 = nome.upper().count('A')
a2 = nome.upper().find('A') 
a3 = nome.upper().rfind('A')

print(f'Quantidade de vezes que a vogal "A" aparece: {a1}')
print(f'Primeira posição da vogal "A": {a2+1}')
print(f'Última posição da vogal "A": {a3+1}')
