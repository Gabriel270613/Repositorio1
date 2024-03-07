nombre = "gabriel"
print(nombre.upper().center(100,"x"))

nombre = "GABRIEL"
print(nombre.lower())
print(len(nombre))
print(reversed(nombre))
for letter in nombre :
    print(letter)
    
if 'a' in nombre.lower():
    print("si esta letra es a")
    
print(nombre[0])
print(nombre[::-1])