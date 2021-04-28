# An implementation of linked list
# The linked list object will hold in memory the elements added
# Each element will hold a pointer to the next one
# Actions on the list:
#       append - will at an element at the end
#       addNodeAt - will add an element at a certain position
#       getValueAt - will return the data from an element
#       reverse - will update the list with the order reversed
#       various other actions can be added

class linkList():
    class element():
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next

    head = None
    size = 0

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def addNodeAt(self, data, at):
        if self.isEmpty():
            self.append(data)
            return

        if at < 0 or at >= self.getSize():
            return

        if at == 0:
            self.addFirst(data)
            return
        
        if at == self.getSize()-1:
            self.append(data)
            return

        index = 0
        node = self.head
        while node.next != None:
            if index == at-1: # -1 because we update next element
                nextElement = node.next
                node.next = self.element(data, nextElement)
                self.size += 1
                return
            node = node.next
            index += 1
    
    def getValueAt(self, at):
        if self.isEmpty():
            return None
        
        index = 0
        elem = self.head
        while elem.next != None:
            if index == at:
                return elem.data
            elem = elem.next

    def addFirst(self, data):
        if self.isEmpty():
            self.append(data)
        else:
            self.head = self.element(data, self.head)

    def removeNodeAt(self, at):
        pass

    def append(self, data):
        if self.isEmpty():
            self.head = self.element(data, None)
        else:
            elem = self.head
            while elem.next != None: # O(n)
                elem = elem.next
            elem.next = self.element(data, None)
        self.size += 1

    def reverse(self):
        if self.isEmpty():
            return # nothing to reverse
        
        current = self.head
        temp = None
        nextElem = None
        
        while current != None:
            nextElem = current.next # will hold the next element
            current.next = temp # next element will be replace by temp list
            temp = current # temp holds the new elements
            current = nextElem # replace element with the next one in the original list

        self.head = prevElem

def printLList(lList):
    if lList.isEmpty():
        return
    
    elem = lList.head
    i = 0
    while elem != None:
        print(elem.data, i)
        i += 1
        elem = elem.next

lList = linkList()
lList.addNodeAt(0, 0)
lList.append(1)
lList.append(2)
lList.append(3)

# printLList(lList)

lList.reverse()
printLList(lList)