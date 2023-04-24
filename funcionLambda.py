#funcion sin nombre, funcion anonima, se crea con la palabra reservada lambda, diseñada para expresiones pequeñas

sumar=lambda a,b: a+b

print(sumar(10,20))

duplicar= lambda n: n *2
print(duplicar(10))

par= lambda n: n%2 == 0
impar= lambda n: n%2 != 0
# def esPar(n):
#   if(par(n) == True):
#     return "Es par"
#   else:return "Es impar"
# print(esPar(2))  
print(par(2))  
print(impar(2))  



revertir= lambda n: n[::-1]
print(revertir("Hola"))