from random import choice
"""
Um professor quer sortear um dos seus 4 alunos
para apagar o quadro. Faça um programa que ajude
ele lendo o nome dos alunos e escrevendo o nome
do escolhido
"""

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1, a2, a3, a4]

escolhido = choice(lista)

print(f'O aluno escolhido foi {escolhido}')

