

class Persona():
    def __init__(self, nombre, apellido, edad):
        nombre = self.nombre
        apellido = self.apellido
        edad = self.edad

    def __str__(self):
        return("hola")



a = Persona("franco", "alberti", 15)

print(a.apellido)


