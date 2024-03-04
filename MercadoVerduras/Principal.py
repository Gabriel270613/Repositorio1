import FuncionesVerduras
import time

total = 0
cantidadProducto = 1




while cantidadProducto != 0:
    
    print("Hola buenas tardes")
    
    FuncionesVerduras.limpiarConsola()
    
    fruta, opcion = FuncionesVerduras.menu()
    if opcion == 0:
        break
    # PARTE 1
    # PEDIR DATOS
    cantidadProducto = float(input(f"Dime la cantidad de {fruta} vendidas: "))
    if cantidadProducto == 0:
        break
    precioProducto = float(input(f"Dime el precio de la {fruta}: "))
    
    total = cantidadProducto * precioProducto
    # PARTE 2
    # CALCULAR DESCUENTO
    descuento=FuncionesVerduras.calculardescuentos(cantidadProducto,precioProducto)
    total = total - descuento
    # PARTE 3
    # MOSTRAR RESULTADOS
    print(f"Total: {total}" )
    time.sleep(5)

