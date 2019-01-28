'''
The frozenset() method returns an immutable frozenset object initialized with elements from the given iterable.
frozenset([iterable])
'''
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())