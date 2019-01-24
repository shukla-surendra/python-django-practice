'''
  # DO NOT EVER HAS SCRIPT NAME AS INBUILD MODULE NAME
'''
import random

'''
   Randrange(Stop)
'''
#Python Randrange(Stop) Function.
# If “r” is a random number, then its value will lie in the range 0 <= r < stop. # random.randrange(stop)
print(random.randrange(10))

'''
   Randrange(Start, Stop[, Step])
   
   If “r” is a random number, then its value will lie in the range start <= r < stop.

# Syntax.

random.randrange(start, stop[, step])
[start] – It is the base value of the range and may fall in the selection.

[stop] – It is the boundary value of the range excluding from the selection.

[step] – It is the value with which the number is incremented. The default value is 0 if not passed.

'''

# Generate random integer in the interval [4,10]
print(random.randrange(4,11))

# Generate random integer in [4,10] with increment of 3
print(random.randrange(4, 11, 3))

# Generate random even numbers between 2 and 24
print(random.randrange(2, 25, 2))

# Generate random even numbers between 1 and 25
print(random.randrange(1, 26, 2))


'''
Random.Randint(Low, High) 

Purpose- The randint() function is one of many functions which handle random numbers. It has two parameters low and high and generates an integer between low and high (including both).

'''
# generationg random number from 0-9 9 times
iter = 0
while iter < 10:
 # Get random number in range 0 through 9.
 r = random.randint(0, 9)
 print(r)
 iter += 1
 
 '''
 Random.Choice(Seq) Function.
Purpose- The choice() function arbitrarily determines an element from the given sequence.

Note- A sequence in Python is the generic term for an ordered set like a list, tuple etc.
'''

# Generate a random string from the list of strings

print(random.choice( ['Python', 'C++', 'Java'] ))

# Generate a random number from the list [-1, 1, 3.5, 7, 15]

print(random.choice([-1, 1, 3.5, 9, 15]))

# Generate a random number from a uniformly distributed tuple

print(random.choice((1.1, -5, 6, 4, 7)))

# Generate a random char from a string

print(random.choice('Learn Python Programming'))

'''
Random.Shuffle(List) Function.
Purpose- The shuffle() function rearranges the items of a list in place so that they occur in a random order.

For shuffling, it uses the Fisher-Yates algorithm which has O(n) complexity. It starts by iterating the last element in the array to the first entry, then swap each entry with an entry at a random index below it
'''

# How to randomize a list in Python?
from random import shuffle

mylist = [11,21,31,41,51]
shuffle(mylist)

print(mylist)

'''

Random.Sample(Collection, Random List Length) Function.
Purpose- The sample() function randomly selects N items from a given collection (list, tuple, string, dictionary, set) and returns them as a list.

It works by sampling the items without replacement. It means a single element from the sequence can appear in the resultant list at most once.

'''

# How to use sample() in Python?
from random import sample

# Select any three chars from a string

print(sample('Python',3))

# Randomly select a tuple of three elements from a base tuple

print(sample((21, 12, -31, 24, 65, 16.3), 3))

# Randomly select a list of three elements from a base list

print(sample([11, 12, 13, 14, -11, -12, -13, -14], 3))

# Randomly select a subset of size three from a given set of numbers

print(sample({110, 120, 130, 140}, 3))

# Randomly select a subset of size three from a given set of strings

print(sample({'Python', 'C++', 'Java', 'Go'}, 3))

'''
Random.Random() Function.
Purpose- It selects the next random floating point number from the range [0.0, 1.0]. It is a semi-open range as the random function will always return a decimal no. less than its upper bound. However, it may return 0.

'''

# Generate a floating-point pseudo-random number between 0 and 1.

print(random.random())
'''
Random.Uniform(Lower, Upper) Function.
Purpose- It is an extension of the random() function. In this, you can specify the lower and upper bounds to generate a random number other than the ones between 0 and 1.
'''

# How to uniform() method to generate floating-point random numbers?
import random

lower = 111; upper = 999
random_float = random.uniform(lower, upper)
print(random_float)


# Generate a floating-point random number with fixed precision
import random

lower = 1.0; upper = 2.0; fixed_precision = 2

random_float = random.uniform(lower, upper)

print(round(random_float, fixed_precision))