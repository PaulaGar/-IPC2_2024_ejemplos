class SinAtributos:
    def __init__(self) -> None:
        pass
    

#DEFINICION DE UNA CLASE
class Carro:
    #DE ESTA MANERA SE DECLARAN LOS ATRIBUTOS DE UNA CLASE
    def __init__(self, nombre): #SE AGREGA EL ATRTIBUTO SELF YA QUE ASI DISTINGUIMOS QUE VARIABLES SERAN ATRIBUTOS DE LA CLASE
        self.color=""
        self.nombre=nombre
        

    def asignar_color(self,new_color): # TODOS LOS METODOS DEBEN TENER UN SELF PARA PODER ACCEDER A LOS ATRIBUTOS
        self.color= new_color

    def imprimir_colores(self):
        #EL SELF SE USA PARA HACER UN LLAMADO A LOS ATRIBUTOS DE UNA CLASE
        print("soy "+self.nombre)
        print("y mi color  es "+self.color)
        print("-----------------")
    
    #para no hacer nada :D
    def no_hace_nada(self):
        pass

#SE DECLARA UN OBJETO DE TIPO CARRO
car = Carro("Paula")
car.imprimir_colores()
car.asignar_color("blanco")
car.imprimir_colores()

car.no_hace_nada()