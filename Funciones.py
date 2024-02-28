#contexto Global
nombre = " Gabriel"
def mostrarUsuario(NombreFuncion):
    print(NombreFuncion)
    print("hola mundo")
#Contesxto Local
def noUsuario(NombreFuncion):
    print(NombreFuncion)
    print("Adios mundo mundo")
    mostrarUsuario(NombreFuncion)
    
    
mostrarUsuario(nombre)
noUsuario(nombre)