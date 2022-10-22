

class Persona():
    def __init__(self, nombre, apellido, edad):
        
        self.__nombre = nombre
        self.edad = edad
        self.apellido = apellido

    def __str__(self):
        return("hola")



a = Persona("franco", "alberti", 15)

print(a.apellido)
