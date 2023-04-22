#un conjunto no puede almacenar un valor que se repita

#si le coloco una palabra me genera un conjunto con cada una de sus letras sin repetrirse..
a= set("abracadabra")
print(a)

#si resto un conjunto con otro me muestra las letras que comparten entre las dos palabras
b=set("alacazam")
c= a- b
print(c)

#si quiero mostrar las letras que contiene los dos conjuntos
c = a | b
print(c)

#si quiero mostrar las letras que comparten o son iguales en  los dos conjuntos
c = a & b
print(c)

#si quiero mostrar las letras que no comparten o son iguales en  los dos conjuntos
c = a  ^ b
print(c)

#agregar nuevo dato
a.add("x")
print( a)

#eliminar un elemento especifico 
a.discard("b")
print( a)
