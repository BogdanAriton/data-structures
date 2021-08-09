'''
 
 BST - 
 x = 1 2 3 4 5 6 7 8 9 10 11 12 13
     0 1 2 3 4 5 6 7 8  9 10 11 12

 x[6] = 7
 merge sort - take the mid elm all the time and add it to the tree

                            7
                        3


    0 1 2 3 4 5 6
    8  9 10 11 12


            7
        3       9
    2      5 8      10

 7 9 3 5 8 10 2
 Balancing a BST
'''

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def preOrder(node):
    if not node:
        return
     
    print(node.data)
    preOrder(node.left)
    preOrder(node.right)
'''
    1 call = 1 2 3 4 5 6 7 8 9 10 11 12 13
    2 call - mid left = 1 2 3 4 5 6 7
    3 call - mid left = 1 2 3
    4 call - mid left = 1
    5 call - min left = None
    6 call - min left = None
'''
def addElemToBSTRecurs(array):
    
    if not array: # conditie de iesire
        return None

    mid = (len(array))//2
    node = Node(array[mid])
    print(array)

    node.left = addElemToBSTRecurs(array[:mid])
    node.right = addElemToBSTRecurs(array[mid+1:])

    return node



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
root = addElemToBSTRecurs(arr)
#print("PreOrder Traversal of constructed BST ")
preOrder(root)

#print(arr[1:1])