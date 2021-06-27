"""
binary tree - legaturi la doua noduri

            0
        0       0
      0   0   0   0
    0
  0

BT => Binary Search Tree = BST
   => Heap Search

BST: O(longN)
 7 4 3 9 8 12 13
            7
        4       9
      3       8   12
                     13
Pre-Order
    visit
    go left
    go right

Post-Order
    go left
    go right
    visit

In-Order
    go left
    visit
    go right

"""


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BTree:

    def __init__(self) -> None:
        self.root = None
    
    def addNode(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
            return
        current = self.root

        while current != None:
            if data < current.data:
                if current.left != None:
                    current = current.left
                else:
                    current.left = newNode
                    break

            elif data > current.data:
                if current.right != None:
                    current = current.right
                else:
                    current.right = newNode
                    break

    def InOder(self):
        self.InOrderRec(self.root)
    
    def InOrderRec(self, node):
        if node == None:
            return

        self.InOrderRec(node.left)
        print(node.data)
        self.InOrderRec(node.right)

bst = BTree()
#  7 4 3 9 8 12 13
bst.addNode(7)
bst.addNode(4)
bst.addNode(3)
bst.addNode(9)
bst.addNode(8)
bst.addNode(12)
bst.addNode(13)

bst.InOder()

