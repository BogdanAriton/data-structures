"""
    Vrem gasim ce lagatura exista intre doua aeoroporturi

    Trebuie gasim o modalitate de a reprezenta graful
    Adjacency List

    A - B, G
    B - C
    C - E
    E - D
    D - F
    F - A, H, I
    G - H
    H - I
    I - E

Avem niste Noduri care se leaga de alte noduri

**kargs = pack de parametri care se unpack intr-un dictionar
*args = pack de param care se unpack intr-o lista

"""
from queue import LifoQueue

class Node:
    def __init__(self, name):
        self.name = name
        self.dest = {}

    def addDest(self, **dest): # { dest: {B: 6, G: 5} }
        for item in dest['dest']:
            self.dest[item] = dest['dest'][item]

def DFT(node, visited):
    if visited.get(node):
        return
    
    print(node.name)

    visited[node] = True
    for nodes in node.dest:
        DFT(nodes, visited)

"""
    node = a
    stack = [a: true]
    tempNode = B
    stack = [a: true, b: true]
    node = B

"""

        
A = Node("Otopeni")
B = Node("frankfurt")
C = Node("Los Angeles")
D = Node("Cluj")
E = Node("Brasov")
F = Node("Londra")
G = Node("New York")
H = Node("Paris")
I = Node("Dubai")

A.addDest(dest = {B: 6, G: 5})
B.addDest(dest = {C: 5})
C.addDest(dest = {E: 3})
D.addDest(dest = {F:2, B:1})
E.addDest(dest = {D: 2})
F.addDest(dest = {A: 2, H:3, I:3})
H.addDest(dest = {I: 4})
G.addDest(dest = {H: 4})
I.addDest(dest = {E: 2})

visited = {}
DFT(A, visited)
#print("Distanta de la ", A.name, " la ", B.name, " este: ", A.dest[B])

# Depth First Travesal - Parcurgere prin adancime
# stack - LIFO unde intra fiecare nod
# ne facem un dictionar pentru noduri vizitate
# facem munca pana cand stack-ul este gol
# Breath First Traversal - Parcurgere prin invecinare

