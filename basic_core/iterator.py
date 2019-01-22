class IterateNatural:

    def __init__(self, start=0, limit = 30):
        self.value = start
        self.limit = limit

    def __next__(self):
        if self.value == self.limit:
	        raise StopIteration
        value = self.value
        self.value = self.value +1
        return value
    def __iter__(self):
        return self

for value in IterateNatural(limit=100,start=50):
    print(value)