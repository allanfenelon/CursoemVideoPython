"""
 Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""
algo = input('Digite algo: ')
print('O tipo desse algo é: {}'.format(type(algo)))
print('Esse algo só tem espaço? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('Está tudo em maiúsculo? ', algo.isupper())
print('Está tudo em minúsculo? ', algo.islower())
print('É alfanúmerico? ', algo.isalnum())
print('É alfabético? ', algo.isalpha())
