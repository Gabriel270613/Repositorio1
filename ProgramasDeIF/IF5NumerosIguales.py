print("=====Practica 5 =====")

num1 = int(input("""Dame tu primer numero : """))
num2 = int(input("""Dame tu segundo numero : """))
num3 = int(input("""Dame tu tercer numero : """))

if num1 == num2 == num3 :
    print("LOS TRES NUMEROS SON IGUALES")
elif ((num1 == num2) or (num1 == num3) or (num2 == num3)) :
    print("DOS DE TUS NUMEROS SON IGUALES")
else :
    print("NO TIENES NUMEROS IGUALES")