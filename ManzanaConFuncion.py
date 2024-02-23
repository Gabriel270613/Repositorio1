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

def pedirValores(nombreFruta):
    precio = float(input(f'Dime el precio de la {nombreFruta}: '))
    cantidad = float(input(f'Dime la cantidad de {nombreFruta} vendidas: '))
    return precio, cantidad

def calcularDescuento(cantidad,precio,descuentoEspecial):
    descuento = 0
    if cantidad == descuentoEspecial :
        print("Descuento especial")
        descuento = (cantidad * precio)*.2
        print(f"el descuento es de {descuento}")
        total = (cantidad * precio) - descuento
    elif cantidad >= 10:
        print("Descuento normal")
        descuento = (cantidad * precio)*.1
        print(f"el descuento es de {descuento}")
        total = (cantidad * precio) - descuento
    else :
        print("Gracias por pagar el precio completo")
    return total

while opcion != 0:
    nombreFruta, opcion = menu()
    if opcion == 0:
        break
    print("Hola buenas tardes")
    precio, cantidad = pedirValores(nombreFruta)
    total = calcularDescuento(cantidad,precio,30)
    print(f"Total: {total}" )