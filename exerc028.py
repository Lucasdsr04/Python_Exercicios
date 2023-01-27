from random import choice
"""
Escreve um programa que faça o computador 
pensar em um número de 0 a 5 e peça para 
o usuário tentar descobrir qual foi o número
escolhido pelo computador.
O programa deverá escrever na tela se o usuário
venceu ou perdeu
"""

tentativa = int(input('Tente advinhar o número secreto de 0 a 5: '))

nums = [0, 1, 2, 3, 4, 5]

escolha = choice(nums)

if tentativa == escolha:
    print('ACERTOU, PARABéNS')

else:
    print(f'VOCÊ ERROU O NUMERO ERA {escolha}')    