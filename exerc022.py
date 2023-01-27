"""
Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços). 
- Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite seu nome: ')).strip()
separa = nome.split()

print(f'Em maiúsculo: {nome.upper()}')
print(f'Em minúsculo: {nome.lower()}')
print(f'Quantas letras no nome todo: {len(nome) - nome.count(" ")}')
print(f'Quantas letras no primeiro nome: {len(separa[0])} ')