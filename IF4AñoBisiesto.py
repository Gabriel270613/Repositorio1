print("=====PRACTICA 4 =====")
print("TE DIRE SI EL AÑO QUE PONES ES BISIESTO O NO")
año = int(input("Ingresa el año que quieres comprobar : ")) 

if año % 4 != 0: 
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0: 
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
	print("Es bisiesto")