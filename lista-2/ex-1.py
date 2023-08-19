a = int(input('L1: '))
b = int(input('L2: '))
c = int(input('L3: '))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Não forma um triangulo')
elif a == b == c:
    print('Triangulo equilátero')
elif (a == b) or (b == c) or (a == c):
    print('Triangulo isosceles')
else:
    print('Triangulo escaleno')
