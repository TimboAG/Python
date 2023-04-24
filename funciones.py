nombre= "mi nombre"
def saludar():
  #variable global
  global var1
  var1="soy una variable global"
  nombre= "mi nombre"
  print("Hola desde la funcion saludar")
  print("hola ", nombre)
saludar()

print("Saludo desde fuera de la funcion y mi variable global es: ", var1)