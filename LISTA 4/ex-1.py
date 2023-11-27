#Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra
#o maior e o menor valor, sem usar as funções max e min

from random import sample
lista = sample(range(100), 10)
maior = menor = lista[0]
for x in lista [1:]:
    if x > maior : maior = x
    if x < menor : menor = x

print('Lista:',lista)
print(f'Maior: {maior}')
print(f'Menor: {menor}')



