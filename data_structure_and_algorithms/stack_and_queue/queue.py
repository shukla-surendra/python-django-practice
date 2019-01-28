#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:44:13 2019

@author: surendra
"""

class Queue:
    
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return self.queue == []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        return self.queue[0]
    
    def size_queue(self):
        return len(self.queue)

q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.size_queue()) #if no parenthesis then throw bound method error
print("dequeue:", q.dequeue())