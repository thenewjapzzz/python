texto = '''The Python Software Foundation and the global Python
community welcome and encou
rage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your backgrou
nd, we welcome you''' .lower()

import string
for x in string.punctuation:
    texto = texto.replace(x, '')

lista = []
for i in texto.split:
    if i[0] in 'python' or i[-1] in 'python':
        lista.append(i)

print(lista)
    