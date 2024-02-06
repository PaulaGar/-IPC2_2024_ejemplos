#Defenimos 3 funciones las cuales representaran las opciones que se ejecutaran en el menu
def camino_1():
    print("Entro al camino 1")

def camino_2():
    x = 7
    for i in range(x):
        aux = i
        temp=x-i
        while aux != 0:
            while temp > 0:    
                #Usamos la funcion end para evitar que se finalice el print con un salto de linea
                print(" ", end="")
                temp -=1 # Usando el -= podemos rester una unidad al la variable int (temp)
            print("*", end=" ") 
            aux-=1
        print("\n")#imprime un salto de linea

def camino_3():
    aux = ["Este","es","el","camino",3]
    print(aux)


while True: #Con el while true generamos un ciclo infinito
    print("+-+-+-+-+-+-+-+-+-+-+")
    print("1. Ir al primer camino")
    print("2. Imprimir piramide")
    print("3. Imprimir una lista")
    print("4. Salir")
    
    # La funcion "input" nos permite obtener un valor desde la consola y asignarlo a una variable
    selector = int(input("Seleccione la opcion: ")) 

    if selector == 1:
        camino_1()
    elif selector == 2:
        camino_2()
    elif selector == 3:
        camino_3()
    elif selector == 4:
        # Para poder salir del ciclo infinito podemos usar funciones como break
        break
    else: 
        print("Seleccione una opcion correcta :c") 
    print("+-+-+-+-+-+-+-+-+-+-+")

print("Programa finalizado")