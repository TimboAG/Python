def esPrimo():
  numero = float(input("Ingrese una numero entero para saber si es primo: "))  
  numeroEntero=int(numero)
  if numero == numeroEntero and numeroEntero > 0:
    contador = 0
    for i in range(1, numeroEntero+1):
        if i == 1 or i == numeroEntero:
            continue
          
        if numeroEntero % i == 0:
            contador += 1

    if contador == 0:
        print("El numero ingresado es pirmo")
    else:
        print("El numero ingresado no es pirmo")
        
  else:
    print("El numero debe ser entero y mayor a 0")

def main():
  esPrimo()

if __name__ == "__main__":
  main()