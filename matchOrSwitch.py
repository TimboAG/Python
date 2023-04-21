vocal= input("Ingrese un caracter para saber si es vocal: ")
if len(vocal) > 1:
  print("ha ingresado una palabra no un caracter")
else:
  match vocal.upper() :
   case "A":
       print("La vocal ingresada es A")
   case "E":
       print("La vocal es E")
   case "I":
       print("La vocal es I")
   case "O":
       print("La vocal es O")
   case "U":
       print("La vocal es U")
   case _:
    print("no es vocal")
  
  