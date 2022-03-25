from colorama import Fore, Back, Style

class militaryUnit:
    def __init__(self, name: str, rows: int, columns: int, militaryUnits, swap: float, patrones, counter: int, next, prev) -> None:
        self.name:  str = name
        self.rows: float = rows
        self.columns: int = columns
        #self.flip: float = flip
        self.swap: swap = swap
        self.patrones = patrones
        self.counter: int = counter
        self.next = next
        self.prev = prev

class listaCiudades:
    def __init__(self, head=None) -> None:
        self.head = head
        self.tail = None

    def append(self, name, rows, columns, flip, swap, patrones, counter):
        if self.head == None:
            #firstNode = Piso(name, rows, columns, flip, swap, patrones, counter, None, None)
            print(name + '->', end='')
            #self.head = firstNode
        elif self.head != None:
            copiaHead = self.head
            while copiaHead.next != None:
                copiaHead = copiaHead.next
                copiaHead.prev = copiaHead
            #newNode = Piso(name, rows, columns, flip, swap, patrones, counter, None, copiaHead)
            #copiaHead.next = newNode
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
        while head != None:
            print(Fore.BLACK)
            print(Back.BLUE, head.name, end='->')
            print()
            print(Style.RESET_ALL)
            head = head.next
    def length(self):
        head = self.head
        counter = 0
        while head != None:
            counter += 1
            head = head.next
        return counter
