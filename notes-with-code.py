'''
Complexitate - BigO Notation

O(1) - constant
O(n) - linear
O(logn) - logaritmic
O(n2) - quadratic
O(2n) - exponetial

'''

# O(1)
# x = 1
# if x == 3:
#     pass

# O(n)
# a = [1, 2, 3, 4, 5, 6, 7, 8 ]
# for i in a:
#     print(i)

# logn
# 1, 2, 3, 4, 5, 6, 7, 8 - sortat
# Cautam daca 6 este in lista
# Cautare liniara - verifica fiecare element
# Cautare divide and conquer
#   0  1  2  3  4  5  6  7
#   1, 2, 3, 4, 5, 6, 7, 8
# se imparte in juma

# def func(a):
#     if a > 10:
#         return a
#     return func(a+1)

# def funcX(a):
#     if a > 10:
#        return a
#     funcX(a+1)
#     funcX(a+2)
#     print(a)

#print(func(1))
# print(funcX(1))

# def fibonaci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonaci(n-1) + fibonaci(n-2)

# print(fibonaci(48))

from numpy import select


a = [1, 2, 3, 4, 5]
t = (1 , 2, 3, 4, 5)

# Lista simplu inlantuita
class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next
    
    def __repr__(self) -> str:
        return "data = " + str(self.data)

head = Node(1)
nod1 = Node(2)
nod2 = Node(3)
nod3 = Node(4)
nod4 = Node(5)

head.next = nod1
nod1.next = nod2
nod2.next = nod3
nod3.next = nod4

current = head
while current != None:
    print(current)
    current = current.next

# Lista dublu inlantuita
class NodeD:
    def __init__(self, data, next = None, prev = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
    
    def __repr__(self) -> str:
        return "data = " + str(self.data)

# Hash Tables
# are o function de hashing

class MyHashTable:
    def __init__(self) -> None:
        self.size = 20
        self.myArray = []
    
    def add(self, data):
        pass

    def get(self, data):
        pass

    def hash(self, data):
        return data % len(self.size)

x = "paco" % 20
y = "thrall" % 20
print(x)

d = {}
