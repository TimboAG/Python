


def palindromo(cadena):
  cadena = cadena.replace(" ", "")
  cadena = cadena.lower()
  cadenaInvertida= cadena[::-1]
  if cadena == cadenaInvertida:
    print("la palabra ingresada es palindromo")
  else:
    print("la palabra ingresada no es palindromo")
  # cadenaLista= list(cadena)
  # aux=0
  # for n in range(0, len(cadenaLista)):
  #  i=len(cadenaLista)-n
  #  if cadenaLista[n] == cadenaLista[i-1]:
  #    aux+=1    
  # if aux == len(cadenaLista):
  #  print("la palabra ingresada es palindromo")
  # else:
  #   print("la palabra ingresada no es palindromo") 

def main():
  cadena=input("ingrese un palabra para verificar si es palindromo: ")
  palindromo(cadena)

if __name__== "__main__":
  main()