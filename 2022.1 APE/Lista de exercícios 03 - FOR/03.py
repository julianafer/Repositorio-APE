'''Faça um programa que calcule e mostre o fatorial de um número N, fornecido
pelo usuário. A definição de fatorial é mostrada a seguir:
N! = 1 x 2 x 3 x...x N-1 x N
0! = 1'''

n=int(input('Número: '))
fat=1
for i in range(1,n+1):
    fat=fat*i
print(f'Fatorial de {n}!: {fat}')
