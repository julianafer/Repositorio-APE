cont = 0
soma = 0

while True:
    idade = int(input('\nDigite a idade (ou 0 p/encerrar): '))
    if idade == 0:
        break
    if idade < 0:
        print('Idade inválida. Digite novamente...')
        continue
    cont += 1
    soma += idade
    
media = soma / cont
print(f'\nMédia das idades = {media:.0f}')
