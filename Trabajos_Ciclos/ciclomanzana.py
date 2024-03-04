descuento= 0
precioManzana = 10
CantidadManzana =float(input("Cuantas manzanas quieres?"))

while CantidadManzana !=0 :
    
    
    descuento = (CantidadManzana * precioManzana) * .1
    descuentoSecreto = (CantidadManzana * precioManzana) * .2
    if(CantidadManzana >=30 ):
        print("Descuento secreto Aplicado")
        print(f"Total: {(precioManzana * CantidadManzana)- descuentoSecreto}")
    elif(CantidadManzana >=10):
        print("Aplica descuento del 10% y el precio es: ")
        print(f"Total: {(precioManzana * CantidadManzana)- descuento}")
    else :
        print("No hay descuento")
        print(f"Total a pagar: $3{precioManzana*CantidadManzana}")
    CantidadManzana =float(input("Cuantas manzanas quieres?"))
    