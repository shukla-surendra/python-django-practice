#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:10:32 2019

@author: surendra
"""

class Stack:
    
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return self.stack == []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def size_stack1(self):
        return len(self.stack)

stack = Stack()
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.size_stack1()) #if no parenthesis then throw bound method error
print("Popped:", stack.pop())