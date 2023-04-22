diccionario = {"uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6}

# mostrar su valor según su clave
print("mostrar su valor según su clave diccionario[uno]: ", diccionario["uno"])

# agregar un nuevo elemento. Cuando agregamos un nuevo elemento las claves no pueden repetirse
diccionario["siete"] = 7
print("agregar un nuevo elemento ", diccionario)

# modifico el valor de un elemento
diccionario["cinco"] = 7
print("modifico el valor de un elemento ", diccionario)

# buscar un elemento por su clave y si no encuentra mostrar un mensaje
print("buscar un elemento (cuatro) por su clave y si no encuentra mostrar un mensaje ", diccionario.get("cuatro", "no se encontró el número"))

# buscar un elemento por su clave y si no encuentra mostrar un mensaje
print("buscar un elemento (ocho) por su clave y si no encuentra mostrar un mensaje ", diccionario.get("ocho", "no se encontró el número"))

# mostrarme todas las claves que tiene
print("mostrarme todas las claves que tiene ", diccionario.keys())

# mostrarme todas los valores que tiene
print("mostrarme todas los valores que tiene ", diccionario.values())

# mostrarme todas los valores y sus claves que tiene
print("mostrarme todas los valores y sus claves que tiene", diccionario.items())

# eliminar un elemento por su clave
diccionario.pop("cinco")
print("eliminar un elemento por su clave", diccionario)

# eliminar un elemento por su clave, con mensaje opcional si no se encuentra
diccionario.pop("cinco", "no se encontró la clave")
print("eliminar un elemento por su clave con mensaje si no se encuentra", diccionario)


# mostrar las claves con un for
for clave in diccionario:
    print(clave)

# mostrar los valores con un for
for valor in diccionario.values():
    print(valor)
    
# mostrar las claves y valores con un for
for clave, valor in diccionario.items():
    print(clave, valor)
    