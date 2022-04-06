from os import system, startfile
#from models.piso import Piso, listaPisos
from colorama import *
from models.city import listaCiudades, City
from models.disperseMatrix import Nodo_Interno, MatrizDispersa
from functions import isPath, isPathExtreme


def rescueMissions(city):
    chooseDrone = True
    chooseUnit = True
    chooseEntrance = True
    rescueUnit = False
    entranceUnit = False
    map = city.matrix
    print("------------------MISIONES DE RESCATE -----------------------------------------------------------")
    print("============= Acciones de Ciudad " + str(city.name) + " =================================")

    print("| Dimensiones (Filas X Columnas) >>>" + str(city.rows) + 'x' + str(city.columns))
    print("")
    print(Style.RESET_ALL)
    while chooseDrone == True:
        print("--------------- ESCOJA UN DRON --------------")
        print("|", end="")
        city.drones.printRescue()
        print("|")
        #city.drones.printIndex()
        rescueDrone = input("Ingrese el Numero >> ")
        droneList = city.drones
        if droneList.searchByIndex(int(rescueDrone)) == False:
            print("NO SE HA ENCONTRADO EL DRON")

        else:
            print("-------------------------")
            print("Se ha encontrado el dron")
            print("-------------------------")

            print("")
            print("=========================")
            print("| Se ha escogido " + str(droneList.searchByIndex(rescueDrone).name), end="")
            print("|")
            print("=========================")
            print("")
            print("---------------- MISION DE RESCATE -----------------")
            while chooseUnit == True:
                print("------ UNIDAD QUE DESEA RESCATAR -----")
                print("Dron en uso>> " + str(droneList.searchByIndex(rescueDrone).name))
                print("Ciudad en uso>> " + str(city.name))
                print("+++POTENCIALES UNIDADES CIVILES++")
                map: MatrizDispersa
                map = city.matrix
                print("----- Escoja la Unidad Civil ----- ")
                map.printCivilUnits()
                civilUnitData = input(">>")
                #Se establece el punto Salida
                if map.searchByIndexType(int(civilUnitData), 'C') != False:
                    rescueUnit: Nodo_Interno
                    rescueUnit = map.searchByIndexType(int(civilUnitData), 'C')
                    chooseUnit = False
                else:
                    print("No se ha seleccionado ninguna unidad")

            while chooseEntrance == True:
                print("------ POTENCIALES ENTRADAS -----")

                print("Dron en uso>> " + str(droneList.searchByIndex(rescueDrone).name))
                print("Ciudad en uso>> " + str(city.name))
                print("Unidad Recurso >> " + str(rescueUnit.CivilUnitIndex) + ' X: ' + str(rescueUnit.coordenadaX) + ' Y: ' + str(rescueUnit.coordenadaY))
                print("+++POTENCIALES ENTRADAS ++")
                map: MatrizDispersa
                map = city.matrix
                print("----- Escoja la ENTRADA ----- ")
                map.searchEntranceUnits()
                map.printEntranceUnits()
                entranceUnitData = input(">>")
                #Se establece el punto Salida
                if map.searchByIndexTypeE(int(entranceUnitData), 'E') != False:
                    entranceUnit: Nodo_Interno
                    entranceUnit = map.searchByIndexTypeE(int(entranceUnitData), 'E')
                    chooseEntrance = False
                else:
                    print("No se ha seleccionado ninguna unidad")


            #Ya tenemos la entrada y la salida
            #Debe entrar, (ENTRADA, SALIDA, DRON a UTILIZAR)
            #map.findRescuePath()
            print("===================================")
            print("| Configuraciones Iniciales        |")
            print("-----------------------------------")
            print("Dron en uso>> " + str(droneList.searchByIndex(rescueDrone).name))
            print("Ciudad en uso>> " + str(city.name))
            print("Unidad Recurso >> " + str(rescueUnit.CivilUnitIndex) + ' X: ' + str(rescueUnit.coordenadaX) + ' Y: ' + str(rescueUnit.coordenadaY))
            print("Entrada >> " + str(entranceUnit.entranceUnitIndex) + ' X: ' +str(entranceUnit.coordenadaX) + ' Y: ' + str(entranceUnit.coordenadaY))
            print("------------------------------------")
            print("====================================")
            print('************************************')
            print("Calculando Path Finder")
            isPath(map, entranceUnit, rescueUnit)

            print("Desea Salir?[1 para Si, 0 para No")
            entrada = input(">>")
            if entrada == '1':
                chooseDrone = False
            elif entrada == '0':
                pass




    pass
def extractionMissions(city):
    chooseDrone = True
    chooseUnit = True
    chooseEntrance = True
    fightUnit = False
    entranUnit = False
    map = city.matrix
    print("------------------MISIONES DE COMBATE -----------------------------------------------------------")
    print("============= Acciones de Ciudad " + str(city.name) + " =================================")

    print("| Dimensiones (Filas X Columnas) >>>" + str(city.rows) + 'x' + str(city.columns))
    print("")
    print(Style.RESET_ALL)
    while chooseDrone == True:
        print("--------------- ESCOJA UN DRON --------------")
        print("|", end="")
        city.drones.printFighter()
        print("|")
        # city.drones.printIndex()
        rescueDrone = input("Ingrese el Numero >> ")
        droneList = city.drones
        if droneList.searchByIndex(int(rescueDrone)) == False:
            print("NO SE HA ENCONTRADO EL DRON")

        else:
            print("-------------------------")
            print("Se ha encontrado el dron")
            print("-------------------------")

            print("")
            print("=========================")
            print("| Se ha escogido " + str(droneList.searchByIndex(rescueDrone).name), end="")
            print("|")
            print("=========================")
            print("")
            print("---------------- MISION DE COMBATE -----------------")
            while chooseUnit == True:
                print("------ UNIDAD QUE DESEA RESCATAR (RECURSO) -----")
                print("Dron en uso>> " + str(droneList.searchByIndex(rescueDrone).name))
                print("Ciudad en uso>> " + str(city.name))
                print("+++POTENCIALES UNIDADES DE RECURSOS++")
                map: MatrizDispersa
                map = city.matrix
                print("----- Escoja la Unidad Recursos ----- ")
                map.printResourceUnits()
                resourceUnitData = input(">>")
                # Se establece el punto Salida
                if map.searchByIndexTypeR(int(resourceUnitData), 'R') != False:
                    rescueUnitR: Nodo_Interno
                    rescueUnitR = map.searchByIndexTypeR(int(resourceUnitData), 'R')
                    chooseUnit = False
                else:
                    print("No se ha seleccionado ninguna unidad")

            while chooseEntrance == True:
                print("------ POTENCIALES ENTRADAS -----")

                print("Dron en uso>> " + str(droneList.searchByIndex(rescueDrone).name))
                print("Ciudad en uso>> " + str(city.name))
                print("Unidad Recursos >> " + str(rescueUnitR.resourceUnit) + ' X: ' + str(
                    rescueUnitR.coordenadaX) + ' Y: ' + str(rescueUnitR.coordenadaY))
                print("+++POTENCIALES ENTRADAS ++")
                map: MatrizDispersa
                map = city.matrix
                print("----- Escoja la ENTRADA ----- ")
                map.searchEntranceUnits()
                map.printEntranceUnits()
                entranceUnitData = input(">>")
                # Se establece el punto Salida
                if map.searchByIndexTypeE(int(entranceUnitData), 'E') != False:
                    entranceUnitR: Nodo_Interno
                    entranceUnitR = map.searchByIndexTypeE(int(entranceUnitData), 'E')
                    chooseEntrance = False
                else:
                    print("No se ha seleccionado ninguna unidad")

            # Ya tenemos la entrada y la salida
            # Debe entrar, (ENTRADA, SALIDA, DRON a UTILIZAR)
            # map.findRescuePath()
            print("===================================")
            print("| Configuraciones Iniciales        |")
            print("-----------------------------------")
            print("Dron en uso>> " + str(droneList.searchByIndex(rescueDrone).name))
            print("Ciudad en uso>> " + str(city.name))
            print("Unidad Civil >> " + str(rescueUnitR.CivilUnitIndex) + ' X: ' + str(
                rescueUnitR.coordenadaX) + ' Y: ' + str(rescueUnitR.coordenadaY))
            print("Entrada >> " + str(entranceUnitR.entranceUnitIndex) + ' X: ' + str(
                entranceUnitR.coordenadaX) + ' Y: ' + str(entranceUnitR.coordenadaY))
            print("------------------------------------")
            print("====================================")
            print('************************************')
            print("Calculando Path Finder")
            isPathExtreme(map, entranceUnitR, rescueUnitR,droneList.searchByIndex(rescueDrone) )
    pass

def submenu(nombreCiudad, cities):
    global option
    option = True

    while option == True:
        print("------------------MISIONES -----------------------------------------------------------")
        print("============= Acciones de Ciudad "+ nombreCiudad + " =================================")
        print(Fore.BLUE)
        print("| Dimensiones (Filas X Columnas) >>>" + str(cities.search(nombreCiudad).rows) + 'x' +str(cities.search(nombreCiudad).columns))
        print(Style.RESET_ALL)
        print("|  1. Visualizar Ciudad                                               |")
        print("|  2. Mision de Rescate                                               |")
        print("|  3. Mision de Extracción de Recursos                                |")
        print("|  4. Salir                                                           |")
        print('=======================================================================')

        op = input('Ingresa una opción: ')
        if op == '1':
            print("===Ha visualizar opciones====")

            if cities.search(nombreCiudad) == False:
                print("No se ha encontrado la ciudad")

            else:
                cities.search(nombreCiudad).matrix.graphWithTable(str(nombreCiudad))
        elif op == '2':
            # The code above is the main function of the program. It is the one that will be executed first.
            #BUSCAR SI HAY EXISTENCIA DE CHAPINRESCUE
            print("Se ha seleccionado MISION DE RESCATE")
            if cities.search(nombreCiudad) == False:
                print("No se ha encontrado la ciudad")
            else:
                actualCity = cities.search(nombreCiudad)
                if actualCity.drones.searchRescue() == False:
                    print("-------------------------------")
                    print("| No existen Drones de Rescate |")
                    print("--------------------------------")
                elif actualCity.matrix.searchCivilUnits() == False:
                    print("--------------------------------")
                    print("| No hay Unidades que rescatar  |")
                    print("--------------------------------")

                else:
                    city = cities.search(nombreCiudad)
                    rescueMissions(city)


        elif op == '3':
            #BUSCAR SI HAY EXISTENCIA DE CHAPINFIGHTER
            print("Se ha seleccionado MISSION DE EXTRACCION")
            # BUSCAR SI HAY EXISTENCIA DE CHAPINRESCUE
            print("Se ha seleccionado MISION DE RESCATE")
            if cities.search(nombreCiudad) == False:
                print("No se ha encontrado la ciudad")
            else:
                actualCity = cities.search(nombreCiudad)
                if actualCity.drones.searchFighter() == False:
                    print("-------------------------------")
                    print("| No existen ChapinFighters |")
                    print("--------------------------------")
                elif actualCity.matrix.searchRescueUnits() == False:
                    print("--------------------------------")
                    print("| No hay Unidades que rescatar  |")
                    print("--------------------------------")

                else:
                    city = cities.search(nombreCiudad)
                    extractionMissions(city)
        elif op == '4':
            print("Se ha seleccionado SALIR")
            option = False



