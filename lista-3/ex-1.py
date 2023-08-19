nota = float(input('Uma nota de zero a dez: '))
while (nota > 10) or (nota < 0):
    print('Tente novamente ')
    nota = float(input('Uma nota de zero a dez: '))
if (nota <= 10) or (nota >= 0):
    print('Nota válida')
