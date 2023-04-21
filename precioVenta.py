
"""Práctica 02: Calcular precio de venta
Enunciado: dado el valor de venta de 
productos, hallar el IGV (18%) y el 
precio de venta.
Análisis: para la solución de este problema,
se requiere que el usuario ingrese el valor de 
venta del producto y el sistema realice el 
cálculo respectivo para hallar el IGV y el 
precio de venta, para esto use la siguiente 
expresión.
igv = vv * 0.18
pv = vv + igv
"""
precio= float(input("Ingrese el precio: "))
igv= precio * 0.18
pv= precio + igv
print(f"El IGV es: {igv} \nEl precio de venta es: {pv}")
