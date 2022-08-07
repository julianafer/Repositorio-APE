'''Faça um programa que calcule e mostre os números múltiplos de 5 do
intervalo 50 a 300, juntamente com suas raízes e seus cubos.'''

import math
print('    x     raíz(x)  cubo(x)')
print('-'*30)
for i in range(50,301,5):
    raiz=math.sqrt(i)
    cubo=i**3
    print(f'{i:5}{raiz:10.2f}{cubo:10}')
