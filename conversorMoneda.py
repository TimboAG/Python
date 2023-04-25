def convertir(valor_dolar):
    cantidad = float(input(f'Ingrese cantidad de Pesos Argentinos: '))

    dolares = cantidad / valor_dolar
    dolares = round(dolares, 2)
    print(f'Tienes ${dolares} Dolares')

def main():
    
    while True:
        menu = """
        1-Pesos Argentinos a Dolares 
        2-Pesos Argentinos a Euro 
        3-Pesos Argentinos a Reales
        4-Salir
        Ingrese una Opcion: """

        opcion = input(menu)

        if opcion == '1':
            convertir(220.88, 'Dolares')
        elif opcion == '2':
            convertir(242.33, 'Euro')
        elif opcion == '3':
            convertir(43.56, 'Reales')
        elif opcion == '4':
            print("Cerrando conversor de monedas ")
            break
        else:
            print("Opcion incorrecta !!!")
            print("Vuelve a ingresar la opción correcta")
    

if __name__ == '__main__':
    main()
