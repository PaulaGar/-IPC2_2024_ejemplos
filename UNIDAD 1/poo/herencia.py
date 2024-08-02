#HERENCIA
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def descripcion(self):
        print("soy un animal de la especie "+self.especie +" y tengo la edad de "+str(self.edad))

class Perro (Animal): #LA CLASE PERRO ES HIJA DE LA CLASE ANIMAL
    def __init__(self, especie, edad,dueño):
        super().__init__(especie, edad) # POR LO TANTO HEREDA LOS ATRIBUTOS DE LA PLASE PADRE
        self.dueño = dueño #ESTE SERIA UN ATRIBUTO PROPIO DE ESTA CLASE
    
    def obtener_dueño(self):
        print("El dueño de este perro es "+ self.dueño)


mi_perro = Perro("mamifero",6,"Carlos")
mi_perro.descripcion()
mi_perro.obtener_dueño()#COMO HEREDA DE LA CLASE ANIMAL PODEMOS USAR SUS FUNCIONES Y ATRIBUTOS

#OJO! una clase padre no puede acceder a las funciones de la clase hija
mi_animal= Animal("leon",10)
mi_animal.obtener_dueño()