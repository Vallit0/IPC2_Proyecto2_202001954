from colorama import Fore, Back, Style

class Drone:
         #Nombre, R, C, F, S, PATRONES (Sera una lista de listas)
    def __init__(self, name: str, type: str, capacity: int, next, prev) -> None:
        self.name:  str = name
        self.type: float = type
        self.capacity: int = capacity
        self.next = next
        self.prev = prev

class listaDrones:
    def __init__(self, head=None) -> None:
        self.head = head
        self.tail = None

    def append(self, name, type, capacity):
        if self.head == None:
            firstNode = Drone(name, type, capacity, None, None)
            print(name + '->', end='')
            self.head = firstNode
        elif self.head != None:
            copiaHead = self.head
            while copiaHead.next != None:
                copiaHead = copiaHead.next
                copiaHead.prev = copiaHead
            newNode = Drone(name, type, capacity, None, copiaHead)
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
        while head != None:
            print(Fore.BLACK)
            print(Back.BLUE, head.name, end='->')
            print()
            print(Style.RESET_ALL)
            head = head.next
