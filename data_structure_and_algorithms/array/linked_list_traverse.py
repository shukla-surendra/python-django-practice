#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 00:10:52 2019

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

    # O(N)
    def traverse(self):
        next_node = self.head
        while next_node is not None:
            print(next_node.data)
            next_node = next_node.next_node
    '''   
    def insertAtEnd(self, data):
        self.size = self.size + 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self
        next_node = self.head
        while next_node is not None:
            if next_node.next_node is None:
                next_node.next_node = new_node
                break
            next_node = next_node.next_node
    '''
     # O(N)
    def insertAtEnd(self, data):
        self.size = self.size + 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        actual_node = self.head
        while actual_node.next_node is not None:
            actual_node = actual_node.next_node
        actual_node.next_node = new_node
        
        # O(N)
    def remove(self, data):
        if self.head is None:
            return
        self.size = self.size - 1
        current_node = self.head
        previous_node = None
        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node
        if previous_node == None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node

        #size is a built in method never use it
    def get_linked_list_size(self):
        return self.size
    
    

# application 
            
linkedlist = LinkedList()
linkedlist.insertAtEnd(10)
linkedlist.insertAtEnd(20)
linkedlist.insertAtEnd(30)
linkedlist.insertAtEnd(40)
linkedlist.insertAtEnd(50)
linkedlist.insertAtEnd(60)
linkedlist.traverse()
linkedlist.remove(60)
print(linkedlist.get_linked_list_size())
linkedlist.traverse()
            