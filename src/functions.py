from os import system, startfile
from colorama import Fore, Back, Style, init
from models.disperseMatrix import MatrizDispersa,Nodo_Interno
init(convert=True)
from models.drones import Drone

global instructions
global finalMatrix
#finalMatrix: designList
# Python3 program to find
# path between two cell in matrix

# Method for finding and printing
# whether the path exists or not
def isPath(matrix: MatrizDispersa, entrada: Nodo_Interno, salida: Nodo_Interno):
    print("====DIMENSIONES DE LA MATRIX=====")
    print("Filas>>")
    print(matrix.filas.length())
    print("Columnas>>")
    print(matrix.columnas.length())
    # Defining visited array to keep
    #Se crea una matriz de comparación
    #Sabemos que todos los nodos de MATRIX tendran como Falso el valor visited
    visited: MatrizDispersa
    visited = matrix


    # Flag to indicate whether the
    # path exists or not
    flag = False

    for j in range(1, int(matrix.filas.length()), 1):

        for i in range(1, int(matrix.columnas.length()), 1):

            # 1.
            Node : Nodo_Interno = matrix.searchCoordinates(i, j)

            visitedNode: Nodo_Interno = visited.searchCoordinates(i,j)
            #Si es source, podemos proceder a realizar el algoritmo
            if (Node.caracter == 'E' and visitedNode.visited == False and int(Node.coordenadaX) == int(entrada.coordenadaX) and int(Node.coordenadaY) == int(entrada.coordenadaY)):
                print("|", end="")

                # Starting from i, j and
                # then finding the path
                if (checkPath(matrix, i,j, visited, salida)):
                    # If path exists
                    flag = True
                    break
            print(Node.caracter, end="->")
        print("")
    if (flag):
        print("=====================")
        print("Existe al menos algun camino")
        print("=====================")
    else:

        print("========================")
        print("NO EXISTE NINGUN CAMINO")
        print("========================")


# Method for checking boundaries
def isSafe(i, j, matrix: MatrizDispersa):
    if (i > 0 and i < matrix.columnas.length() and
            j > 0 and j < matrix.filas.length()):
        return True
    return False


# Returns true if there is a
# path from a source(a
# cell with value 1) to a
# destination(a cell with
# value 2)
def checkPath(matrix: MatrizDispersa, i, j,visited: MatrizDispersa, salida: Nodo_Interno):
    # Checking the boundaries, walls and
    # whether the cell is unvisited
    Node: Nodo_Interno
    visitedNode : Nodo_Interno
    visitedNode = visited.searchCoordinates(i,j)
    Node = matrix.searchCoordinates(i,j)
    if (isSafe(i, j, matrix) and Node.caracter != '*' and Node.caracter != 'M' and visitedNode.visited == False ):

        # Make the cell visited


        # If the cell is the required
        # destination then return true
        if (Node.caracter == 'C' and int(Node.coordenadaX) == int(salida.coordenadaX) and int(Node.coordenadaY == salida.coordenadaY)):
            visited.graphWithTable('SALIDA')
            return True

        visitedNode.visited = True
        visitedNode.caracter = 'V'


        # traverse up
        up = checkPath(matrix, i - 1, j, visited, salida)

        # If path is found in up
        # direction return true
        if (up):
            return True

        # Traverse left
        left = checkPath(matrix, i, j - 1, visited, salida)

        # If path is found in left
        # direction return true
        if (left):
            return True

        # Traverse down
        down = checkPath(matrix, i + 1, j, visited, salida)

        # If path is found in down
        # direction return true
        if (down):
            return True


        # Traverse right
        right = checkPath(matrix, i, j + 1, visited, salida)

        # If path is found in right
        # direction return true
        if (right):
            return True



    # No path has been found
    return False

def checkPathExtreme(matrix: MatrizDispersa, i, j,visited: MatrizDispersa, salida: Nodo_Interno, drone: Drone):
    # Checking the boundaries, walls and
    # whether the cell is unvisited
    Node: Nodo_Interno
    visitedNode : Nodo_Interno
    visitedNode = visited.searchCoordinates(i,j)
    Node = matrix.searchCoordinates(i,j)
    if (isSafe(i, j, matrix) and Node.caracter != '*' and visitedNode.visited == False ):

        if Node.caracter == 'M':
            if float(drone.capacity) > float(Node.power):
                visitedNode.visited = True
                visitedNode.caracter = 'V'
                visited.graphWithTable('Try')



        # Make the cell visited


        # If the cell is the required
        # destination then return true
        if (Node.caracter == 'R' and int(Node.coordenadaX) == int(salida.coordenadaX) and int(Node.coordenadaY == salida.coordenadaY) and Node.caracter != 'C'):
            visited.graphWithTable('SALIDARECURSOS')
            return True



        visitedNode.visited = True
        visitedNode.caracter = 'V'




        # traverse up
        up = checkPathExtreme(matrix, i - 1, j, visited, salida, drone)

        # If path is found in up
        # direction return true
        if (up):
            return True

        # Traverse left
        left = checkPathExtreme(matrix, i, j - 1, visited, salida, drone)

        # If path is found in left
        # direction return true
        if (left):
            return True

        # Traverse down
        down = checkPathExtreme(matrix, i + 1, j, visited, salida, drone)

        # If path is found in down
        # direction return true
        if (down):
            return True

        # Traverse right
        right = checkPathExtreme(matrix, i, j + 1, visited, salida, drone)

        # If path is found in right
        # direction return true
        if (right):
            return True


                #return True

    # No path has been found
    return False
# Driver code

def isPathExtreme(matrix: MatrizDispersa, entrada: Nodo_Interno, salida: Nodo_Interno, drone: Drone):
    print("====DIMENSIONES DE LA MATRIX=====")
    print("Filas>>")
    print(matrix.filas.length())
    print("Columnas>>")
    print(matrix.columnas.length())
    print("Dron>> " + str(drone.name))

    # Defining visited array to keep
    #Se crea una matriz de comparación
    #Sabemos que todos los nodos de MATRIX tendran como Falso el valor visited
    visited: MatrizDispersa
    visited = matrix


    # Flag to indicate whether the
    # path exists or not
    flag = False

    for j in range(1, int(matrix.filas.length()), 1):

        for i in range(1, int(matrix.columnas.length()), 1):

            # 1.
            Node : Nodo_Interno = matrix.searchCoordinates(i, j)

            visitedNode: Nodo_Interno = visited.searchCoordinates(i,j)
            #Si es source, podemos proceder a realizar el algoritmo
            if (Node.caracter == 'E' and visitedNode.visited == False and int(Node.coordenadaX) == int(entrada.coordenadaX) and int(Node.coordenadaY) == int(entrada.coordenadaY)):
                print("|", end="")

                # Starting from i, j and
                # then finding the path
                if (checkPathExtreme(matrix, i,j, visited, salida, drone)):
                    # If path exists
                    flag = True
                    break
            print(Node.caracter, end="->")
        print("")
    if (flag):
        print("---------------------------")
        print("EXISTE AL MENOS UN CAMINO")
        print("===========================")
    else:
        print("============================")
        print(" NO EXISTE NINGUN CAMINO ")
        print("=============================")
# This code is contributed by Chitranayal







