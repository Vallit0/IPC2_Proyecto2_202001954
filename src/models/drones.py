from colorama import Fore, Back, Style

class Drone:
         #Nombre, R, C, F, S, PATRONES (Sera una lista de listas)
    def __init__(self, name: str, type: str, capacity: int, next, prev) -> None:
        self.name:  str = name
        self.type: float = type
        self.capacity: int = capacity
        self.next = next
        self.prev = prev
        self.index = None
        self.counter = None

class droneList:
    def __init__(self, head=None) -> None:
        self.head = head
        self.tail = None
        self.counter = 0

    def append(self, name, type, capacity):
        self.counter += 1
        cont = 0
        if self.head == None:
            firstNode = Drone(name, type, capacity, None, None)
            firstNode.index = self.counter
            print(name + '->', end='')
            self.head = firstNode
        elif self.head != None:
            copiaHead = self.head
            while copiaHead.next != None:
                copiaHead = copiaHead.next
                copiaHead.prev = copiaHead
            newNode = Drone(name, type, capacity, None, copiaHead)
            newNode.index = self.counter
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
            print(head.name, end='->')
            head = head.next

    def printRescue(self):
        head = self.head
        while head != None:
            if head.type.upper() == 'CHAPINRESCUE':
                print(head.index, '.', head.name)
                print("|", end="")
                head = head.next
            else:
                head = head.next

    def printFigher(self):
        head = self.head
        while head != None:
            if head.type.upper() == 'CHAPINFIGHTER':
                print(head.counter, '.', head.name)
                head = head.next
            else:
                head = head.next
    def searchRescue(self):
        head = self.head
        counter = 0
        while head != None:
            if head.type.upper() == 'CHAPINRESCUE':
                counter += 1
                head = head.next
            else:
                head = head.next

        if counter == 0:
            return False
        else:
            return True
        pass
    def searchFighter(self):
        head = self.head
        counter = 0
        while head != None:
            if head.type.upper() == 'CHAPINFIGHTER':
                counter += 1
                head = head.next
            else:
                head = head.next

        if counter == 0:
            return False
        else:
            return True
        pass
    def printIndex(self):
        current_node = self.head
        while current_node is not None:
            print(str(current_node.index) + ' ' + str(current_node.name) + '->')
            current_node = current_node.next
    def searchByIndex(self, indice):
        current_node = self.head
        while current_node is not None:
            if current_node.index == int(indice):
                return current_node
            current_node = current_node.next
        return False
        pass

    pass

