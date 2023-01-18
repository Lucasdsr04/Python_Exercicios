"""
Escreva um programa que pergunte a 
quantidade de KM percorridos por um
caro alugado e a quantidade de dias 
pelos quais ele foi alugado. Calcule
o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por KM
rodado
"""

km = float(input('Digite a quantidade de KM percorridos: '))
days = float(input('Digite a quantidade de dias de aluguel: '))

print(f'O preço total foi de R${(km * 0.15) + (days * 60):.2f}')