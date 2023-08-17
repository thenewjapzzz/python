#Calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média
#esperada para a viagem.

distância = float(input('Informe a distância da viagem em quilômetros: '))
velocidade_média = float(input('Informe a velocidade média esperada: '))
tempo = distância / velocidade_média

print (f'O tempo da viagem é de {tempo} horas')
