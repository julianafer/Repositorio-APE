'''nota=float(input('Nota: '))
if nota >= 7:
    print('Aprovado')
if nota >= 4 and nota < 7:
    print('Prova final')
if nota < 4:
    print('Reprovado')
print('Fim do programa')'''

nota=float(input('Nota: '))
if nota >= 7:
    print('Aprovado')
else:
    if nota >= 4:
        print('Prova final')
    else:
        print('Reprovado')
print('Fim do programa')
