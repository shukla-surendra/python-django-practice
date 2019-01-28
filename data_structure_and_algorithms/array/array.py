#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:19:49 2019

@author: surendra
"""

numbers = [2,3,200,4,9] 

# random access O(1)
#print(numbers[2])

for value in numbers:
    print(value)
    
# assigning different type of value i list

#numbers[3] = "Surendra"
    
for i in range(len(numbers)):
    print(numbers[i])
    
# slicing numbers[start:stop:step]
#print(numbers[:])
#print(numbers[::-1])
'''    
linear serach
O(N)
'''
maximum_number = numbers[0]
for num in numbers:
    if num > maximum_number:
        maximum_number = num

print(maximum_number)

num = 5
num +=1
print(num) 
