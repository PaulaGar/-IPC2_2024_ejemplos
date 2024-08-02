#ASI SE HACEN LOS COMENTARIOS EN PYTHON

#VARIABLES Y EXPRESIONES DE SENTENCIA ----------------------------
numero = 2
char = '2'
texto = "Hola"
lista = [1,2,3,4,5]
operacion = 5*(numero+1)
#operacion = 2
Nulo = None
#Null 

print(str(numero)+char) #concatenar
print(numero+int(char)) #operar
print( operacion*char)
print(type(lista))
print(lista)

# EJECUCION CONDICIONAL --------------------------------

#los if entran con TRUE
if not False:
    print("Entro al IF")

#comparaciones relacionales 
if numero > operacion:
    print("numero es mayor que e")
elif numero== operacion:
    print ("numero es igual a e")
else:
    print("numero es menor que e")

#existe o no existe un valor 
if Nulo:
    print("El valor de nulo no existe en este punto")
Nulo = 12
if Nulo:
    print("El valor de nulo  existe")

# FUNCIONES -----------------------------------------

#declarar funciones
def funcion1():
    texto_f1="esta es la funcion numero 1"
    print(texto_f1)

#declarar funcion con parametro
def funcion2(aux):
    print(aux)

funcion1()

#no se puede usar variables no declaradas dentro del mismo contexto

texto_f2 = "esta es la funcion numero 2"
funcion2(texto_f2) 

#LLAMADO DE FUNCIONES DE OTROS ARCHIVOS
import afuera
#procedimiento
afuera.funcion3(5)
#funcion
print(afuera.func_retorno())

#ITERACIONES

aux1 = 0

while aux1 <5:
    print(aux1)
    aux1 +=1

for i in lista:
    print(i)
    
print("-----------")
for j in texto[2:4]:
    print(j)

print("-----------")
for k in range(8):
    print(k)

