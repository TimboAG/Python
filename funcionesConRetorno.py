nombre= "mi nombre"
def saludar():
  #variable global
  global var1
  var1="soy una variable global"
  nombre= "mi nombre"
  edad= 20
  return "Hola desde la funcion saludar " + nombre + " " +  str(edad)

valorDelReturn= saludar()
print("Mostrando valor de retorno desde una variable: ", valorDelReturn)
print(saludar())