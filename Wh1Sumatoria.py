print("=====While practica 1 =====")
suma = 0
numero = int(input("ingresa un valor del teclado (coloca 0 para finalizar): "))
while True:
    if numero >= 1 :
        print(f"Agregaste el nuemero {numero} a la suma")
        suma += numero 
    elif numero == 0 :
        print(f"LA SUMA DE LOS VALORES AGREGADOS ES = {sumatotal}")
        break
    numero = int(input("ingresa un valor del teclado (coloca 0 para finalizar): "))
    sumatotal = suma  