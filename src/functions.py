from os import system, startfile
from colorama import Fore, Back, Style, init
from models.disperseMatrix import MatrizDispersa,Nodo_Interno
init(convert=True)


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
    print(matrix.filas.lenght())
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

    for i in range(matrix.filas.length()):
        for j in range(matrix.columnas.length()):

            # If matrix[i][j] is source
            # and it is not visited
            Node : Nodo_Interno
            visitedNode: Nodo_Interno
            Node = matrix.searchCoordinates(i, j)
            visitedNode = visited.searchCoordinates(i,j)
            if (Node.caracter == entrada.caracter and
            visitedNode.visited != False and Node.coordenadaX == entrada.coordenadaX and
                    Node.coordenadaY == entrada.coordenadaY):


                # Starting from i, j and
                # then finding the path
                if (checkPath(matrix, i,j, visited, salida)):
                    # If path exists
                    flag = True
                    break
    if (flag):
        print("YES")
    else:
        print("NO")


# Method for checking boundaries
def isSafe(i, j, matrix: MatrizDispersa):
    if (i >= 0 and i < matrix.filas.lenght() and
            j >= 0 and j < matrix.columnas.lenght()):
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
    if (isSafe(i, j, matrix) and Node.caracter != '*' and Node.caracter != 'M' and
            visitedNode.visited == False ):

        # Make the cell visited
        visitedNode.visited = True

        # If the cell is the required
        # destination then return true
        if (Node.caracter == salida.caracter and Node.coordenadaX == salida.coordenadaX and Node.coordenadaY == salida.coordenadaY):

            return True

        # traverse up
        up = checkPath(matrix, i - 1,
                       j, visited, salida)

        # If path is found in up
        # direction return true
        if (up):
            return True

        # Traverse left
        left = checkPath(matrix, i,
                         j - 1, visited, salida)

        # If path is found in left
        # direction return true
        if (left):
            return True

        # Traverse down
        down = checkPath(matrix, i + 1,
                         j, visited, salida)

        # If path is found in down
        # direction return true
        if (down):
            return True

        # Traverse right
        right = checkPath(matrix, i,
                          j + 1, visited, salida)

        # If path is found in right
        # direction return true
        if (right):
            return True

    # No path has been found
    return False


# Driver code


# This code is contributed by Chitranayal







