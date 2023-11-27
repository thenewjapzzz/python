#Faça um programa que crie dois vetores com 10 elementos aleatórios
#entre 1 e 100. Gere um terceiro vetor com 20 elementos, cujos valores
#deverão ser compostos pelos elementos intercalados dos dois outros vetores.
#Imprima os três vetores

from random import randint
vetor_1 = []
vetor_2 = []
vetor_3 = []
for k in range (10):
    x = randint (1, 100)
    vetor_1.append(x)
    vetor_3.append(x)
    x = randint (1, 100)
    vetor_2.append(x)
    vetor_3.append(x)

print('Vetor 1:', vetor_1)
print('Vetor 2:', vetor_2)
print('Vetor 3:', vetor_3)