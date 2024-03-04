print("HOLA DAME DOS NUEMROS Y TE DIRE SI ES MENOR O MENOR")
numero1 = int(input("Dame tu primer numero = "))
numero2 = int(input("Dame tu segundo numero = "))

if numero1 == numero2 :
    print("Los dos numeros son iguales")
elif numero1 < numero2 :
    print(f"El numero {numero2} es mayor que {numero1}")
elif numero1 > numero2 :
    print(f"El numero {numero1} es mayor que {numero2}")