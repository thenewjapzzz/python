ganho = float(input('Ganho por hora: '))
horas =float(input('Horas trabalhadas: '))

bruto = ganho * horas

desc_imposto = bruto * 0.11
desc_inss = bruto * 0.08
desc_sindicato = bruto * 0.05
líquido = bruto - desc_sindicato - desc_imposto - desc_inss

print(f'Salário bruto R${bruto :.2f}')
print(f'Imposto de renda R${desc_imposto :.2f}')
print(f'INSS R${desc_inss :.2f}')
print(f'Sindicato R${desc_sindicato :.2f}')
print(f'Salário líquido R${líquido :.2f}')
