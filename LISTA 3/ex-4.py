#A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
#formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
#soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o
#seu número de Fibonacci

n = int(input('Digite um número: '))
a, b = 1, 1 
c = 1 

while c <= n-2:
    a , b = b , a + b 
    c = c + 1

print (b)
