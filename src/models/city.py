from colorama import Fore, Back, Style

class City:
         #Nombre, R, C, F, S, PATRONES (Sera una lista de listas)
    def __init__(self, name: str, rows: int, columns: int, counter: int, next, prev) -> None:
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

    def append(self, name, rows, columns, counter):
        if self.head == None:
            firstNode = City(name, rows, columns,counter, None, None)
            print(name + '->', end='')
            self.head = firstNode
        elif self.head != None:
            copiaHead = self.head
            while copiaHead.next != None:
                copiaHead = copiaHead.next
                copiaHead.prev = copiaHead
            newNode = City(name, rows, columns,counter, None, copiaHead)
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
            print(Fore.BLACK)
            counter += 1
            print(Back.BLUE, counter, '. ', head.name, end='->')
            print()
            print(Style.RESET_ALL)
            head = head.next
    def addDrones(self, drones):
        head = self.head
        while head != None:
            head.drones = drones
            head = head.next





