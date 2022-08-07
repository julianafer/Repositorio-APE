'''Faça um programa que leia um número inteiro N, calcule e mostre o maior quadrado perfeito menor ou igual a N.
Por exemplo, se N for igual a 38, o resultado é 36.'''

import math
maior = 0
n = int(input('Digite um número inteiro: '))

for i in range(1,n+1):                      #vai testar todos os números entre 1 e N
    raiz = math.sqrt(i)                     #vai fazer a raíz de todos
    if raiz == int(raiz) and i > maior:     #se a raíz for um inteiro com um quadrado perfeito
        maior = i                           #ele vai assumir esse valor como maior até realmente obter o maior quadrado perfeito

print(f'Maior quadrado perfeito: {maior}')
