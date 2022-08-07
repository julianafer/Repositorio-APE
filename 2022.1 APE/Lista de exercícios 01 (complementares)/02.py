'''Escreva um programa para calcular e exibir a média ponderada de 2 notas dadas. Sabe-
se que nota1 possui peso 6 e nota2 possui peso 4.'''
nota1=float(input('Primeira nota (peso 6): '))
nota2=float(input('Segunda nota (peso 4): '))
x=nota1*6
y=nota2*4
z=x+y
média=z/10
print(f'Sua média é {média}')
