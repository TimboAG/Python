lista = [1, 2, 3, 4, 5, 6]

# muestro los datos de la lista
print("-" * 10)
print("este es lista in lista:")
for elemento in lista:
  print(elemento)
print("-" * 10)

# muestro los datos de la lista
ultimo = len(lista)
print("este es i in range, salteando un numero:")
for i in range(0, ultimo, 2):
  print(lista[i])
print("-" * 10)

  # muestro los pares
print("muestro los pares:")
for i in lista:
    if i % 2 != 0:
        continue
    print(i)
print("-" * 10)

# busco un numero especific de la lista
aux = len(lista)
print("busco un numero especific de la lista,  ejemplo el 2:")
for n in lista:
    if n == 2:
        print("Se encontro el numero 2")
        break
    else:
      if n == aux-1:
        print("no se encontro el numero 2")      
print("-" * 10)

