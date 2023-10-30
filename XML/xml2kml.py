# xml2kml.py
# # -*- coding: utf-8 -*-
""""
Uso de Xpath para obtener archivos kml a partir de Ruta

@version 1.1 30/Octubre/2023 
@author: Luis A. Fernandez Suarez
"""

import xml.etree.ElementTree as ET

xml_file = open("rutas.kml", "w") # Abre y borra el contenido del archivo

def verXPath(archivoXML, expresionXPath):
    """Función verXPath(archivoXML, expresionXPath)
    Visualiza por pantalla el nodo correspondiente de una expresión XPath de un archivo XML
        
    Version: 1.2 21/Octubre/2020
    Author: Juan Manuel Cueva Lovelle. Universidad de Oviedo
    """
    try:
        
        arbol = ET.parse(archivoXML)
        
    except IOError:
        print ('No se encuentra el archivo ', archivoXML)
        exit()
        
    except ET.ParseError:
        print("Error procesando en el archivo XML = ", archivoXML)
        exit()
       
    raiz = arbol.getroot()
    
    # Recorrido de los elementos del árbol
    for hijo in raiz.findall(expresionXPath): # Expresión XPath
        print("\nElemento = " , hijo.tag)
        if hijo.text != None:
            print("Contenido = ", hijo.text.strip('\n')) #strip() elimina los '\n' del string
        else:
            print("Contenido = ", hijo.text)    
        print("Atributos = ", hijo.attrib)

def write_in_file(line):
    """ Funcion que escribe la linea en el archivo y agrega un salto de linea"""
    file.write(line)
    file.write("\n")

def convert_XML_to_KML(archivo_XML):
    try:
        arbol = ET.parse(archivo_XML)

    except IOError:
        print("No se ha encontrado el archivo: ", archivo_XML)
        exit()
    
    except ET.ET.ParseError:
        print("Error procesando el archivo: ", archivo_XML)
        exit()

        # Obtener raiz del elemento
        raiz = arbol.getroot()
        
        # Cabezera xml kml
        write_in_file_kml_head()

        write_in_file('<Document>') # Abrir la etiqueta Documento
        write_in_file("<name> coordenadas de los amigos de la RS </name>")

        
        write_in_file_ruta(raiz) # procesado de la ruta


        write_in_file('</Document>')  # Cerrar la etiqueta Documento
        write_in_file('</kml>') # Cerrar la etiqueta <kml>


def write_in_file_kml_head():
    '''
    Incluye la cabecera del archivo kml:
        <?xml version="1.0" encoding="UTF-8"?>
        <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
    '''
    write_in_file('<?xml version="1.0" encoding="UTF-8"?>')
    write_in_file('<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">')

write_in_file_ruta(ruta):


def main():
    """Prueba de la función verXPath()"""
    
    print(verXPath.__doc__)
    
    XML_filename = "rutas.xml"
    convert_XML_to_KML(convert_XML_to_KML)

    archivo_XML.close()
    

if __name__ == "__main__":
    main()