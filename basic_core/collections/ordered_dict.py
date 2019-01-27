# A Python program to demonstrate working of OrderedDict
from collections import OrderedDict

print("This is a Dict:\n")
d = {}
d['b'] = 2
d['c'] = 3
d['a'] = 1
d['d'] = 4
d.pop('c')
d['c'] = 3
for key, value in d.items():
	print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
	print(key, value)



# A Python program to demonstrate working of key
# value change in OrderedDict
from collections import OrderedDict

print("Before:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
	print(key, value)

print("\nAfter:\n")
od['c'] = 5
for key, value in od.items():
	print(key, value)




# A Python program to demonstrate working of deletion
# re-inserion in OrderedDict
from collections import OrderedDict

print("Before deleting:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
	print(key, value)

print("\nAfter deleting:\n")
od.pop('c')
for key, value in od.items():
	print(key, value)

print("\nAfter re-inserting:\n")
od['c'] = 3
for key, value in od.items():
	print(key, value)
