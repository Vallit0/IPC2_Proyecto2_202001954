from os import system, startfile
from colorama import Fore, Back, Style, init
init(convert=True)
#from models.piso import Piso, listaPisos
from models.matrixNode import matrix, matrixNode
from models.nodes import designList, designNode
global instructions
global finalMatrix
finalMatrix: designList
def inverseColor(text: str) -> str:
    if text.upper() == 'B':
        return 'W'
    elif text.upper() == 'W':
        return 'B'
    else:
        print("El color ingresado no es valido")

def generateArchive(text, inputname, outname) -> None:
    filename = inputname + 'to' + outname + '.txt'
    print(text)
    file = open(filename, 'w')
    file.write(str(text))
    file.close()
    system('cd .')
    startfile(filename)


def graphOutcomes(diseno: designList, name, inputname, outname):
    head: designNode
    head = diseno.head
    text = '''digraph Example{
            fontname="Helvetica,Arial,sans-serif"
            node [fontname="Helvetica,Arial,sans-serif"]
            edge [fontname="Helvetica,Arial,sans-serif"]'''
    text += '\n label = Analisis de Cambio entre  ' + inputname + ' ' + outname + ' ;'
    text += '\n label = ' + name + ';'

    filename = inputname + 'to' + outname
    filename += '.dot'
    outputFileName = inputname + 'to' + outname + '.png'
    while head != None:
        head.patron.writeGraph()
        text += head.patron.returnGraphviz()
        head = head.next

    text += '}'
    text = text.replace("+", '')
    print()
    print(text)
    file = open(filename, 'w')
    file.write(str(text))
    file.close()

    system('dot -Tpng ' + filename + ' > ' + outputFileName)
    system('cd .')
    startfile(outputFileName)
    pass

def addInstruction(instruction: str, swap: bool, index: int, price: float, total: float) -> str:
    desition = ''
    if swap == True:
        desition += 'swap'
        instruction += str(index) + '. ' + 'Realizar un ' + desition + ' ' + 'Q. ' + str(price) + '\n'
        instruction += 'Acumulado ' + str(total)
        return instruction
    else:
        desition += 'flip'
        instruction += str(index) + '. ' + 'Realizar un ' + desition + ' ' + 'Q. ' + str(price)
        return instruction

global option
option = True
def graph(name: str, listPisos):
    designsList: designList
    designsList = listPisos.search(name).patrones
    head: designNode
    head = designsList.head
    text = '''digraph Example{
        fontname="Helvetica,Arial,sans-serif"
        node [fontname="Helvetica,Arial,sans-serif"]
        edge [fontname="Helvetica,Arial,sans-serif"]'''
    text += '\n label = ' + name + ';'
    filename = name
    filename += '.dot'
    outputFileName = name + '.png'
    while head != None:
        head.patron.writeGraph()
        text += head.patron.returnGraphviz()
        head = head.next


    text += '}'
    text = text.replace("+", '')
    print(Fore.BLACK)
    print(Back.WHITE)
    print(text)
    print(Style.RESET_ALL)
    file = open(filename, 'w')
    file.write(str(text))
    file.close()

    system('dot -Tpng '+ filename + ' > '+ outputFileName)
    system('cd .')
    startfile(outputFileName)

def graphDirect(name: str, designsList):
    head: designNode
    head = designsList.head
    text = '''digraph Example{
        fontname="Helvetica,Arial,sans-serif"
        node [fontname="Helvetica,Arial,sans-serif"]
        edge [fontname="Helvetica,Arial,sans-serif"]'''
    text += '\n label = ' + name + ';'
    filename = name
    filename += '.dot'
    outputFileName = name + '.png'
    while head != None:
        head.patron.writeGraph()
        text += head.patron.returnGraphviz()
        head = head.next


    text += '}'
    text = text.replace("+", '')
    print(Fore.BLACK)
    print(Back.WHITE)
    print(text)
    print(Style.RESET_ALL)
    file = open(filename, 'w')
    file.write(str(text))
    file.close()

    system('dot -Tpng '+ filename + ' > '+ outputFileName)
    system('cd .')
    startfile(outputFileName)

def operation(inputMatrix: matrix, swap: bool, index1,color1, index2, color2):
    if swap:
        print("Realizar Swap")
        inputMatrix.swap(index1,color1, int(index2), color2)
    elif swap is False:
        inputMatrix.flip(index1, color1)

    else:
        print("Se ha utilizado mal esta funcion")

def compare(inputMatrix: matrix, outputMatrix: matrix):
    proofMatrix: matrix
    head: matrixNode
    headInput: matrixNode
    headOutput: matrixNode
    inputMatrix.indexList()
    headInput = inputMatrix.head
    headOutput = outputMatrix.head
    totalAcumulado: float = 0
    instructions = ''
    instructionIndex: int = 0
    index = 0

    diseno = designList()
    print("MATRIZ DE ENTRADA")
    inputMatrix.print()
    print("MATRIZ DE SALIDA ")
    outputMatrix.indexList()
    outputMatrix.print()


    while headInput != None:
        up:matrixNode
        down:matrixNode
        left:matrixNode
        right: matrixNode
        upOut: matrixNode
        downOut: matrixNode
        rightOut: matrixNode

        totalFlip = totalAcumulado + float(headInput.flip)
        totalSwap = totalAcumulado + float(headInput.swap)
        if ((totalFlip) > (totalSwap)):
            if headInput.color != headOutput.color:
                # First, the robot need to watch the perifericals
                up, down, left, right = inputMatrix.orthogonalNodes(headInput)
                upOut, downOut, leftOut, rightOut = outputMatrix.orthogonalNodes(headInput)
                # Verification process
                ############################# INICIA PROCESO DE BLOQUEO DE NODOS #################3
                if down != None:
                    if down.color == downOut.color:
                        print("El plato de abajo ya esta en su lugar")
                        down.block = True
                else:
                    print("El plato de abajo no existe")
                    #down.block = True

                if right != None:
                    if right.color == rightOut.color:
                        print("El plato de derecha no es permutable")
                        right.block = True
                else:
                    print("El plato de derecha no existe")
                    #right.block = True
            ################################## TERMINA PROCESO DE BLOQUEO DE NODOS ##################



                #Primero verificará a la derecha (Esto para facilitar el potencial cambio)
                if right.block == False: #Si no esta bloqueado
                    print("Hacer cambio con la derecha")
                    #Si se realiza este Swap, el siguiente nodo quedara en su lugar?
                    if rightOut.color == headInput.color: #Tiene el color que necesito?
                        print("SE REALIZA EL SWAP HACIA LA DERECHA")
                        instructions += addInstruction(instructions, True, instructionIndex, headInput.swap,
                                                       totalAcumulado)
                        # ################################################## Cambio a la derecha
                        operation(inputMatrix, True, index, inverseColor(headInput.color), index + 1, headInput.color)
                        diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        index += 1
                        # Actualizar Head, ya que es una copia de la anterior
                        headInput = inputMatrix.head
                        headOutput = outputMatrix.head
                        for i in range(index):
                            headInput = headInput.next
                            headOutput = headOutput.next

                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        print()
                        totalAcumulado += headInput.swap

                    elif down.block == False:
                        if downOut.color == headInput.color:
                            print("SE REALIZA EL SWAP HACIA LA ABAJO")
                            instructions += addInstruction(instructions, True, instructionIndex, headInput.swap,
                                                           totalAcumulado)
                            # ################################################## Cambio abajo
                            operation(inputMatrix, True, index, inverseColor(headInput.color), index + int(inputMatrix.columns),
                                      headInput.color)
                            diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            index += 1
                            # Actualizar Head, ya que es una copia de la anterior
                            headInput = inputMatrix.head
                            headOutput = outputMatrix.head
                            for i in range(index):
                                headInput = headInput.next
                                headOutput = headOutput.next

                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            print()
                            totalAcumulado += headInput.swap
                        else:
                            print("FLIP")
                            instructions += addInstruction(instructions, False, instructionIndex, headInput.flip,
                                                           totalAcumulado)
                            # ################################################## FLIP
                            operation(inputMatrix, False, index, inverseColor(headInput.color), index + 1,
                                      headInput.color)
                            diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            index += 1
                            headInput = inputMatrix.head
                            headOutput = outputMatrix.head
                            for i in range(index):
                                headInput = headInput.next
                                headOutput = headOutput.next

                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            print()
                            totalAcumulado += headInput.flip
                    else:
                        print("FLIP")
                        instructions += addInstruction(instructions, False, instructionIndex, headInput.flip,
                                                       totalAcumulado)
                        # ################################################## FLIP
                        operation(inputMatrix, False, index, inverseColor(headInput.color), index + 1,
                                  headInput.color)
                        diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        index += 1
                        # Actualizar Head, ya que es una copia de la anterior
                        headInput = inputMatrix.head
                        headOutput = outputMatrix.head
                        for i in range(index):
                            headInput = headInput.next
                            headOutput = headOutput.next

                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        print()
                        totalAcumulado += headInput.flip

                elif down != None and down.block == False:

                    # Si se realiza este Swap, el siguiente nodo quedara en su lugar?
                    if downOut.color == headInput.color:
                        print("SE REALIZA EL SWAP HACIA LA ABAJO")
                        instructions += addInstruction(instructions, True, instructionIndex, headInput.swap,
                                                       totalAcumulado)
                        # ################################################## Cambio abajo
                        operation(inputMatrix, True, index, inverseColor(headInput.color),
                                  index + int(inputMatrix.columns),
                                  headInput.color)
                        diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        index += 1

                        headInput = inputMatrix.head
                        headOutput = outputMatrix.head
                        for i in range(index):
                            headInput = headInput.next
                            headOutput = headOutput.next

                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        print()
                        totalAcumulado += headInput.swap
                    else:
                        print("FLIP")
                        instructions += addInstruction(instructions, False, instructionIndex, headInput.flip,
                                                       totalAcumulado)
                        # ################################################## FLIP
                        operation(inputMatrix, False, index, inverseColor(headInput.color), index + 1,
                                  headInput.color)
                        diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        index += 1
                        # Actualizar Head, ya que es una copia de la anterior
                        headInput = inputMatrix.head
                        headOutput = outputMatrix.head
                        for i in range(index):
                            headInput = headInput.next
                            headOutput = headOutput.next

                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        print()
                        totalAcumulado += headInput.flip

            else:

                print(" Este Nodo ya se encuentra en su lugar ")
                headOutput = headOutput.next
                headInput = headInput.next

        elif ((totalFlip) < (totalSwap)):
            if headInput.color != headOutput.color:
                # First, the robot need to watch the perifericals
                up, down, left, right = inputMatrix.orthogonalNodes(headInput)
                upOut, downOut, leftOut, rightOut = outputMatrix.orthogonalNodes(headInput)

                # Verification process
                # Compare the Perifericals with headOutPut

                if down != None:
                    if down.color == downOut.color:
                        print("El plato de abajo ya esta en su lugar")
                        #down.block = True
                else:
                    print("El plato de abajo no existe")
                    #down.block = True
                if right != None:
                    if right.color == rightOut.color:
                        print("El plato de derecha no es permutable")
                        right.block = True
                else:
                    print("El plato de derecha no existe")
                    #right.block = True
                #Media vez se obtienen lo perifericos, vamos a preguntar si se realiza el cambio alguno de los otroa
                #Platos quedara en su lugar

                if right.block == False:
                    if headInput.color == rightOut.color:
                        #Significa que si es permutable
                        if 2*float(headInput.flip) > float(headInput.swap):

                            print("SE REALIZA EL SWAP HACIA LA DERECHA")
                            instructions += addInstruction(instructions, True, instructionIndex, headInput.swap,
                                                           totalAcumulado)
                            # ################################################## Cambio a la derecha
                            operation(inputMatrix, True, index, inverseColor(headInput.color), index + 1,
                                      headInput.color)
                            diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            index += 1
                            # Actualizar Head, ya que es una copia de la anterior
                            headInput = inputMatrix.head
                            headOutput = outputMatrix.head
                            for i in range(index):
                                headInput = headInput.next
                                headOutput = headOutput.next

                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            print()
                            totalAcumulado += headInput.swap


                        elif down.block == False:
                            if downOut.color == headInput.color:
                                if 2 * float(headInput.flip) > float(headInput.swap):
                                    print("SE REALIZA EL SWAP HACIA LA ABAJO")
                                    instructions += addInstruction(instructions, True, instructionIndex, headInput.swap,
                                                                   totalAcumulado)
                                    # ################################################## Cambio abajo
                                    operation(inputMatrix, True, index, inverseColor(headInput.color),
                                              index + int(inputMatrix.columns),
                                              headInput.color)
                                    diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                                    print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                                    print(headInput.index, headOutput.index)
                                    index += 1

                                    headInput = inputMatrix.head
                                    headOutput = outputMatrix.head
                                    for i in range(index):
                                        headInput = headInput.next
                                        headOutput = headOutput.next

                                    print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                                    print(headInput.index, headOutput.index)
                                    print()
                                    totalAcumulado += headInput.swap
                                else:
                                    print("FLIP")
                                    instructions += addInstruction(instructions, False, instructionIndex,
                                                                   headInput.flip,
                                                                   totalAcumulado)
                                    # ################################################## FLIP
                                    operation(inputMatrix, False, index, inverseColor(headInput.color), index + 1,
                                              headInput.color)
                                    diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                                    print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                                    print(headInput.index, headOutput.index)
                                    index += 1
                                    # Actualizar Head, ya que es una copia de la anterior
                                    headInput = inputMatrix.head
                                    headOutput = outputMatrix.head
                                    for i in range(index):
                                        headInput = headInput.next
                                        headOutput = headOutput.next

                                    print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                                    print(headInput.index, headOutput.index)
                                    print()
                                    totalAcumulado += headInput.flip
                            else:
                                print("FLIP")
                                instructions += addInstruction(instructions, False, instructionIndex, headInput.flip,
                                                               totalAcumulado)
                                # ################################################## FLIP
                                operation(inputMatrix, False, index, inverseColor(headInput.color), index + 1,
                                          headInput.color)
                                diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                                print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                                print(headInput.index, headOutput.index)
                                index += 1
                                # Actualizar Head, ya que es una copia de la anterior
                                headInput = inputMatrix.head
                                headOutput = outputMatrix.head
                                for i in range(index):
                                    headInput = headInput.next
                                    headOutput = headOutput.next

                                print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                                print(headInput.index, headOutput.index)
                                print()
                                totalAcumulado += headInput.flip

                        else:
                            print("FLIP")
                            instructions += addInstruction(instructions, False, instructionIndex, headInput.flip,
                                                           totalAcumulado)
                            # ################################################## FLIP
                            operation(inputMatrix, False, index, inverseColor(headInput.color), index + 1,
                                      headInput.color)
                            diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            index += 1
                            # Actualizar Head, ya que es una copia de la anterior
                            headInput = inputMatrix.head
                            headOutput = outputMatrix.head
                            for i in range(index):
                                headInput = headInput.next
                                headOutput = headOutput.next

                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            print()
                            totalAcumulado += headInput.flip
                    else:
                        print("FLIP")
                        instructions += addInstruction(instructions, False, instructionIndex, headInput.flip,
                                                       totalAcumulado)
                        # ################################################## FLIP
                        operation(inputMatrix, False, index, inverseColor(headInput.color), index + 1,
                                  headInput.color)
                        diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        index += 1
                        # Actualizar Head, ya que es una copia de la anterior
                        headInput = inputMatrix.head
                        headOutput = outputMatrix.head
                        for i in range(index):
                            headInput = headInput.next
                            headOutput = headOutput.next

                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        print()
                        totalAcumulado += headInput.flip

                elif down.block == False:
                    if downOut.color == headInput.color:
                        if 2 * float(headInput.flip) > float(headInput.swap):
                            print("SE REALIZA EL SWAP HACIA LA ABAJO")
                            instructions += addInstruction(instructions, True, instructionIndex, headInput.swap,
                                                           totalAcumulado)
                            # ################################################## Cambio abajo
                            operation(inputMatrix, True, index, inverseColor(headInput.color),
                                      index + int(inputMatrix.columns),
                                      headInput.color)
                            diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            index += 1

                            headInput = inputMatrix.head
                            headOutput = outputMatrix.head
                            for i in range(index):
                                headInput = headInput.next
                                headOutput = headOutput.next

                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            print()
                            totalAcumulado += headInput.swap
                        else:
                            print("FLIP")
                            instructions += addInstruction(instructions, False, instructionIndex, headInput.flip,
                                                           totalAcumulado)
                            # ################################################## FLIP
                            operation(inputMatrix, False, index, inverseColor(headInput.color), index + 1,
                                      headInput.color)
                            diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)

                            # Actualizar Head, ya que es una copia de la anterior
                            headInput = inputMatrix.head
                            headOutput = outputMatrix.head
                            for i in range(index):
                                headInput = headInput.next
                                headOutput = headOutput.next

                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            print()
                            totalAcumulado += headInput.flip
                    else:


                        print("FLIP")
                        instructions += addInstruction(instructions, False, instructionIndex, headInput.flip,
                                                       totalAcumulado)
                        # ################################################## FLIP
                        operation(inputMatrix, False, index, inverseColor(headInput.color), index + 1,
                                  headInput.color)
                        diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        index += 1
                        # Actualizar Head, ya que es una copia de la anterior
                        headInput = inputMatrix.head
                        headOutput = outputMatrix.head
                        for i in range(index):
                            headInput = headInput.next
                            headOutput = headOutput.next

                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        print()
                        totalAcumulado += headInput.flip

                else:
                    print("FLIP")
                    instructions += addInstruction(instructions, False, instructionIndex, headInput.flip,
                                                   totalAcumulado)
                    # ################################################## FLIP
                    operation(inputMatrix, False, index, inverseColor(headInput.color), index + 1,
                              headInput.color)
                    diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                    print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                    print(headInput.index, headOutput.index)
                    index += 1
                    # Actualizar Head, ya que es una copia de la anterior
                    headInput = inputMatrix.head
                    headOutput = outputMatrix.head
                    for i in range(index):
                        headInput = headInput.next
                        headOutput = headOutput.next

                    print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                    print(headInput.index, headOutput.index)
                    print()
                    totalAcumulado += headInput.flip


        else: #Significa que son iguales
            if headInput.color != headOutput.color:
                # First, the robot need to watch the perifericals
                up, down, left, right = inputMatrix.orthogonalNodes(headInput)
                upOut, downOut, leftOut, rightOut = outputMatrix.orthogonalNodes(headInput)
                # Verification process

                # Compare the Perifericals with headOutPut

                if down != None:
                    if down.color == downOut.color:
                        print("El plato de abajo ya esta en su lugar")
                        down.block = True
                else:
                    print("El plato de abajo no existe")
                    #down.block = True
                if right != None:
                    if right.color == rightOut.color:
                        print("El plato de derecha no es permutable")
                        right.block = True
                else:
                    print("El plato de derecha no existe")
                    #right.block = True

                # Termina proceso de Bloqueo de Nodos

                # Primero verificará a la derecha (Esto para facilitar el potencial cambio)
                if right.block == False:  # Si no esta bloqueado
                    # Si se realiza este Swap, el siguiente nodo quedara en su lugar?
                    if rightOut.color == headInput.color:  # Tiene el color que necesito?
                        print("SE REALIZA EL SWAP HACIA LA DERECHA")
                        instructions += addInstruction(instructions, True, instructionIndex, headInput.swap, totalAcumulado)
                        # ################################################## Cambio a la derecha
                        operation(inputMatrix, True, index, inverseColor(headInput.color), index + 1, headInput.color)
                        diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        index += 1
                        #Actualizar Head, ya que es una copia de la anterior
                        headInput = inputMatrix.head
                        headOutput = outputMatrix.head
                        for i in range(index):
                            headInput = headInput.next
                            headOutput = headOutput.next

                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        print()
                        totalAcumulado += headInput.swap


                    elif down.block == False:
                        if downOut.color == headInput.color:
                            print("SE REALIZA EL SWAP HACIA LA ABAJO")
                            instructions += addInstruction(instructions, True, instructionIndex, headInput.swap,
                                                           totalAcumulado)
                            # ################################################## Cambio abajo
                            operation(inputMatrix, True, index, inverseColor(headInput.color),
                                      index + int(inputMatrix.columns),
                                      headInput.color)
                            diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            index += 1

                            headInput = inputMatrix.head
                            headOutput = outputMatrix.head
                            for i in range(index):
                                headInput = headInput.next
                                headOutput = headOutput.next

                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            print()
                            totalAcumulado += headInput.swap
                        else:
                            print("FLIP")
                            instructions += addInstruction(instructions, False, instructionIndex, headInput.flip,
                                                           totalAcumulado)
                            # ################################################## FLIP
                            operation(inputMatrix, False, index, inverseColor(headInput.color), index + 1,
                                      headInput.color)
                            diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            index += 1
                            # Actualizar Head, ya que es una copia de la anterior
                            headInput = inputMatrix.head
                            headOutput = outputMatrix.head
                            for i in range(index):
                                headInput = headInput.next
                                headOutput = headOutput.next

                            print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                            print(headInput.index, headOutput.index)
                            print()
                            totalAcumulado += headInput.flip
                    else:
                        print("FLIP")
                        instructions += addInstruction(instructions, False, instructionIndex, headInput.flip,
                                                       totalAcumulado)
                        # ################################################## FLIP
                        operation(inputMatrix, False, index, inverseColor(headInput.color), index + 1,
                                  headInput.color)
                        diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        index += 1
                        # Actualizar Head, ya que es una copia de la anterior
                        headInput = inputMatrix.head
                        headOutput = outputMatrix.head
                        for i in range(index):
                            headInput = headInput.next
                            headOutput = headOutput.next

                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        print()
                        totalAcumulado += headInput.flip

                elif down.block == False:

                    # Si se realiza este Swap, el siguiente nodo quedara en su lugar?
                    if downOut.color == headInput.color:
                        print("SE REALIZA EL SWAP HACIA LA ABAJO")
                        instructions += addInstruction(instructions, True, instructionIndex, headInput.swap,
                                                       totalAcumulado)
                        # ################################################## Cambio abajo
                        operation(inputMatrix, True, index, inverseColor(headInput.color),
                                  index + int(inputMatrix.columns),
                                  headInput.color)
                        diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        index += 1

                        headInput = inputMatrix.head
                        headOutput = outputMatrix.head
                        for i in range(index):
                            headInput = headInput.next
                            headOutput = headOutput.next

                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        print()
                        totalAcumulado += headInput.swap
                    else:
                        print("FLIP")
                        instructions += addInstruction(instructions, False, instructionIndex, headInput.flip,
                                                       totalAcumulado)
                        # ################################################## FLIP
                        operation(inputMatrix, False, index, inverseColor(headInput.color), index + 1,
                                  headInput.color)
                        diseno.append(inputMatrix, str(inputMatrix.index), str(inputMatrix.code))
                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        index += 1
                        # Actualizar Head, ya que es una copia de la anterior
                        headInput = inputMatrix.head
                        headOutput = outputMatrix.head
                        for i in range(index):
                            headInput = headInput.next
                            headOutput = headOutput.next

                        print("HEAD INPUT INDEX, HEAD OUTPUT INDEX")
                        print(headInput.index, headOutput.index)
                        print()
                        totalAcumulado += headInput.flip

            else:

                print(" Este Nodo ya se encuentra en su lugar ")
                headOutput = headOutput.next
                headInput = headInput.next
                index += 1
                instructionIndex += 1

    #Generar Archivos (Graphviz e Instrucciones)

    graphDirect('AnalisisPiso' + inputMatrix.code + 'to' + outputMatrix.code, diseno)
    generateArchive(instructions, inputMatrix.code, outputMatrix.code)
    print("------------------------------------")
    print("------El Costo Minimo es de "+ str(totalAcumulado))






