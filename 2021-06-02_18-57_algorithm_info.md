---
tags:
    - algorithms
    - data structures
    - big 0
---

# Algorithms
Note taken following this course: https://www.youtube.com/watch?v=8hly31xKli0

# Big O Notation
It's a definition of the complexity of an algorithm! :)
O - order of magnitude of complexity
O(1) - constant time
O(n) - linear time
O(log n) - logarithmic time - basically log2 of n + 1 = which reads: how many times we can divide n by 2


# Search algorithms:
1. Linear search - evaluates each value individually - O(n)
2. Binary search - can only work on a sorted array - much faster - O(logN) (or O(lnN))
    1. Iterative - simply move first and last based on the midpoint
    2. Recursive implementation:
        # recursive copy heavy
        def recursive_binary(myList, value):
            if len(myList) == 0:
                return False
            else:
                midpoint = (len(myList))//2
                if myList[midpoint] == value:
                    return True
                elif myList[midpoint] < value:
                    return recursive_binary(myList[midpoint+1:], value) 
                else:
                    return recursive_binary(myList[:midpoint], value)

        # recursive nested
        def recursive_binary_nested(myList, value):
            def recursive_inner(first, last):
                if first <= last:
                    middle = (first+last)//2
                    if myList[middle] == value:
                        return True
                    
                    if myList[middle] < value:
                        return recursive_inner(middle+1, last)
                    else:
                        return recursive_inner(first, middle - 1)
            return recursive_inner(0, len(myList)-1)
    3. Using the bisect module you can:
        - bisect() -
        - bisect_left()
        - bisect_right()
        - insort() - insert keeping the sorting order
        - insort_left()
        - insort_right()

        example:
            import bisect as bisect
            list = [1, 2, 3, 4, 5, 6, 8 , 9 , 11, 17, 20]
            index = bisect.bisect_right(list, 8)

            [1, 2, 3, 4, 5, 6, 8, 9, 11, 17, 20]
            [1, 2, 3, 4, 5, 6, 8, 9, 11, 17, 20]
            -> the index where the item should be in the list to the right of list[8] = position 7

    # note - recursions in python have a limit - normally this should not be reached, but just in case recursion should be avoided

3. Merge sort - [ 1 ] [ 2, 3] [ 45 ] [ 65 ] [ 324 ] [ 23 ] [ 43 ] [ 1212 ]
4. Insert sort - 
5. Bubble sort - [ 1, 2, 3, 45, 65, 324, 23, 43, 1212 ]
6. Selection sort [ 1, 2, 3, 45, 65, 324, 23, 43, 1212 ]
7. 