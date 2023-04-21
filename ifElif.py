vocal= input("Ingrese un caracter para saber si es vocal: ")
if len(vocal) > 1:
  print("ha ingresado una palabra no un caracter")
else:
 if vocal == "a" or vocal == "A":
  print("La vocal ingresada es A")
 elif vocal == "e" or vocal == "E":
  print("La vocal es E")
 elif vocal == "i" or vocal == "I":
  print("La vocal es I")
 elif vocal == "o" or vocal == "O":
  print("La vocal es  O ")
 elif vocal == "u" or vocal == "U":
  print("La vocal es U")
 else:
  print("no es vocal")