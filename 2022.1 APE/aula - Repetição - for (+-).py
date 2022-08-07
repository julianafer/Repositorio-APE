#Ler 5 idades e determinar a maior e a menor delas
n=5
maior=0 #menor valor possível
menor=1000 #maior valor possível

print(f'Digite as {n} idades:')

for i in range(n):
    idade=int(input())
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade

print(f'Maior idade: {maior}')
print(f'Menor idade: {menor}')



#Ler 5 números e determinar a maior e a menor deles
n=5
print(f'Digite as {n} números:')

for i in range(n):
    numero=int(input())
    if i == 0:
        maior=numero
        menor=numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')


#Ler o nome e a idade de 5 pessoas e determinar a pessoa mais velha e a pessoa mais nova (obs: suponha a inexistência de empates)
n=5
idademaior=0 #menor valor possível
idademenor=1000 #maior valor possível

print(f'Digite o nome e a idade das {n} pessoas')

for i in range(n):
    nome=input('\nNome: ')
    idade=int(input('Idade: '))
    if idade > idademaior:
        idademaior = idade
        nomemaior=nome
    if idade < idademenor:
        idademenor = idade
        nomemenor=nome

print(f'\nMaior idade: {nomemaior} com {idademaior} anos')
print(f'Menor idade: {nomemenor} com {idademenor} anos')
