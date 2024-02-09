from xml.dom import minidom #Libreria DOM

archivo_xml = "entrada.xml" #ruta del archivo a leer
doc = minidom.parse(archivo_xml) #parsear| convertir en arbol tipo DOM

for i in doc.getElementsByTagName("matrices"):
    print(i.tagName)
    for j in i.getElementsByTagName("matriz"):
        print(j.tagName)
        for k in j.getElementsByTagName("dato"): #se debe especificar siempre
            print(k.getAttribute("x"),"x",k.firstChild.nodeValue)