from colorama import Fore, Back, Style

class unit:
    def __init__(self, posY, posX, power, next, prev) -> None:
        self.posY: int = posY
        self.posX: int = posX
        self.power: float = power
        self.next = next
        self.prev = prev

class militaryUnits:
    def __init__(self, head=None) -> None:
        self.head = head
        self.tail = None

    def append(self, posY, posX, power):
        if self.head == None:
            firstNode = unit(posY, posX, power, None, None)
            print(str(power) + '->', end='')
            self.head = firstNode
        elif self.head != None:
            copiaHead = self.head
            while copiaHead.next != None:
                copiaHead = copiaHead.next
                copiaHead.prev = copiaHead
            newNode = unit(posY, posX, power, None, copiaHead)
            copiaHead.next = newNode
            print(str(power) + '->', end='')
        pass
    def pop(self):
        pass
    #position
    def delete(self):
        pass
    def search(self, posY, posX):
        current_node = self.head
        while current_node is not None:
            if int(current_node.posY) == int(posY) and int(current_node.posX) == int(posX):
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
            print(head.power, head.posX, head.posY ,end='->')
            head = head.next
    def length(self):
        head = self.head
        counter = 0
        while head != None:
            counter += 1
            head = head.next
        return counter

def main():
    units = militaryUnits()
    units.append(1,2,3)
    print()
    units.print()
    units.append(1,3,4)
    print()
    units.print()

    print(units.search(1,2))
if __name__ == '__main__':
    main()