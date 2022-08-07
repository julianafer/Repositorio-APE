'''Um motorista anota a marcação do hodômetro do seu veículo antes e após uma viagem,
bem como o número de litros de combustível gastos.
Escreva um programa que leia os 3 dados acima, o preço do litro de combustível, a
capacidade do tanque e mostre:
a) Quilometragem rodada.
b) Quantos quilômetros por litro faz o veículo.
c) Autonomia do veículo.
d) Custo da viagem.'''

antes=float(input('Hodômetro antes da viagem: '))
depois=float(input('Hodômetro depois da viagem: '))
lgastos=float(input('Litros de combustível gastos: '))
preço=float(input('Preço do litro de combustível: '))
capacidade=float(input('Capacidade do tanque: '))

print('\nQuestão 4 letra a')
quilometragem=depois-antes
print(f'A quilometragem rodada foi de {quilometragem}km')

print('\nQuestão 4 letra b')
kml=quilometragem/lgastos
print(f'O veículo anda {kml}km por litro de combustível')

print('\nQuestão 4 letra c')
autonomia=kml*capacidade
print(f'A autonomia do veículo é de {autonomia}km')

print('\nQuestão 4 letra d')
custo=lgastos*preço
print(f'O custo da viagem foi de R${custo}')

