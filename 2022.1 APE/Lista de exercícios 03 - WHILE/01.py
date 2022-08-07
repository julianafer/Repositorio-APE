'''Faça um programa que leia 30 números inteiros, calcule e mostre a soma deles
Obs: não use o comando for, use while.'''

n=3
cont=0
soma=0

print(f'Digite {n} números inteiros:')

while cont < n:
    num=int(input())
    soma+=num
    cont+=1
    
print(f'Soma: {soma}')
