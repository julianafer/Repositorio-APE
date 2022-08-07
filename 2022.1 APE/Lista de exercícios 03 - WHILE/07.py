'''Faça um programa que leia a idade de várias pessoas visitantes de um show
(a leitura da idade 0 indicará o fim dos dados de entrada), calcule e exiba:
• A média de idade do público;
• A porcentagem de pessoas com idade entre 18 e 21 anos;
• Idade do visitante mais jovem.'''

flag=0
geral=0
todas=0
jovens=0

print(f'Digite as idades das pessoas que foram ao show: (digite {flag} para parar)')
idade=int(input())
menor=idade

while idade != flag:
    todas+=idade
    geral+=1
    if idade >= 18 and idade <= 21:
        jovens+=1
    if idade < menor:
        menor=idade
    idade=int(input())

media=int(todas/geral)
porcentagem=int((100*jovens)/geral)

print(f'A média de idade do público: {media} ')
print(f'A porcentagem de pessoas com idade entre 18 e 21 anos: {porcentagem}%')
print(f'Idade do visitante mais jovem: {menor} anos')
