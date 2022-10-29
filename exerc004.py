from sys import breakpointhook


x = input('Digite algo: ')
print('O tipo primitivo é ', type(x))
print('Só tem espaços? ', x.isspace())
print('É numérico? ', x.isnumeric())
print('É alfabético? ', x.isalpha())
print('É alfanumérico? ', x.isalnum())
print('Está em maiúsculas? ', x.isupper())
print('Está em minúsculas?', x.islower())
print('Está capitalizada? ', x.istitle())
