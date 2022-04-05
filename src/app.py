from typing import List
from colorama import Fore, Style, Back, init
init(convert=True)
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd
from analyzer import analyzeXML
from models.city import listaCiudades
#from models.piso import Piso, listaPisos
from helpers import submenu
if __name__ == '__main__':
    while True:
        print(Fore.LIGHTMAGENTA_EX + 'hie')
        print("=============Menu =======================")
        print("|  1. Cargar Configuraciones del Sistema |")
        print("|  2. Salir                              |")
        print('=========================================')

        op = input('Ingresa una opción: ')
        if op == '1':
            print("===Ha escogido Cargar Configuraciones del Sistema====")

            Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
            filename = fd.askopenfilename(title="Select file", filetypes=(("XML Files", "*.xml"), ("All", "*.txt")))
            print(filename)
            file = open(filename,encoding="utf8")
            ciudades = listaCiudades()

            cities = analyzeXML(file, ciudades)
            print("")
            print("Lectura Terminada")
            print(Fore.GREEN + "                                                    Lectura terminada                  ")
            print(Style.RESET_ALL)
            print("")
            print("")
            print("-----------------------------------------------------")
            print("-----------ESCRIBA EL NUMERO DE LA CIUDAD  -----------")
            print("-----------------------------------------------------")
            cities.print()

            cityName = input(">>")
            cityName = str(cityName.replace(" ", '').replace("\n", ''))
            if cities.searchByIndex(cityName) != False:
                #Enviar las ciudades a la MENU
                cityRealName = cities.searchByIndex(cityName).name
                print("Se ha encontrado la ciudad")
                submenu(cityRealName, cities)
            else:
                print("El piso no ha sido cargado")
                pass


            #First

            # process_file(tokens, errs)
        elif op == '2':
            print("===salir====")
            print("==================================")
            print("| Gracias por usar el Analizador |")
            print("==================================")
            exit()

