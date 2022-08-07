'''Escreva um programa que tenha a funcionalidade de uma calculadora simples.
O programa deve solicitar a digitação de dois operandos e um operador (+ - x * / %) e deve imprimir ao resultado da operação aritmética.
Caso o usuário digite um operador inválido, o programa deve imprimir "Operador desconhecido".'''

x=int(input('1º operando: '))
y=int(input('2º operando: '))
op=input('Operador: ')

print('\nResultado: ', end='')
if op=='+' :
    print(x+y)
elif op=='-' :
    print=(x-y)
elif op=='x' or op=='*' :
    print=(x*y)
elif op=='/' :
    print=(x/y)
elif op=='%' :
    print=(x%y)
else:
    print('Operador desconhecido')
