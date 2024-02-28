contador = 0
numero = int(input("ingresa un numero: "))

while numero < 0 or numero >= 20 :
    print("el numero no se encuentra en el rango (0,20), ingresa otro numero valido")
    numero = int(input("ingresa un numero: "))
    contador += 1
print(f"numero de intentos: {contador}")
