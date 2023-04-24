import random

pares = []
impares = []
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for n in numeros:
    numeroRandom = random.randint(1,100)
    resultado = n * numeroRandom

    if resultado % 2 == 0:
        print(f'{n} x {numeroRandom} = {resultado}')
        pares.append(resultado)
    else:
        print(f'{n} x {numeroRandom} = {resultado}')
        impares.append(resultado)

print('LISTA DE PARES: ', pares)
print('LISTA DE IMPARES: ', impares)