print("=====While practica 1 =====")
suma = 0
numero = int(input("ingresa un valor del teclado (coloca 0 para finalizar): "))
while numero != 0:
    if numero == 0 :
        sumatotal= suma
        print(f"LA SUMA DE LOS VALORES AGREGADOS ES = {sumatotal}")  
    else :
        print(f"Agregaste el nuemero {numero} a la suma")
        suma += numero     
    numero = int(input("ingresa un valor del teclado (coloca 0 para finalizar): "))