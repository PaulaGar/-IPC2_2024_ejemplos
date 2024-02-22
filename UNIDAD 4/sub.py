#sub lista de anidada
#creamos la clase para el nodo
class nodo:
    def __init__(self, nombre, estado, siguiente=None) -> None:
        self.nombre =   nombre
        self.estado =   estado
        self.siguiente= siguiente

#creamos la clase para la lista
class lista:
    def __init__(self,inicio=None, size=0) -> None:
        self.inicio = inicio
        self.size= size

    def agregar(self, nombre, estado):
        #Creamos el nuevo objeto nodo
        nuevo = nodo(nombre,estado)

        #comprobamos si la lista está vacía
        if self.size==0:
            #el nuevo nodo sera el inicial y le sumamos al tamaño de la lista
            self.inicio=nuevo
            self.size+=1
        else:
            #creamos un nodo auxiliar
            aux=self.inicio
            #buscamos el final de la lista || None es igual a nulo, pero nulo no existe en python
            while aux.siguiente!=None:
                aux=aux.siguiente
            #el apuntador siguiente del ultimo apunta al nuevo nodo y se suma al tamaño
            aux.siguiente=nuevo
            self.size=self.size+1

    def imprimir(self):
        if self.inicio==None:
            print("historial vacio")
            return
        auxiliar=self.inicio
        while True:
            print(str(auxiliar.nombre)+auxiliar.estado, end="=>")
            auxiliar=auxiliar.siguiente
            if auxiliar==None:
                break

#Crear un objeto lista
estudiante=lista()

#declarar variables útiles
name=""
state=""
decidir=""
#Ciclo para el menú
while True:
    name=input("Ingrese el nombre del estudiante \n")
    state=input("Ingrese el estado del curso \n")
    estudiante.agregar(name,state)
    estudiante.imprimir()
    print("\n")
    decidir = input("desea agregar otro usuario? y/cualquier tecla para terminar \n") #\n es para hacer un salto de linea en consola
    if decidir=="y":
        pass
    else:
        break
