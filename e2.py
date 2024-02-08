'''
David Muñoz
Pol Danés
Yeray Lopez
24 gener 2024

Mitjana de nombre aleatoriss
'''
import random
MAX= 100
numeros = [random.randint(1, 50) for _ in range(MAX)]
numeros_parelles = numeros[1::2]
media_parelles = (sum(numeros_parelles) // len(numeros_parelles))
numeros_senars = numeros[::2]
media_senars = sum(numeros_senars) // len(numeros_senars)

print(numeros)
print("mitjana posicions parelles:",media_parelles)
print("mitjana posicions senars:",media_senars)
