import math as m 

#redondeo para abajo
miMath= m.floor(4.99)
print(miMath)

#redondeo para arriba
miMath= m.ceil(4.01)
print(miMath)

#suma cadena  respetando los valores reales
cadena=[1,2,3,4,0.676543]
miMath= m.fsum(cadena)
print(miMath)

#truncar, ignorarme la parte decimal
miMath= m.trunc(45.098)
print(miMath)

#potencia
miMath= m.pow(2,3)
print(miMath)


#resultado de la raiz cuadrada
miMath= m.sqrt(13)
print(miMath)

#valor de pi
miMath= m.pi
print(miMath)

#valor de euler
miMath= m.e
print(miMath)
