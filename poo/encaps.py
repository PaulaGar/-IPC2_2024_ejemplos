#ENCAPSULAMIENTO
class persona:
    def __init__(self, nombre,contrasenia):
        self.nombre = nombre
        self.__contrasenia= contrasenia # USAMOS EL DOBLE GUION BAJO "__" PARA DECLARAR UN ATRIBUTO PRIVADO

    def get_contrasenia(self):
        return self.__contrasenia
    
paula = persona("Paula","123")
print(paula.nombre)
#print(paula.__contrasenia) # ESTE CODIGO GENERA ERROR PORQUE CONTRASENIA ES UN ATRIBUTO PRIVADO
print(paula.get_contrasenia())