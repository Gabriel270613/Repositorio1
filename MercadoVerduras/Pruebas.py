opcion = 1

def menu():
    nombreFruta = ""
    print("""
    1.- manzanas
    2.- peras
    3.- guayabas
    4.- uvas
    5.- fresas
    0.- salir
    """)
    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
        nombreFruta = 'Manzanas'
    elif opcion == 2:
        nombreFruta = 'Peras'
    elif opcion == 3:
        nombreFruta = 'Guayabas'
    elif opcion == 4:
        nombreFruta = 'Uvas'
    elif opcion == 5:
        nombreFruta = 'Fresas'
    else:
        print("Opcion no valida")
    return nombreFruta, opcion


