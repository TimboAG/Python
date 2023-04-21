numero= int(input("Ingrese un numero entero: "))

if numero !=0:
  if numero >0:    
    if numero%2 == 0:
      print("Es par positivo")
    else:
      print("es impar positivo")
  else:
       if numero%2 == 0:
        print("Es par negativo")
       else:
        print("es impar negativo")
else:
  print("El numero ingresado es neutro")

