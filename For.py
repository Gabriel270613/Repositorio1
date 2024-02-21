numero1 = int(input("ingresa un numero1"))
numero2 = int(input("ingresa un numero2"))

rango = range(numero1, numero2)
for numero in rango:
    if numero %2==0:
        print(f"este numero es par {numero}")
    else:
        print(f"este numero es impar{numero}")

nombre ="Gabriel"
for letra in nombre:
    print(letra)