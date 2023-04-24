#Si nose cuantos parametros voy a recibir o cuantos argumentos voy a enviar

#funcion sumar n numeros
def sumar(*args):
  suma=0
  for n in args:
    suma+= n
  return suma

total= sumar(1,2,3,4,5,6)
print("La suma total es: ", total)


total= sumar()
print("La suma total es: ", total)


#argumentos indeterminados por nombre
#args = tupla
#kwargs = diccionario
def sumar2(*args, **kwargs):
  suma=0
  for n in args:
    suma+= n
  return suma, kwargs

total= sumar2(1,2,3,4,5,6, nombre= "mi nombre", nombre2= "miNombre2", edad= 23)
print("La suma total es con argumentos indeterminados por nombre: ", total)