#funciones que se ejecutan a si mismas

def factorial(n):
  if n >1:
    n*=factorial(n-1)
  return n

n= int(input("ingrese un numero  para saber su factorial: "))
print(f"El factorial de {n} es:  {factorial(n)} ")