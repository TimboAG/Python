# Práctica 01: Calcular cociente y residuo 
# Enunciado: hallar el cociente y el residuo (resto) de dos numeros enteros.
# Análisis: para la solución se requiere que el usuario ingrese dos numeros enteros, el sistema realice el cálculo para hallar el cociente y el residuo

num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))
suma= num1 + num2
cociente=  num1// num2
residuo= num1%num2
print(f"La suma es: {suma} \nEl cociente es: {cociente} \nEl residuo es: {residuo}")
