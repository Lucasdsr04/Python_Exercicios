"""
Crie um programa que leia quanto
dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode
comprar 
considere $1 = R$5,45 (cotação 04/01/23)
"""

cash = float(input('Digite seu saldo: R$ '))
print(f'Com R${cash:.2f} Você pode comprar: {cash/5.45:.2f} dólares')