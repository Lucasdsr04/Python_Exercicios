#Crie um programa que leia algo pelo teclado e mostre informações acerca do que foi lido 
x = input('Digite algo: ')
print('O tipo primitivo é ', type(x))
print('Só tem espaços? ', x.isspace())
print('É numérico? ', x.isnumeric())
print('É alfabético? ', x.isalpha())
print('É alfanumérico? ', x.isalnum())
print('Está em maiúsculas? ', x.isupper())
print('Está em minúsculas?', x.islower())
print('Está capitalizada? ', x.istitle())
