class MyClass(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        

test = MyClass("Name", "Age")
# test.hi = "Hello" # can't set because hi is not in __slot__ list
print("test")