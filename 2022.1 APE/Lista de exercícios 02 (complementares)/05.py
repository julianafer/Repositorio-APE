'''Escreva um programa para determinar as raízes de uma equação de segundo grau, dados os seus coeficientes. Fórmulas:

x=-b+-raízdeΔ  ,onde   Δ=b^2-4ac
      2a

Obs: se Δ for negativo, não existem as raízes da equação.
Dica: use a função sqrt do módulo math.'''

print('Digite os coeficientes de equação: ')
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))
import math

delta = (b**2) - (4*a*c)

if delta < 0:
    print('Não há raízes para delta negativo')
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f'As raízes são {x1} e {x2}')
