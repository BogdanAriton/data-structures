class MyClass:
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return 'clasa Mea'

instMyClass = MyClass()

myhash = { 1 : "value", "key1" : "value1", 2.3 : "value2", 'a' : "value3",  instMyClass : "value4", "key5" : "value5"}

"""
    size = 6
    key => 
    hash => key => 1423423 % 6 => 1 -> pos = value5
"""

print(myhash)
