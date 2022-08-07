'''Faça um programa que leia vários números, calcule e exiba a média desses números.
Obs: a leitura do número 999 indica o fim dos dados de entrada e não deve ser computado na média'''

flag = 999
soma = 0
cont = 0

print('Digite os número:')
num = int(input())

while num != flag:
    soma += num
    num = int(input())
    cont += 1

media = soma/cont
print(f'Média: {media:.1f}')
