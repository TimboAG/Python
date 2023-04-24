
def saludar(nombre):
  return f"Hola desde la funcion saludar {nombre}"

valorDelReturn= saludar("mi nombre")
print("Mostrando valor de retorno desde una variable: ", valorDelReturn)
print(saludar("mi nombre"))

def suma(a, b):
  return a + b

print("Esta es la suma de 2 + 1: ", suma(2,1))


def resta(a, b):
  return a - b

miResta= resta(b=20, a=10)
print("Esta es la resta de 10 - 20: ", miResta)

#Ai no envio ningun valor
def resta2(a=None, b=None):
  if a== None and b!= None :
    return "El  valor de a es vacio, no se pueden restar"
  elif b== None and a!=None:
     return "El  valor de b es vacio, no se pueden restar"
  elif a== None and b==None:
        return "El  valor de a y b es vacio, no se pueden restar"  
  else:
    return a - b

miResta2= resta2(b=20, a=10)
print("Esta es la resta de 10 - 20: ", miResta2)
#Si envio a vacio
miResta2= resta2(b=20)
print("Esta es la resta con a vacio: ", miResta2)

#Si envio b vacio
miResta2= resta2(a=20)
print("Esta es la resta con b vacio: ", miResta2)

#Si envio a y b vacio
miResta2= resta2()
print("Esta es la resta con a y b vacio: ", miResta2)