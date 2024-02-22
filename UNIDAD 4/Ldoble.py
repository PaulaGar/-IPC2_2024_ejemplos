#creamos la clase para el nodo
class nodo:
    def __init__(self, nombre, estado, siguiente=None, anterior=None) -> None:
        self.nombre =   nombre
        self.estado =   estado
        self.siguiente= siguiente
        self.anterior=anterior

#creamos la clase para la lista
class lista:
    def __init__(self,inicio=None,fin=None, size=0) -> None:
        self.inicio = inicio
        self.fin = fin
        self.size= size

    def agregar(self, nombre, estado):
        #Creamos el nuevo objeto nodo
        nuevo = nodo(nombre,estado)

        #comprobamos si la lista está vacía
        if self.size==0:
            #el nuevo nodo sera el inicial y le sumamos al tamaño de la lista
            self.inicio=nuevo
            self.fin=nuevo
            self.size+=1
        else:
            #creamos un nodo auxiliar
            aux=self.inicio
            #buscamos el final de la lista || None es igual a nulo, pero nulo no existe en python
            while aux.siguiente!=None:
                aux=aux.siguiente
            #el apuntador siguiente del ultimo apunta al nuevo nodo y se suma al tamaño
            aux.siguiente=nuevo
            #El apuntador del nuevo nodo al final de la lista apunta al nodo auxiliar
            nuevo.anterior=aux
            self.fin=nuevo
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
                
    def reves(self):
        if self.inicio==None:
            print("historial vacio")
            return
        auxiliar=self.fin
        while True:
            print(str(auxiliar.nombre)+auxiliar.estado, end="=>")
            auxiliar=auxiliar.anterior
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
    print("\nal reves:")
    estudiante.reves()
    print("\n")
    
