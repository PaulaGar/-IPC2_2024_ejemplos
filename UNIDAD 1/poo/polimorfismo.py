#POLIMORFISMO
from abc import ABC, abstractmethod 

class Animal(ABC):
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
        super().__init__()

    @abstractmethod 
    def hablar(self):
        pass

class Perro (Animal):
    def __init__(self, especie, edad,):
        super().__init__(especie, edad) 

    def hablar(self): 
        print("Guau! Guau!")

class Gato (Animal):
    def __init__(self, especie, edad,):
        super().__init__(especie, edad) 

    def hablar(self): 
        print("MIAUUUU")

mi_perro = Perro("mamifero",6)
mi_perro.hablar()
mi_gato = Gato("mamifero",6)
mi_gato.hablar() #A PESAR QUE SON DOS FUNCIONES QUE SE LLAMAN IGUAL SU RESULTADO ES DISTINTO YA QUE DEPENDEN DEL CONTEXTO