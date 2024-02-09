import xml.etree.ElementTree as ET #Libreria para manejar XML

ruta ="entrada.xml"
print(ruta)
arbol = ET.parse(ruta) #parsear ruta || devolver contenido en listas de listas
ramas = arbol.getroot() #se obtiene la raiz | ruta padre
for i in ramas.iter('matriz'): #Recorrer la raiz hacia las ramas | .iter es para filtrar tags
    print(i.tag, i.attrib)
    for j in i.iter('dato'): #se puede dejar como solo i para obtener TODOS los hijos
        print(j.tag)
        print(j.get('x'))
        print(j.get('y'))
        #print(j.attrib)
        print(j.text)
    print("++++++++++++++++++++++++++++++++++++++++")
        
