import os

def calculardescuentos(cantidad , precio):
    if cantidad >=30 :
        print("Descuento especial")
        descuento = (cantidad * precio)*.2
        print(f"el descuento es de {descuento}")
    elif cantidad >= 10:
        print("Descuento normal")
        descuento = (cantidad * precio)*.1
        print(f"el descuento es de {descuento}")
    else :
        descuento = 0
        print("Gracias por pagar el precio completo")
    return descuento

def limpiarConsola():
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)



def menu():
    nombreFruta = ""
    print("""
    1.- manzanas
    2.- peras
    3.- guayabas
    4.- uvas
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
    else:
        print("Opcion no valida")

        
    return nombreFruta,opcion