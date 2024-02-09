import xml.etree.ElementTree as ET #LIBRERIA PARA TRABAJAR XML

#EMBELLECER XML IDENTAR OBLIGATORIO COMENTAR de ser utilizado 
def indent(elem, level=0, hor='\t', ver='\n'):
    i = ver + level * hor
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + hor
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1, hor, ver)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

#---------------------------------------------------------------------------------------------
ruta = "salida.xml" #definir ruta de salida
#creamos la raiz
NewXml = ET.Element('matrices') 
#se agregan los subelementos/ramas/hijos
ET.SubElement(NewXml,"valor").text="Valor inicial" 
ET.SubElement(NewXml,"valor2",Atributo1="3").text="Valor inicial numero 2" #el contenido debe ser string siempre
# ** las hojas son las unicas que pueden tener valor
con=0
#creamos rama matriz 
Matri = ET.SubElement(NewXml,"matriz")
contador=1
while contador < 10:
    ET.SubElement(Matri,"dato",x=str(con),y=str(5)).text=str(contador)
    con+=1
    contador+=1

#generar el contenido del archivo de salida
salida = ET.ElementTree(NewXml) #se mete la raíz
ET.dump(NewXml)
indent(NewXml)
salida.write(ruta) #escribir el archivo