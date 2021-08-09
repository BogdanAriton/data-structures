class Node:
    def __init__(self, data) -> None:
        __data = data
        nodesList = { '', Node }
    


"""
adjacency matrix

    [1, 2, 3, 4, 5, 6, 7, 8, 9]

     1 2 3 4 5 6 7 8 9
   1 0 1 0 0 0 1 1 0 1
   2 1 0 1 0 0 0 0 1 0
   3 0 1 0 0 0 0 0 0 0
   4 0 1 0 0 0 0 0 0 0
   5 0 1 0 0 0 0 0 0 0
   6 0 1 0 0 0 0 0 0 0
   7 0 1 0 0 0 0 0 0 0
   8 0 1 0 0 0 0 0 0 0
   9 0 1 0 0 0 0 0 0 0 

   a = [][]
      a[5][2] - O(1) - constant time
      Space complexity - O(n^2)

adjacency list
    1 -> [2][][][][] - O(n) - linear time
    2 -> [1][]

"""

"""
Applicabilitate:

     1 2 3 4 5 6 7 8
   1 T T 0 0 0 0 0 0
   2 0 x 0 0 0 0 0 0
   3 0 x x 0 0 0 0 0
   4 0 0 0 0 0 0 0 0
   5 0 0 0 0 0 0 0 0
   6 0 0 0 0 0 0 0 0
   7 0 0 0 0 0 0 0 0
   8 0 0 0 0 0 0 0 0

   Casuta - nodul:
    Info:
        Atacata - de cine - un arbore the atacuri
        Next move - este un arbore


    words: banana
    

"""
