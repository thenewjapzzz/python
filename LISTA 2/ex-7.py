a = int(input('Área: '))
if a / 54 == 0:
    latas = a / 54
else:
    latas = int(a / 54) + 1
valor = latas * 80

print(f'Necessário {latas} latas')
print(f'Valor de R${valor :.2f}')
