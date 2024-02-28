print("=====While practica 1 =====")
suma = 0
numero = int(input("ingresa un valor del teclado (coloca 0 para finalizar): "))
<<<<<<< HEAD
while numero != 0:
    if numero == 0 :
        sumatotal= suma
        print(f"LA SUMA DE LOS VALORES AGREGADOS ES = {sumatotal}")  
    else :
        print(f"Agregaste el nuemero {numero} a la suma")
        suma += numero     
    numero = int(input("ingresa un valor del teclado (coloca 0 para finalizar): "))
=======
while True:
    if numero >= 1 :
        print(f"Agregaste el nuemero {numero} a la suma")
        suma += numero 
    elif numero == 0 :
        print(f"LA SUMA DE LOS VALORES AGREGADOS ES = {sumatotal}")
        break
    numero = int(input("ingresa un valor del teclado (coloca 0 para finalizar): "))
    sumatotal = suma  
>>>>>>> a48e0b28e7572b2140a99f3e9013d6f61525885c
