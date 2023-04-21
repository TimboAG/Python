vocal= "None"
separador= '-' * 50
while vocal != "S" :
   print(separador)
   vocal= input("Ingrese un caracter para saber si es vocal, para terminar ingrese la letra S:  ")
   vocal= vocal.upper()
   if len(vocal) > 1:
    print("ha ingresado una palabra no un caracter")
   else:
    if vocal == "A":
     print("La vocal ingresada es A")     
    elif  vocal == "E":
     print("La vocal es E")
    elif  vocal == "I":
     print("La vocal es I")
    elif  vocal == "O":
     print("La vocal es  O ")
    elif vocal == "U":
     print("La vocal es U")
    else:
     print("no es vocal")