#from heads import Nodo_Encabezado, Lista_Encabezado
from os import system, startfile
import webbrowser
from colorama import Back, Fore, Style
from colorama import init
init(convert=True)
#------------ Nodo que representa el encabezado de una fila y columna respectivamente
class Nodo_Encabezado():
    def __init__(self, id):
        self.id : int = id #posicion de fila o columna
        self.siguiente = None
        self.anterior = None
        self.acceso = None  # Apuntador a los nodos de la matriz(nodos internos)
                            # self.acceso es como el root de la lista que esta en este encabezado
class Lista_Encabezado():
    def __init__(self, tipo):
        self.primero: Nodo_Encabezado = None
        self.ultimo: Nodo_Encabezado = None
        self.tipo = tipo
        self.size = 0

    def insertar_nodoEncabezado(self, nuevo):
        #nuevo = Nodo_Encabezado(nuevo)
        self.size += 1
        if self.primero == None: # Es el primer nodo insertado
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            # ---- Insercion en ORDEN
            # -- verificamos si el nuevo nodo es menor que el primero
            print(nuevo.id, self.primero.id)
            if int(nuevo.id) < int(self.primero.id):
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            # -- verificamos si el nuevo es mayor que el ultimo
            elif int(nuevo.id) > int(self.ultimo.id):
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
            else:
                # -- sino, recorremos la lista para buscar donde acomodarnos, entre el primero y el ultimo
                tmp: Nodo_Encabezado = self.primero
                while tmp != None:
                    if int(nuevo.id) < int(tmp.id):
                        nuevo.siguiente = tmp
                        nuevo.anterior = tmp.anterior
                        if tmp.anterior != None:
                            tmp.anterior.siguiente = nuevo
                            tmp.anterior = nuevo
                            break
                    elif int(nuevo.id) > int(tmp.id):
                        tmp = tmp.siguiente
                    else:
                        break

    def mostrarEncabezados(self):
        tmp = self.primero
        while tmp != None:
            print('Encabezado', self.tipo, tmp.id)
            tmp = tmp.siguiente

    def getEncabezado(self, id) -> Nodo_Encabezado: #esta funcion debe retornar un nodo cabecera
        tmp = self.primero
        while tmp != None:
            if id == tmp.id:
                return tmp
            tmp = tmp.siguiente
        return None
    def length(self):
        tmp = self.primero
        len = 0
        while tmp != None:
            len += 1
            tmp = tmp.siguiente
        return len

# -----------------------------Codigo de MATRIZ DISPERSA ----------------
# -------- Clase NodoOrtogonal, con 4 apuntadores -> Nodos Internos

class Nodo_Interno():  # Nodos ortogonales
    def __init__(self, x, y, caracter, power):  # 'caracter' puede ser cualquier valor
        self.caracter = caracter
        self.power = power
        self.coordenadaX = x  # fila
        self.coordenadaY = y  # columna
        self.arriba = None
        self.abajo = None
        self.derecha = None  # self.siguiente
        self.izquierda = None  # self.anterior
        self.CivilUnitIndex = None
        self.entranceUnitIndex = None
        self.visited = False
        self.resourceUnit = None




class MatrizDispersa():
    def __init__(self, capa):
        self.capa = capa
        self.filas = Lista_Encabezado('fila')  # Encabezados efe X
        self.columnas = Lista_Encabezado('columna')  # Encabezados efe Y

    # (filas = x, columnas = y)
    def insert(self, pos_x, pos_y, caracter, power):
        nuevo = Nodo_Interno(pos_y, pos_x, caracter, power)  # se crea nodo interno
        # --- lo primero sera buscar si ya existen los encabezados en la matriz
        nodo_X = self.filas.getEncabezado(pos_x)
        nodo_Y = self.columnas.getEncabezado(pos_y)

        if nodo_X == None:  # --- comprobamos que el encabezado fila pos_x exista
            # --- si nodo_X es nulo, quiere decir que no existe encabezado fila pos_x, por lo tanto hay que crearlo
            nodo_X = Nodo_Encabezado(pos_x)
            self.filas.insertar_nodoEncabezado(nodo_X)

        if nodo_Y == None:  # --- comprobamos que el encabezado columna pos_y exista
            # --- si nodo_Y es nulo, quiere decir que no existe encabezado columna pos_y, por lo tanto hay que crearlo
            nodo_Y = Nodo_Encabezado(pos_y)
            self.columnas.insertar_nodoEncabezado(nodo_Y)

        # ----- INSERTAR NUEVO EN FILA
        if nodo_X.acceso == None:  # -- comprobamos que el nodo_x no esta apuntando hacia ningun nodoInterno
            nodo_X.acceso = nuevo
        else:  # -- si esta apuntando, validamos si la posicion de la columna del NUEVO nodoInterno es menor a la posicion de la columna del acceso
            if int(nuevo.coordenadaY) < int(nodo_X.acceso.coordenadaY):  # F1 --->  NI 1,1     NI 1,3
                nuevo.derecha = nodo_X.acceso
                nodo_X.acceso.izquierda = nuevo
                nodo_X.acceso = nuevo
            else:
                # de no cumplirse debemos movernos de izquierda a derecha buscando donde posicionar el NUEVO nodoInterno
                tmp: Nodo_Interno = nodo_X.acceso  # nodo_X:F1 --->      NI 1,2; NI 1,3; NI 1,5;
                while tmp != None:  # NI 1,6
                    if int(nuevo.coordenadaY) < int(tmp.coordenadaY):
                        nuevo.derecha = tmp
                        nuevo.izquierda = tmp.izquierda
                        if tmp.izquierda != None:
                            tmp.izquierda.derecha = nuevo
                            tmp.izquierda = nuevo
                            break;
                    elif nuevo.coordenadaX == tmp.coordenadaX and nuevo.coordenadaY == tmp.coordenadaY:  # validamos que no haya repetidas
                        break;
                    else:
                        if tmp.derecha == None:
                            tmp.derecha = nuevo
                            nuevo.izquierda = tmp
                            break;
                        else:
                            tmp = tmp.derecha
                            #         nodo_Y:        C1    C3      C5      C6
                            # nodo_X:F1 --->      NI 1,2; NI 1,3; NI 1,5; NI 1,6;
                            # nodo_X:F2 --->      NI 2,2; NI 2,3; NI 2,5; NI 2,6;

        # ----- INSERTAR NUEVO EN COLUMNA
        if nodo_Y.acceso == None:  # -- comprobamos que el nodo_y no esta apuntando hacia ningun nodoCelda
            nodo_Y.acceso = nuevo
        else:  # -- si esta apuntando, validamos si la posicion de la fila del NUEVO nodoCelda es menor a la posicion de la fila del acceso
            if nuevo.coordenadaX < nodo_Y.acceso.coordenadaX:
                nuevo.abajo = nodo_Y.acceso
                nodo_Y.acceso.arriba = nuevo
                nodo_Y.acceso = nuevo
            else:
                # de no cumplirse, debemos movernos de arriba hacia abajo buscando donde posicionar el NUEVO
                tmp2: Nodo_Interno = nodo_Y.acceso
                while tmp2 != None:
                    if nuevo.coordenadaX < tmp2.coordenadaX:
                        nuevo.abajo = tmp2
                        nuevo.arriba = tmp2.arriba
                        tmp2.arriba.abajo = nuevo
                        tmp2.arriba = nuevo
                        break;
                    elif nuevo.coordenadaX == tmp2.coordenadaX and nuevo.coordenadaY == tmp2.coordenadaY:  # validamos que no haya repetidas
                        break;
                    else:
                        if tmp2.abajo == None:
                            tmp2.abajo = nuevo
                            nuevo.arriba = tmp2
                            break
                        else:
                            tmp2 = tmp2.abajo

        ##------ Fin de insercion
    def graficarConTabla(self, nombre):
        # -- lo primero es settear los valores que nos preocupan
        grafo = 'digraph S{ '
        grafo += ''' a0 [label=<\n<TABLE border="4" cellspacing="0" cellpadding="0" style="rounded" bgcolor="black" gradientangle="315">
 <TR>\n<TD border="0"  bgcolor="white">root</TD>\n
 '''

        # --- lo siguiente es escribir los nodos encabezados, empezamos con las filas, los nodos tendran el foramto Fn
        #Creamos las celdas de las listas
        x_fila = self.filas.primero
        while x_fila != None:
            grafo += '<TD border="0"  bgcolor="powderblue">'+str(x_fila.id)+'</TD>\n'
            x_fila = x_fila.siguiente
        grafo += '</TR>\n'



        # Guardamos los nodos de Y en una lista
        y_columna = self.filas.primero
        aux2 = y_columna.acceso
        while y_columna != None:
            grafo += '<TR>\n'
            grafo += '<TD border="0"  bgcolor="powderblue">'+str(y_columna.id)+'</TD>\n'
            while aux2 != None:
                if aux2.caracter == '*':
                    grafo += '<TD border="0"  bgcolor="black"></TD>\n'
                    aux2 = aux2.derecha
                elif aux2.caracter == 'M':
                    grafo += '<TD border="0"  bgcolor="red"></TD>\n'
                    aux2 = aux2.derecha
                elif aux2.caracter == 'T':
                    grafo += '<TD border="0"  bgcolor="white"></TD>\n'
                    aux2 = aux2.derecha
                elif aux2.caracter == 'E':
                    grafo += '<TD border="0"  bgcolor="green"></TD>\n'
                    aux2 = aux2.derecha
                elif aux2.caracter == 'C':
                    grafo += '<TD border="0"  bgcolor="yellow"></TD>\n'
                    aux2 = aux2.derecha
                elif aux2.caracter == 'R':
                    grafo += '<TD border="0"  bgcolor="grey"></TD>\n'
                    aux2 = aux2.derecha
                else:
                    grafo += '<TD border="0"  bgcolor="blue">NO</TD>\n'
                    aux2 = aux2.derecha
            grafo += '</TR>\n'
            y_columna = y_columna.siguiente

        grafo += '</TABLE>>];}'

        # ---- luego de crear el contenido del Dot, procedemos a colocarlo en un archivo
        dot = "matriz{}.dot".format(nombre)
        file = open(dot, 'w')
        file.write(grafo)
        file.close()

        result = "matriz_{}.pdf".format(nombre)
        system("dot -Tpdf " + dot + " > " + result)
        system('cd .')
        startfile(result)

    def graficarNeato(self, nombre):
        contenido = '''digraph G{
    node[shape=box, width=0.7, height=0.7, fontname="Arial", fillcolor="white", style=filled]
    edge[style = "bold"]
    node[label = "capa:''' + str(self.capa) + '''" fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
        contenido += '''label = "{}" \nfontname="Arial Black" \nfontsize="25pt" \n
                    \n'''.format('\nMATRIZ DISPERSA')

        # --graficar nodos ENCABEZADO
        # --graficar nodos fila
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            contenido += '\n\tnode[label = "F{}" fillcolor="azure3" pos="-1,-{}!" shape=box]x{};'.format(pivote.id,
                                                                                                         posx,
                                                                                                         pivote.id)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            contenido += '\n\tx{}->x{};'.format(pivote.id, pivote.siguiente.id)
            contenido += '\n\tx{}->x{}[dir=back];'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        contenido += '\n\traiz->x{};'.format(self.filas.primero.id)

        # --graficar nodos columna
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            contenido += '\n\tnode[label = "C{}" fillcolor="azure3" pos = "{},1!" shape=box]y{};'.format(pivotey.id,
                                                                                                         posy,
                                                                                                         pivotey.id)
            pivotey = pivotey.siguiente
            posy += 1
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            contenido += '\n\ty{}->y{};'.format(pivotey.id, pivotey.siguiente.id)
            contenido += '\n\ty{}->y{}[dir=back];'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{};'.format(self.columnas.primero.id)

        # ya con las cabeceras graficadas, lo siguiente es los nodos internos, o nodosCelda
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda: Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                # --- buscamos posy
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY: break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                if pivote_celda.caracter == '*':
                    contenido += '\n\tnode[label="*" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format(
                        # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'T':
                    contenido += '\n\tnode[label="T" fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format(
                        # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'M':
                    contenido += '\n\tnode[label="M" fillcolor="red" pos="{},-{}!" shape=box]i{}_{};'.format(
                        # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'E':
                    contenido += '\n\tnode[label="E" fillcolor="green" pos="{},-{}!" shape=box]i{}_{};'.format(
                        # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'C':
                    contenido += '\n\tnode[label="C" fillcolor="yellow" pos="{},-{}!" shape=box]i{}_{};'.format(
                        # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'R':
                    contenido += '\n\tnode[label="*" fillcolor="grey" pos="{},-{}!" shape=box]i{}_{};'.format(
                        # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                else:
                    contenido += '\n\tnode[label=" " fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format(
                        # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                pivote_celda = pivote_celda.derecha

            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.derecha != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                                                              pivote_celda.derecha.coordenadaX,
                                                              pivote_celda.derecha.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX,
                                                                        pivote_celda.coordenadaY,
                                                                        pivote_celda.derecha.coordenadaX,
                                                                        pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha

            contenido += '\n\tx{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\tx{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX,
                                                             pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1

        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda: Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                                                              pivote_celda.abajo.coordenadaX,
                                                              pivote_celda.abajo.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX,
                                                                        pivote_celda.coordenadaY,
                                                                        pivote_celda.abajo.coordenadaX,
                                                                        pivote_celda.abajo.coordenadaY)
                pivote_celda = pivote_celda.abajo
            contenido += '\n\ty{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\ty{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX,
                                                             pivote.acceso.coordenadaY)
            pivote = pivote.siguiente

        contenido += '\n}'
        # --- se genera DOT y se procede a ecjetuar el comando
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "matriz_{}.png".format(nombre)
        system("neato -Tpng" + dot + " > " + result)
        startfile(result)

    def graficarDot(self, nombre):
        # -- lo primero es settear los valores que nos preocupan
        grafo = 'digraph T{ \nnode[shape=box fontname="Arial" fillcolor="white" style=filled ]'
        grafo += '\nroot[label = \"capa: ' + str(self.capa) + '\", group=1]\n'
        grafo += '''label = "{}" \nfontname="Arial Black" \nfontsize="15pt" \n
                    \n'''.format('MATRIZ DISPERSA')

        # --- lo siguiente es escribir los nodos encabezados, empezamos con las filas, los nodos tendran el foramto Fn
        x_fila = self.filas.primero
        while x_fila != None:
            grafo += 'F{}[label="F{}",fillcolor="plum",group=1];\n'.format(x_fila.id, x_fila.id)
            x_fila = x_fila.siguiente

        # --- apuntamos los nodos F entre ellos
        x_fila = self.filas.primero
        while x_fila != None:
            if x_fila.siguiente != None:
                grafo += 'F{}->F{};\n'.format(x_fila.id, x_fila.siguiente.id)
                grafo += 'F{}->F{};\n'.format(x_fila.siguiente.id, x_fila.id)
            x_fila = x_fila.siguiente

        # --- Luego de los nodos encabezados fila, seguimos con las columnas, los nodos tendran el foramto Cn
        y_columna = self.columnas.primero
        while y_columna != None:
            group = int(y_columna.id) + 1
            grafo += 'C{}[label="C{}",fillcolor="powderblue",group={}];\n'.format(y_columna.id, y_columna.id,
                                                                                  str(group))
            y_columna = y_columna.siguiente

        # --- apuntamos los nodos C entre ellos
        cont = 0
        y_columna = self.columnas.primero
        while y_columna is not None:
            if y_columna.siguiente is not None:
                grafo += 'C{}->C{}\n'.format(y_columna.id, y_columna.siguiente.id)
                grafo += 'C{}->C{}\n'.format(y_columna.siguiente.id, y_columna.id)
            cont += 1
            y_columna = y_columna.siguiente

        # --- luego que hemos escrito todos los nodos encabezado, apuntamos el nodo root hacua ellos
        y_columna = self.columnas.primero
        x_fila = self.filas.primero
        grafo += 'root->F{};\n root->C{};\n'.format(x_fila.id, y_columna.id)
        grafo += '{rank=same;root;'
        cont = 0
        y_columna = self.columnas.primero
        while y_columna != None:
            grafo += 'C{};'.format(y_columna.id)
            cont += 1
            y_columna = y_columna.siguiente
        grafo += '}\n'
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux != None:
            cont += 1
            while aux2 != None:
                # if aux2.caracter == '-':
                #    grafo += 'N{}_{}[label=" ",group="{}"];\n'.format(aux2.coordenadaX, aux2.coordenadaY, int(aux2.coordenadaY)+1)
                # el
                if aux2.caracter == '*':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="black"];\n'.format(aux2.coordenadaX,aux2.coordenadaY,aux2.caracter,int(aux2.coordenadaY) + 1)
                elif aux2.caracter == 'M':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="red"];\n'.format(aux2.coordenadaX,aux2.coordenadaY,aux2.caracter,int(aux2.coordenadaY) + 1)
                elif aux2.caracter == 'T':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="white"];\n'.format(aux2.coordenadaX,aux2.coordenadaY,aux2.caracter,int(aux2.coordenadaY) + 1)

                elif aux2.caracter == 'E':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="green"];\n'.format(aux2.coordenadaX,aux2.coordenadaY,aux2.caracter,int(aux2.coordenadaY) + 1)
                elif aux2.caracter == 'C':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="yellow"];\n'.format(aux2.coordenadaX,aux2.coordenadaY,aux2.caracter,int(aux2.coordenadaY) + 1)
                elif aux2.caracter == 'R':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="grey"];\n'.format(aux2.coordenadaX,aux2.coordenadaY,aux2.caracter,int(aux2.coordenadaY) + 1)

                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux is not None:
            rank = '{' + f'rank = same;F{aux.id};'
            cont = 0
            while aux2 != None:
                if cont == 0:
                    grafo += 'F{}->N{}_{};\n'.format(aux.id, aux2.coordenadaX, aux2.coordenadaY)
                    grafo += 'N{}_{}->F{};\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux.id)
                    cont += 1
                if aux2.derecha != None:
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux2.derecha.coordenadaX,
                                                        aux2.derecha.coordenadaY)
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.derecha.coordenadaX, aux2.derecha.coordenadaY,
                                                        aux2.coordenadaX, aux2.coordenadaY)

                rank += 'N{}_{};'.format(aux2.coordenadaX, aux2.coordenadaY)
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
            grafo += rank + '}\n'
        aux = self.columnas.primero
        aux2 = aux.acceso
        cont = 0
        while aux != None:
            cont = 0
            grafo += ''
            while aux2 != None:
                if cont == 0:
                    grafo += 'C{}->N{}_{};\n'.format(aux.id, aux2.coordenadaX, aux2.coordenadaY)
                    grafo += 'N{}_{}->C{};\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux.id)
                    cont += 1
                if aux2.abajo != None:
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.abajo.coordenadaX, aux2.abajo.coordenadaY,
                                                        aux2.coordenadaX, aux2.coordenadaY)
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux2.abajo.coordenadaX,
                                                        aux2.abajo.coordenadaY)
                aux2 = aux2.abajo
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        grafo += '}'

        # ---- luego de crear el contenido del Dot, procedemos a colocarlo en un archivo
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as f:
            f.write(grafo)
        result = "matriz_{}.pdf".format(nombre)
        system("dot -Tpdf " + dot + " > " + result)
        system('cd .')
        startfile(result)

    def print(self):

        print(Back.LIGHTMAGENTA_EX)
        print("===========IMPRESION DE MATRIZ=============")
        x_fila = self.filas.primero
        while x_fila != None:
            print(str(x_fila.id), end="-> ")
            x_fila = x_fila.siguiente
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux != None:
            cont += 1
            print("")
            print(Back.CYAN + str(aux.id), end="->")

            while aux2 != None:
                if aux2.caracter == '*':
                    print(Back.BLACK + '*', end="->")


                elif aux2.caracter == 'T':
                    print(Back.WHITE + 'T', end="->")
                    #print(Style.RESET_ALL, end="")

                elif aux2.caracter == 'E':
                    print(Back.GREEN + 'E', end="->")
                    #print(Style.RESET_ALL, end="")

                elif aux2.caracter == 'C':
                    print(Back.BLUE +  'C', end="->")
                    #print(Style.RESET_ALL, end="")

                elif aux2.caracter == 'R':
                    print(Back.LIGHTWHITE_EX +  'R', end="->")
                    #print(Style.RESET_ALL, end="")

                #print(aux2.caracter, end="->")

                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso

        print("")

    def graphWithTable(self, name):
        graphviz = ' '
        graphviz += '''digraph G {\nnode [fontname="Helvetica,Arial,sans-serif"]\nedge [fontname="Helvetica,Arial,sans-serif"]\n
\tsubgraph cluster1 {node [shape=square fillcolor="black" style="radial" gradientangle=180 style="rounded"]\na0 [label=<'''
        graphviz += '\n<TABLE border="10" cellspacing="0" cellpadding="20" style="rounded" bgcolor="black" gradientangle="315">'
        print(Back.LIGHTMAGENTA_EX)
        print("===========IMPRESION DE MATRIZ=============")
        x_fila = self.columnas.primero
        graphviz += '<TR>'
        graphviz += '<TD border="3" bgcolor="white" gradientangle="270">Root</TD>'
        while x_fila != None:
            print(str(x_fila.id), end="->")
            # Se anaden nodos X en la tabla
            graphviz += '<TD border="3" bgcolor="powderblue" gradientangle="270">'+str(x_fila.id)+'</TD>'
            x_fila = x_fila.siguiente
        graphviz += '</TR>'

        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux != None:
            cont += 1
            print("")
            graphviz += '<TR>'
            print(Back.CYAN + str(aux.id), end="->")
            graphviz += '<TD border="3"  bgcolor="powderblue">'+str(aux.id)+'</TD>'
            while aux2 != None:
                if aux2.caracter == '*':
                    print(Back.BLACK + '*', end="->")
                    graphviz += '<TD border="3"  bgcolor="black">' + str(aux2.caracter) + '</TD>'

                elif aux2.caracter == 'T':
                    print(Back.WHITE + 'T', end="->")
                    #print(Style.RESET_ALL, end="")
                    graphviz += '<TD border="3"  bgcolor="white">' + str(aux2.caracter) + '</TD>'

                elif aux2.caracter == 'E':
                    print(Back.GREEN + 'E', end="->")
                    #print(Style.RESET_ALL, end="")
                    graphviz += '<TD border="3"  bgcolor="green">' + str(aux2.caracter) + '</TD>'
                elif aux2.caracter == 'C':
                    print(Back.LIGHTBLUE_EX +  'C', end="->")
                    #print(Style.RESET_ALL, end="")
                    graphviz += '<TD border="3"  bgcolor="grey">' + str(aux2.caracter) + '</TD>'
                elif aux2.caracter == 'R':
                    print(Back.BLUE +  'R', end="->")
                    graphviz += '<TD border="3"  bgcolor="blue">' + str(aux2.caracter) + '</TD>'
                    #print(Style.RESET_ALL, end="")

                elif aux2.caracter == 'M':
                    print(Back.LIGHTWHITE_EX +  'M', end="->")
                    graphviz += '<TD border="3"  bgcolor="red">' + str(aux2.caracter) + '</TD>'
                    #print(Style.RESET_ALL, end="")
                elif aux2.caracter == 'V':
                    print(Back.YELLOW +  'M', end="->")
                    graphviz += '<TD border="3"  bgcolor="yellow">' + str(aux2.caracter) + '</TD>'

                elif aux2.caracter == 'D':
                    print(Back.LIGHTRED +  'M', end="->")
                    graphviz += '<TD border="3"  bgcolor="purple">' + str(aux2.caracter) + '</TD>'

                #print(aux2.caracter, end="->")

                aux2 = aux2.derecha
            aux = aux.siguiente
            graphviz += '</TR>'
            if aux != None:
                aux2 = aux.acceso
        graphviz += '</TABLE>>];}}'

        dot = "matriz{}.dot".format(name)
        file = open(dot, 'w')
        file.write(graphviz)
        file.close()

        result = "matriz_{}.pdf".format(name)
        system("dot -Tpdf " + dot + " > " + result)
        system('cd .')
        startfile(result)

    def printCivilUnits(self):



        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 1
        posX = 1
        posY = 1
        while aux != None:

            aux2.CivilUnitsIndex = 0
            while aux2 != None:
                if aux2.caracter == 'C':
                    aux2.CivilUnitIndex = cont

                    print("-----Unidad Civil: " + str(cont)+ "-----")
                    print("fila >> " + str(aux2.coordenadaY))
                    print("columna >> "+ str(aux2.coordenadaX))
                    print("--------------------------------")
                    cont += 1




                aux2 = aux2.derecha
                posX +=1
            aux = aux.siguiente
            posY += 1
            if aux != None:
                aux2 = aux.acceso

        if cont == 0:
            return False

    def printResourceUnits(self):



        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 1
        posX = 1
        posY = 1
        while aux != None:
            aux2: Nodo_Interno
            aux2.CivilUnitsIndex = 0
            while aux2 != None:
                if aux2.caracter == 'R':
                    aux2.resourceUnit = cont

                    print("-----Unidad Recurso: " + str(cont)+ "-----")
                    print("fila >> " + str(aux2.coordenadaY))
                    print("columna >> "+ str(aux2.coordenadaX))
                    print("--------------------------------")
                    cont += 1




                aux2 = aux2.derecha
                posX +=1
            aux = aux.siguiente
            posY += 1
            if aux != None:
                aux2 = aux.acceso

        if cont == 0:
            return False

    def printEntranceUnits(self):



        aux = self.filas.primero
        aux2: Nodo_Interno
        aux2 = aux.acceso
        cont = 0
        posX = 1
        posY = 1
        while aux != None:
            counter = 0
            #aux2.entranceUnitIndex = 0
            while aux2 != None:
                if aux2.caracter == 'E':
                    cont += 1
                    aux2.entranceUnitIndex = cont

                    print("-----Entrada: " + str(aux2.entranceUnitIndex) + "-----")
                    print("fila >> " + str(aux2.coordenadaY))
                    print("columna >> " + str(aux2.coordenadaX))
                    print("--------------------------------")

                aux2 = aux2.derecha
                posX += 1
            aux = aux.siguiente
            posY += 1
            if aux != None:
                aux2 = aux.acceso

        if cont == 0:
            return False

    def searchCivilUnits(self):
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        posX = 1
        posY = 1
        while aux != None:


            while aux2 != None:
                if aux2.caracter == 'C':
                    cont += 1
                    aux2.CivilUnitIndex = cont

                aux2 = aux2.derecha
                posX += 1
            aux = aux.siguiente
            posY += 1
            if aux != None:
                aux2 = aux.acceso

        if cont == 0:
            return False

    def searchRescueUnits(self):
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        posX = 1
        posY = 1
        while aux != None:


            while aux2 != None:
                if aux2.caracter == 'R':
                    cont += 1
                    aux2:Nodo_Interno
                    aux2.resourceUnit = cont

                aux2 = aux2.derecha
                posX += 1
            aux = aux.siguiente
            posY += 1
            if aux != None:
                aux2 = aux.acceso

        if cont == 0:
            return False

    def searchByIndexType(self, index, type):
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        posX = 1
        posY = 1
        while aux != None:

            contador = 0
            while aux2 != None:
                if aux2.caracter == type.upper() and aux2.CivilUnitIndex == index:
                    return aux2
                    cont += 1

                aux2 = aux2.derecha
                posX += 1
            aux = aux.siguiente
            posY += 1
            if aux != None:
                aux2 = aux.acceso

        if cont == 0:
            return False


        print("")

    def searchByIndexTypeE(self, index, type):
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        posX = 1
        posY = 1
        while aux != None:

            contador = 0
            while aux2 != None:
                if aux2.caracter == type.upper() and aux2.entranceUnitIndex == index:
                    return aux2
                    cont += 1

                aux2 = aux2.derecha
                posX += 1
            aux = aux.siguiente
            posY += 1
            if aux != None:
                aux2 = aux.acceso

        if cont == 0:
            return False


        print("")
    def searchByIndexTypeR(self, index, type):
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        posX = 1
        posY = 1
        while aux != None:

            contador = 0
            while aux2 != None:
                if aux2.caracter == type.upper() and aux2.resourceUnit == index:
                    return aux2
                    cont += 1

                aux2 = aux2.derecha
                posX += 1
            aux = aux.siguiente
            posY += 1
            if aux != None:
                aux2 = aux.acceso

        if cont == 0:
            return False


        print("")
    def searchEntranceUnits(self):
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        posX = 1
        posY = 1
        while aux != None:


            while aux2 != None:
                if aux2.caracter == 'E':
                    cont += 1
                    aux2.entranceUnitIndex = cont

                aux2 = aux2.derecha
                posX += 1
            aux = aux.siguiente
            posY += 1
            if aux != None:
                aux2 = aux.acceso

        if cont == 0:
            return False

    def searchCoordinates(self, X, Y):
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0

        while aux != None:

            while aux2 != None:
                if int(aux2.coordenadaY) == int(Y) and int(aux2.coordenadaX) == int(X):
                    cont += 1
                    return aux2

                aux2 = aux2.derecha

            aux = aux.siguiente

            if aux != None:
                aux2 = aux.acceso

        if cont == 0:
            return False

    #Le deben ingresar ENTRADA, SALIDA, DRON
    def pathFinderRescue(self, entrada, salida, dron):
        #Path Finding con Algoritmo A*

        #Find the start and the end
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        posX = 1
        posY = 1
        while aux != None:

            contador = 0
            while aux2 != None:
                if aux2.caracter == 'E' and aux2.entranceUnitIndex == entrada.entranceUnitIndex:
                    #Ya nos encontramos en la entrada, ahora debemos encontrar un camino

                    #Verificamos



                    cont += 1

                aux2 = aux2.derecha
                posX += 1
            aux = aux.siguiente
            posY += 1
            if aux != None:
                aux2 = aux.acceso

        if cont == 0:
            return False
        pass



