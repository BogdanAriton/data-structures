# Overview

Learning python by understanding data-structures and common algorithms.

# Outline
1. General ideas about the language and what you can do with it
2. IDE and setup
3. Hello world with python
4. Importing "from" "as"
5. Multiple files (modules)
7. Conditional statements (if)
6. Data structures
    1. Lists - [] - array [1, 2, 3]
    2. Tuples - (1, "ceva", 2.7) - immutable (nu se modifica o data definit ramane asa)
    3. Dictionary - {1 : "unu", 2 : "doi"}
    4. Sets - {"1", "2", "3"}
    Teorie:
    5. Linked list
    6. Double Linked list
       queue: 1| 2| 3| 4| 5| 6| - FIFO - push_back/push, front, pop/pop_front - O(1) - while myQ is not empty - pop
       priority queue 5| 1| 2| 3|
       double ended queue
       stack - LIFO - push/push_back, back, pop/pop_back
            ___
            ___
            ___
            ___
            ___

    7. hash table - [1, 2, 3, 4, 5] - functie de hashing - 
                             444
        hash(valoare):
            x = n % valoare -> 2132141 -> pus intr-un tabel virtual care reprezinta pozitia acestei valori
        acest numar unic este folosit sa indentifici o valoare din sir (e ca un CNP)
        O(1) orice cautare de elemnt este constant time 
        Linked Lists = [4, 444] - O(n)

    8. arbori (binari, .. )
    9. graphs !

7. Data types - str, float, int, list, dict, tuple, set, double, ...
8. Iterations (for, while)
9. Functions
    1. Function arguments def fct(param: int = 0)
    2. Function calls - var = fct(..)
    3. Recursion - faptul ca o functie se cheama pe ea insasi
10. Strings - concat (+), ...
11. Classes and objects - Class Def: "User Defined Data Type", Obj = Instanta unei Clase ()
12. Collections
13. Iter-tools
14. Lambda Functions
15. Exceptions and errors
16. Logging
17. JSON - orice clasa din python se poate serializa intr-un json - 
    { 
        "nume" : "gheorghe",
        "lista" : 
        [
            "elem1" : "valoare",
            "elem2" : "valoare"
        ]
    }
    FAST API, Flask

18. Random numbers - UUIDs - 21yug32uy 32uy4g12u 12giu12g8
19. Decorators - @setter, @getter, @classmemeber, @static, @cache - tu poti sa ai o functie care poate face ceva pentru alte functii
    - cum aveam fibonacii poti face o functie care pastreza numerele de dinainte de calcul ca sa poti face calculul automat = @cache
    from functools import cache

20. Generators - pattern (genereaza obiecte in functie de ce nevoie ai - factory)
21. Threading vs multiprocessing (CUDA - procesare pe placa grafica)
    1. Multi-threading
    2. Multiprocessing

22. Shallow vs deep copying
23. The asterisk (*) operator - fct(*, a = 5, b) ... fct(5)
24. Context Managers

Frameworks de python:
25. Flask - Web Framework
26. Pandas - excel (csv) manipulation
27. SQL Alchemy ORM
28. FAST API - Rest Framework
29. Django