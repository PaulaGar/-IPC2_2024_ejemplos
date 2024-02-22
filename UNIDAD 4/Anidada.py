import sub

#creamos la clase para el nodo
class nodoA:
    def __init__(self, nombre, lista, siguiente=None) -> None:
        self.nombre =   nombre
        self.lista =   lista
        self.siguiente= siguiente

#creamos la clase para la lista
class listaA:
    def __init__(self,inicio=None, size=0) -> None:
        self.inicio = inicio
        self.size= size

    def agregar(self, nombre, lista):
        #Creamos el nuevo objeto nodo
        nuevo = nodoA(nombre,lista)

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
            print("---"+str(auxiliar.nombre), end="=>")
            #auxiliar
            auxiliar2=auxiliar.lista.inicio 
            while True:
                print("\n") 
                print(str(auxiliar2.nombre)+str(auxiliar2.estado),end="=>")
                auxiliar2=auxiliar2.siguiente
                if auxiliar2==None:
                    break
            print("\n") 
            auxiliar=auxiliar.siguiente
            if auxiliar==None:
                break  


#Crear un objeto lista
estudiante=listaA()
cursos=sub.lista()
cursos2=sub.lista()

#declarar variables útiles
name=""
state=""
decidir=""
#agregar
cursos.agregar("matematicas"," aprobado")
cursos.agregar("ciencias"," aprobado")
cursos.agregar("historia"," reprobado")
cursos2.agregar("matematicas"," reprobado")
cursos2.agregar("ciencias"," pendiente")
cursos2.agregar("historia"," reprobado")
estudiante.agregar("paula",cursos)
estudiante.agregar("José",cursos2)
estudiante.imprimir()