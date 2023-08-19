from calendar import isleap
ano = int(input('Ano: '))
if isleap(ano):
    print('Ano bissexto')
else:
    print('Não bissexto')
