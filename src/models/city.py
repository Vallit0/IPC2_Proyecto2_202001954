from colorama import Fore, Back, Style

class City:
    def __init__(self, matrix, name: str, rows: int, columns: int, counter: int, next, prev) -> None:
        self.matrix = matrix
        self.name:  str = name
        self.rows: float = rows
        self.columns: int = columns
        self.drones = None
        self.counter: int = counter
        self.next = next
        self.prev = prev

class listaCiudades:
    def __init__(self, head=None) -> None:
        self.head = head
        self.tail = None

    def append(self, matrix, name, rows, columns, counter):
        if self.head == None:
            firstNode = City(matrix, name, rows, columns,counter, None, None)
            print(name + '->', end='')
            firstNode.counter = 1
            self.head = firstNode
        elif self.head != None:
            copiaHead = self.head
            cont = 0
            while copiaHead.next != None:
                cont += 1
                copiaHead = copiaHead.next
                copiaHead.prev = copiaHead
            newNode = City(matrix, name, rows, columns,counter, None, copiaHead)
            newNode.counter = cont
            copiaHead.next = newNode
            print(name + '->', end='')
        pass
    def pop(self):
        pass
    #position
    def delete(self):
        pass
    def search(self, name):
        current_node = self.head
        while current_node is not None:
            if current_node.name == name:
                return current_node
            current_node = current_node.next
        return False
        pass
    def searchByIndex(self, index):
        current_node = self.head
        while current_node is not None:
            if int(current_node.counter) == int(index):
                return current_node
            current_node = current_node.next
        return False
        pass
    def isIn(self,name) -> bool:
        current_node = self.head
        while current_node is not None:
            if current_node.name == name:
                return True
            current_node = current_node.next
        return False
    def print(self):
        head = self.head
        counter = 0
        while head != None:
            counter += 1
            print(counter, '. ', head.name, end='->')
            print()
            print(Style.RESET_ALL)
            head = head.next
    def addDrones(self, drones):
        head = self.head
        while head != None:
            head.drones = drones
            head = head.next









