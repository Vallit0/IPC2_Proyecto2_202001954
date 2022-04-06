from xml.dom import minidom
from colorama import Fore, Style, Back, init
init(convert=True)

from models.disperseMatrix import Lista_Encabezado, Nodo_Interno, MatrizDispersa
from models.city import listaCiudades
from models.drones import droneList
from models.militaryUnits import militaryUnits

def fillMatrix(rows, columns, color, matrix, flip, swap) -> None:
    posX = 0
    posY = 0
    for i in range(rows):
        posY += 1
        posX = 0
        for j in range(columns):
            posX += 1
            matrix.append(color[j], posX, posY, flip, swap)

def analyzeXML(filename, listOfCities: listaCiudades):
    rows: int = 0
    columns: int = 0
    flip: float = 0
    swap: float = 0
    patterns: list = []

    doc = minidom.parse(filename)
    cities = doc.getElementsByTagName("ciudad")
    row = 1
    rowPatterns = 1
    listOfCities = listaCiudades()

    for city in cities:
        row += 1
        cityData = city.getElementsByTagName("nombre")[0]
        cityName = cityData.firstChild.data
        print(Style.RESET_ALL)
        print("")
        print("----------CIUDAD " + str(cityData.firstChild.data) + '--------')
        print('Nombre Ciudad', cityName)
        name = cityName
        print("Rows ->", cityData.getAttribute("filas"))
        rows  = cityData.getAttribute("filas")
        print("Columns ->", cityData.getAttribute("columnas"))
        column = cityData.getAttribute("columnas")


        filas = city.getElementsByTagName('fila')
        matrix: MatrizDispersa

        matrix = MatrizDispersa(row)
        print(Fore.MAGENTA)
        print("============ UNIDADES militares " + str(cityData.firstChild.data) + '=======')
        units = militaryUnits()
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
            units.append(int(posY), int(posX), float(power))
            #matrix.insert(int(posY), int(posX), 'M', float(power))
        #matrix.print()
        #n = 1
        #matrix.graphWithTable('name' + str(n))
        # += 1
        print("")
        #print("======= Lista de Unidades === ")
        #units.print()
        print(Fore.CYAN)
        print("============ FILAS de Ciudad " + str(cityData.firstChild.data) + '=======')
        for i in range(len(filas)):
            #Crear una matriz
            print("")
            print("----------Fila"+str(rowPatterns)+'---------')
            print("Codigo >>" + filas[i].getAttribute('numero'))
            posY = filas[i].getAttribute('numero')
            print("Patron >>" + filas[i].firstChild.data)
            rowData = filas[i].firstChild.data
            posX = 1
            for node in rowData:
                testUnit = units.search(posY, posX)
                #print(testUnit)
                if node == '*':
                    if testUnit == False:
                        matrix.insert(posY, posX, '*', None)
                        posX += 1
                    else:
                        matrix.insert(posY, posX, 'M', testUnit.power)
                        posX += 1
                    pass
                elif node == ' ':
                    #Crear Nuevo nodo
                    if testUnit == False:
                        matrix.insert(posY, posX, 'T', None)
                        posX += 1
                    else:
                        matrix.insert(posY, posX, 'M', testUnit.power)
                        posX += 1
                    pass
                elif node.upper() == 'E':
                    #Crear Nodo con Punto de Entrada
                    if testUnit == False:
                        matrix.insert(posY, posX, 'E', None)
                        posX += 1
                    else:
                        matrix.insert(posY, posX, 'M', testUnit.power)
                        posX += 1
                    pass
                elif node.upper() == 'R':
                    #Crear Nodo con Recursos
                    if testUnit == False:
                        matrix.insert(posY, posX, 'R', None)
                        posX += 1
                    else:
                        matrix.insert(posY, posX, 'M', testUnit.power)
                        posX += 1
                    pass
                elif node.upper() == 'C':
                    #Crear Nodo con Unidad Civil
                    if testUnit == False:
                        matrix.insert(posY, posX, 'C', None)
                        posX += 1
                    else:
                        matrix.insert(posY, posX, 'M', testUnit.power)
                        posX += 1
                    pass
                elif node == '"':
                    pass
                else:
                    print("Existe un Error en el archivo")
                    matrix.graficarDot('Matriz1')
                    posX += 1
            rowPatterns += 1

        print(Style.RESET_ALL)


        #print('TERMINO lectura de FILAS')
        #print("Primera Matrix con solo FILAS")
        #matrix.print()
        #print("GRAFICA COMPLETA")
        matrix.print()
        #matrix.graphWithTable('Grafiz'+str(row))
        #matrix.graficarDot('Grafica11')
        #Anadir a la Matriz las Unidades Militares


        #matrix.graficarDot('ANADIR UNIDADES')
        listOfCities.append(matrix, name,rows,column,row)

    #Media vez se logra la lectura de las matrices, hay que crear la lectura de los drones
    robots = doc.getElementsByTagName("robot")

    drones = droneList()
    print("")
    for robot in robots:

        print()
        print("")
        droneName = robot.getElementsByTagName("nombre")[0]
        print("============= "+str(droneName.firstChild.data)+" ================")
        print("Tipo de dron>>", droneName.getAttribute('tipo'))
        tipo = droneName.getAttribute('tipo')
        if tipo.replace(" ", "").upper() == 'CHAPINFIGHTER':
            tipo = tipo.replace(" ", "").upper()
            power = droneName.getAttribute('capacidad')
            print("Poder>>", droneName.getAttribute('capacidad'))
            drones.append(droneName.firstChild.data, tipo,power)
        elif tipo.replace(" ","").upper() == 'CHAPINRESCUE':
            tipo = tipo.replace(" ","").upper()
            print("Unidad de Rescate")
            drones.append(droneName.firstChild.data, tipo,0)

        drones.print()


    listOfCities.addDrones(drones)



    return listOfCities



