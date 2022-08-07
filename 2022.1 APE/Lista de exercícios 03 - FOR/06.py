'''Faça um programa que leia 3 números inteiros (N, X, Y) e mostre todos os números múltiplos de N entre X e Y.'''

n=int(input('1º número: '))
x=int(input('2º número: '))
y=int(input('3º número: '))

print(f'Os múltiplos de {n} entre {x} e {y} são:')
for i in range(x,y+1,n):
    print(i,end=' ')
