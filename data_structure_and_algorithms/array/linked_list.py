#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 23:46:04 2019

@author: surendra
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    # O(1)
    def insertStart(self, data):
        self.size +=1
        node = Node(data)
        if self.head is not None:
            node.next_node = self.head
        self.head = node
    '''
    def traverse(self):
        next_node = self.head
        for i in range(self.size):
            print(next_node.data)
            next_node = next_node.next_node
    '''
    # O(N)
    def traverse(self):
        next_node = self.head
        while next_node is not None:
            print(next_node.data)
            next_node = next_node.next_node
            
    #size is a built in method never use it
    def get_linked_list_size(self):
        return self.size
    
    # O(N)
    def size2(self):
        size = 0
        next_node = self.head
        while next_node is not None:
            size += 1
            next_node = next_node.next_node

# application 
            
linkedlist = LinkedList()
linkedlist.insertStart(10)
linkedlist.insertStart(20)
linkedlist.insertStart(30)
linkedlist.insertStart(40)
linkedlist.insertStart(50)
linkedlist.insertStart(60)
linkedlist.traverse()
            