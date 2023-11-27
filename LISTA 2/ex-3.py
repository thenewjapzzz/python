peso = int(input('Peso de peixe: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0

print (f'O excesso de peso foi de {excesso}kg e a multa de R${multa}')
