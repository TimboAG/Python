import collections
#en las tuplas no se pueden agregar datos ni modificarlos 

tupla=("hola", "mundo", "hola", "hola")
print("tupla original: ", tupla)

#buscar el indice de un dato especifico
indice=tupla.index("mundo")
print("buscar el indice de un dato especifico index(mundo): ", indice)

#cuantos elementos especificos hay en una tupla
cantidad= tupla.count("hola")
print("cuantos elementos especificos hay en una tupla count(hola): ", cantidad)

#cuantos elementos  hay en una tupla importar collections
collectionCounter= collections.Counter(tupla)
print("cuantos elementos hay en una tupla collections.counter", collectionCounter)

