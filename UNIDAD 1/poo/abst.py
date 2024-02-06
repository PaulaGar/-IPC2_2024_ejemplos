#ABSTRACCION
from abc import ABC, abstractmethod # LIBRERIA ESPECIFICAMENTE PARA PERMITIR LA ABSTRACCION

class Animal(ABC):# LA ABTRACCION PODRIA CONSIDERARSE UNA PLANTILLA
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
        super().__init__() #Herencia de ABC para poder usar metodos abstractos

    @abstractmethod 
    def hablar(self):#ESTE ES UN METODO ABSTRACTO Y OBLIGA A IMPLEMENTARLO A LOS HIJO
        pass

class Perro (Animal):
    def __init__(self, especie, edad,):
        super().__init__(especie, edad) 

    #OBLIGATORIAMENMTE HAY QUE AGREGARLO SI NO EL PROGRAMA LO CONSIDERARA COMO CODIGO INCOMPLETO Y DARA ERROR
    def hablar(self): 
        print("Guau! Guau!")

class gato (Animal):
    def __init__(self, especie, edad,):
        super().__init__(especie, edad) 

    #OBLIGATORIAMENMTE HAY QUE AGREGARLO SI NO EL PROGRAMA LO CONSIDERARA COMO CODIGO INCOMPLETO Y DARA ERROR
    def hablar(self): 
        miau="miau "
        for i in range (4):
           miau=miau+miau
           print(miau)


mi_perro = Perro("mamifero",6)
mi_gato = gato("mamifero",6)
mi_gato.hablar()
mi_perro.hablar()