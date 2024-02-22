class nodo:
    def __init__(self,variable,numero,siguiente=None) -> None:
        self.nombre= variable
        self.edad=numero
        self.siguiente=siguiente

class listaS:
    def __init__(self,inicio=None,size=0) -> None:
        self.inicio=inicio
        self.size=size

    def agregar(self,nombre,edad):
        nuevo=nodo(nombre,edad)

        if self.size==0:
            self.inicio=nuevo
            self.size+=1
        else:
            aux=self.inicio

            while aux.siguiente!=None:
                aux=aux.siguiente


            aux.siguiente=nuevo
            self.size+=1
  