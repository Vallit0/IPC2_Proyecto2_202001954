from xml.dom import minidom
#from models.piso import Piso, listaPisos
#from models.nodes import designNode, designList
#from models.matrixNode import matrixNode, matrix
from typing import Tuple
import xml.dom.minidom
from xml.dom.minidom import parse, parseString
from models.headersList import Lista_Encabezado
from models.disperseMatrix import Lista_Encabezado, Nodo_Interno, MatrizDispersa
from models.city import listaCiudades
from models.drones import listaDrones

def fillMatrix(rows, columns, color, matrix, flip, swap) -> None:
    posX = 0
    posY = 0
    for i in range(rows):
        posY += 1
        posX = 0
        for j in range(columns):
            posX += 1
            matrix.append(color[j], posX, posY, flip, swap)

def analyzeXML(filename, listOfCities):
    rows: int = 0
    columns: int = 0
    flip: float = 0
    swap: float = 0
    patterns: list = []

    doc = minidom.parse(filename)
    cities = doc.getElementsByTagName("ciudad")
    row = 1
    rowPatterns = 1
    #listOfCities = listaCiudades()

    for city in cities:
        row += 1
        cityData = city.getElementsByTagName("nombre")[0]
        cityName = cityData.firstChild.data
        print("")
        print("----------CIUDAD " + str(cityData.firstChild.data) + '--------')
        print('Nombre Ciudad', cityName)
        name = cityName
        print("Rows ->", cityData.getAttribute("filas"))
        rows  = cityData.getAttribute("filas")
        print("Columns ->", cityData.getAttribute("columnas"))
        column = cityData.getAttribute("columnas")
        print("============ FILAS de Ciudad "+str(cityData.firstChild.data)+'=======')
        filas = city.getElementsByTagName('fila')

        matrix = MatrizDispersa()

        for i in range(len(filas)):
            #Crear una matriz
            print("")
            print("----------Fila"+str(rowPatterns)+'---------')
            print("Codigo >>" + filas[i].getAttribute('numero'))
            posY = filas[i].getAttribute('numero')
            print("Patron >>" + filas[i].firstChild.data)
            rowData = filas[i].firstChild.data
            posX = 0
            for node in rowData:
                if node == '*':
                    posX += 1
                    pass
                elif node == ' ':
                    #Crear Nuevo nodo
                    matrix.insert(posX, posY, 'T')
                    posX += 1
                    pass
                elif node.upper() == 'E':
                    #Crear Nodo con Punto de Entrada
                    matrix.insert(posX, posY, 'E')
                    posX += 1
                    pass
                elif node.upper() == 'R':
                    #Crear Nodo con Recursos
                    matrix.insert(posX, posY, 'R')
                    posX += 1
                    pass
                elif node.upper() == 'C':
                    #Crear Nodo con Unidad Civil
                    matrix.insert(posX, posY, 'C')
                    posX += 1
                    pass
                else:
                    print("Existe un Error en el archivo")
            rowPatterns += 1

        print('')
        #Anadir a la Matriz las Unidades Militares

        print("============ UNIDADES militares " + str(cityData.firstChild.data) + '=======')
        unidades = city.getElementsByTagName('unidadMilitar')
        rowUnits = 0
        for i in range(len(unidades)):
            print("")
            print("----------Unidad Militar" + str(rowUnits) + '---------')
            print("Fila >>" + unidades[i].getAttribute('fila'))
            posY = unidades[i].getAttribute('fila')
            print("Columna >>" + unidades[i].getAttribute('columna'))
            posX = unidades[i].getAttribute('columna')
            print("Poder >>" + unidades[i].firstChild.data)
            power = unidades[i].firstChild.data
            rowUnits += 1
            matrix.addUnitNode(posX, posY, power)
            #getNode and then change the characteristics

        listOfCities.append(name,rows,columns,row)
    robots = doc.getElementsByTagName("robot")
    drones = listaDrones()
    for robot in robots:
        print("============= "+str(robot.firstChild.data)+" ================")
        print("tipo de dron>>", robot.getAttribute('tipo'))
        print("poder>>", robot.getAttribute('capacidad'))
        drones.append(str(robot.firstChild.data), robot.getAttribute('tipo'),robot.getAttribute('capacidad') )

    listOfCities.addDrones(drones)



    return listOfCities



