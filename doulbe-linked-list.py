
class DoubleLinked:
    
    class Node:
        def __init__(self, data, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev
    
    tail = Node(None, None, None)
    head = Node(None, tail, None)
    tail.prev = head
    size = 0

    def append(self, value):

        if self.size == 0:
            self.head.data = value
            self.size += 1
            return
        
        newNode = self.Node(value)
        newNode.next = self.tail
        newNode.prev = self.tail.prev
        self.tail.prev.next = newNode # 
        self.tail.prev = newNode
        self.size += 1
    
    def print(self):
        
        current = self.head
        while current != self.tail:
            print(current.data)
            current = current.next

mylinked = DoubleLinked()
mylinked.append(1)
mylinked.append(2)
mylinked.append(3)
mylinked.append(4)

mylinked.print()