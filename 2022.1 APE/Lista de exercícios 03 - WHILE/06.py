'''Chico tem 1,50 metros e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metros e cresce 3 centímetros por ano.
Faça um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.'''

m_chico = 150
m_ze = 110
ano = 1

while m_chico != m_ze:
    m_chico += 2
    m_ze += 3
    ano += 1

print(f'Depois de {ano} anos, Chico e Zé tem a mesma altura')
