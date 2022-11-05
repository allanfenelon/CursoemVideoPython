"""
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""
msg = 'Seja bem vindo {0}'
name = input('Digite seu nome: ')
print(msg.format(name))