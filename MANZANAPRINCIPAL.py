descuento = 0
total = 0
cantidadManzana = 1

print("Hola buenas tardes")

while cantidadManzana != 0:
    # PARTE 1
    # PEDIR DATOS
    cantidadManzana = float(input('Dime la cantidad de manzanas vendidas: '))
    if cantidadManzana == 0:
        break
    precioManzana = float(input('Dime el precio de la manzana: '))
    
    total = cantidadManzana * precioManzana
    # PARTE 2
    # CALCULAR DESCUENTO
    if cantidadManzana ==30 :
        print("Descuento especial")
        descuento = (cantidadManzana * precioManzana)*.2
        print(f"el descuento es de {descuento}")
        total = total - descuento
    elif cantidadManzana >= 10:
        print("Descuento normal")
        descuento = (cantidadManzana * precioManzana)*.1
        print(f"el descuento es de {descuento}")
        total = total - descuento
    else :
        print("Gracias por pagar el precio completo")
    # PARTE 3
    # MOSTRAR RESULTADOS
    print(f"Total: {total}" )



