'''Escreva um programa que leia o peso (kg) e a altura (m) de uma pessoa, determine e mostre o seu grau de obesidade,
de acordo com a tabela seguinte. O grau de obesidade é determinado pelo índice de massa corpórea,
cujo cálculo é realizado dividindo-se o peso da pessoa pelo quadrado da sua altura.

MASSA CORPÓREA        GRAU DE OBESIDADE
     <26                   normal
 >=26 e <30                obeso
     >=30              obeso mórbido
'''

peso=float(input('Peso(kg): '))
altura=float(input('Altura(m): '))
massa=peso/(altura**2)

if massa < 26:
    obesidade='normal'
elif massa >= 26 and massa < 30:
    obesidade='obeso'
else:
    obesidade='obeso mórbido'

print(f'Grau de obesidade: {obesidade}')
