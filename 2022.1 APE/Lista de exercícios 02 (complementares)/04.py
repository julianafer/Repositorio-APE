'''Escreva um programa que leia a hora de início de um jogo e a hora do final do jogo (considerando
apenas horas inteiras), calcula a duração do jogo em horas, sabendo-se que o tempo máximo de
duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.
O programa deve mostrar o resultado obtido.'''

hi=int(input('Hora inicial: '))
hf=int(input('Hora final: '))

if hf > hi:
    duracao=hf-hi
else:
    duracao=(24-hi)+hf

print(f'Duração: {duracao} hora(s)')
