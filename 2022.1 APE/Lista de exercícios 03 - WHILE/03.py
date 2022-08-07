'''Faça um programa que leia vários números, determine e mostre o maior e o menor deles.
Obs: a leitura do número 0 (zero) encerra o programa.'''

flag = 0

print(f'Digite vários números (para encerrar, digite {flag})')
num = int(input())

maior = num
menor = num

while num != flag:
    if num > maior:
        maior = num
        num = int(input())
    elif num < menor:
        menor = num
        num = int(input())
    else:
        num = int(input())

print(f'Maior: {maior}')
print(f'Menor: {menor}')
