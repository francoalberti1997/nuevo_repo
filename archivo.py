

class Familia():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido  
        self.parentesco = True
    
    def familiar (self):
        if self.parentesco:
            return("es amigo")


victor = Familia("victor", "ortiz")

leo = Familia("leo", "ortiz")


print(victor.familiar())