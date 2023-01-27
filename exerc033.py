"""
Faça um programa que leia três números e 
mostre qual é o maior e qual é o menor.
"""

primeiro = float(input('Digite o primeiro número: '))
segundo = float(input('DIgite o segundo número: '))
terceiro = float(input('Digite o terceiro número: '))

if(terceiro > segundo):
    trocar = terceiro
    terceiro = segundo
    segundo = trocar

if(segundo > primeiro):
    trocar = segundo
    segundo = primeiro
    primeiro = trocar

if(terceiro > segundo):
    trocar = terceiro
    terceiro = segundo
    segundo = trocar

print(f'O maior valor digitado foi {primeiro} ')
print(f'O menor valor digitado foi {terceiro} ')