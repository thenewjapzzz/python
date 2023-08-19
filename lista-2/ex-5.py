a = int(input('N1: '))
b = int(input('N2: '))
c = int(input('N3: '))

maior = a
if b > a:
    maior = b
if c > b:
    maior = c

menor = a
if b < a:
    menor = b
if c < b:
    menor = c

print(f'O maior é {maior} e o menor é {menor}')
