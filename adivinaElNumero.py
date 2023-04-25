import random
import sys

def aleatorio(vidas):
    while vidas != 0:
        print("\n" * 2)   
        print("*" * 25)        
        numero = input("Adivina el numero!! Ingresa un numero que crees que saldrá (numero entero de 1-10) Presiona S para salir: \n")
        numeroAleatorio=None
        if numero.isdigit() == True and int(numero)>=1 and int(numero) <= 10:
            numero = int(numero)
            numeroAleatorio= random.randint(1, 10)
            if numero == numeroAleatorio:
                print("\n" * 2)   
                print("*" * 25)                     
                print(f"El numero ingresado es= {numero} \nEl numero que salio es= {numeroAleatorio} ")
                print("Felicidades! adivinaste el numero!")
                vidas=vidas -1
                seguir =input( f"\nQuieres seguir jugando? \n1- Si (Las vidas que te quedan son {vidas} )\n2- No\n3- Volver al menu Principal \n")
                if seguir.isdigit() == True and vidas !=0:
                    seguir = int(seguir)
                    match seguir:
                        case 1: 
                            vidas=vidas
                        case 2: 
                            print("Juego finalizado")
                            sys.exit()                     
                        case 3:
                            menu(vidas)
                            sys.exit()    
                        case _:
                            break
            else:
                print("\n" * 2)   
                print("*" * 25)        
                print(f"El numero ingresado es= {numero} \nEl numero que salio es= {numeroAleatorio} ")
                print("Lo siento! no adivinaste el numero, vulve a intentarlo")
                vidas=vidas -1
                print("Te quedan ", vidas, " vidas" )
        elif numero == "S"  or numero =="s":
            vidas=0
            break
        elif vidas == 0:
            print("Lo siento! no te quedan mas vidas! =( ) " )
            break
        else:
            print("\n" * 2)   
            print("*" * 25)      
            print("Debe elegir un numero entero entre 1 y 10, vuelve a intentarlo")
    print("\n*" * 5)
    print("Juego finalizado")       
def menu(vidas):
    print("******* DIVINA EL NUMERO ***********")
    aux = 1
    print("VIDASSSSS ", vidas)
    if vidas != 0:
        while aux != 0:
            nivel = input("Elige el nivel: \n1- Facil \n2- Medio \n3- Dificil \n4- Salir \n")
            if nivel.isdigit() == True:
                nivel = int(nivel)
                match nivel:
                    case 1:
                        vidas = 10
                        aleatorio(vidas)
                    case 2:
                        vidas = 7
                        aleatorio(vidas)
                    case 3:
                        vidas = 3
                        aleatorio(vidas)
                    case 4:
                        aux = 0
                        break
                    case _:
                        print("La opcion ingresada no es valida. Debe elegir algunas de las opciones")
            else:
                print("La opcion ingresada no es valida. Debe elegir algunas de las opciones")
        print("******* JUEGO FINALIZADO *********")


def main():
    menu(vidas=None)

if __name__== "__main__":
    main()