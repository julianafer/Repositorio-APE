'''O restaurante a quilo Bem-Bão cobra R$25,00 por cada quilo de refeição. Faça um
programa que leia o peso do prato montado pelo cliente (em quilos) e exiba o valor
a pagar. Assuma que a balança já desconte o peso do prato.'''
quilos=float(input('Informe o peso, em quilos, da sua refeição: '))
valor=quilos*25
print(f'Sua refeição custará R${valor}')
