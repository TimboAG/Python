import collections


lista=["hola", "mundo", "hola", "hola"]
print("Lista original: ", lista)

#agregar dato a la lista
lista.append("nuevo")
print("Agregando datos con append: ", lista)

#agregar dato a la lista en una posicion especifica
lista.insert(0,"en el indice 0")
print("agregar dato a la lista en una posicion especifica insert: ", lista)

#elimino el dato por el valor
lista.remove("en el indice 0")
print("elimino dato con el valor remove: ", lista)

#elimino el ultimo elemento
lista.pop()
print("elimino el ultimo elemento pop: ", lista)

#elimino el elemento segun el indice
lista.pop(0)
print("elimino el elemento segun el indice pop(0): ", lista)

#buscar el indice de un dato especifico
indice=lista.index("mundo")
print("buscar el indice de un dato especifico index(mundo): ", indice)

#cuantos elementos especificos hay en una lista
cantidad= lista.count("hola")
print("cuantos elementos especificos hay en una lista count(hola): ", cantidad)

#cuantos elementos  hay en una lista importar collections
collectionCounter= collections.Counter(lista)
print("cuantos elementos hay en una lista collections.counter", collectionCounter)

#Ordenar de menor a mayor
lista.sort()
print("Ordenar de menor a mayor sort", lista)

#Invertir la lista
lista.reverse()
print("lista invertida reverse", lista)

#Elimino toda mi lista
lista.clear()
print("Elimino toda mi lista clear", lista)