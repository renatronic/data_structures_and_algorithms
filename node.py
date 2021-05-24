'''
This Node class can be used for both singly and doubly linked lists. The
only difference is that since a singly linked list is unidirectional, it
wouldn't need of a prev_node property on the class, as well as the 
.get_prev_node() and .set_prev_node() methods.
'''

class Node:
    def __init__(self, value, next_node=None, prev_node=None):  # next_node coud be also named link_node and it's optional
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
        
    def get_next_node(self): # access next
        return self.next_node
    
    def get_prev_node(self):  # access previous
        return self.prev_node
    
    def get_value(self): # access value
        return self.value
    
    def set_value(self, value):
        self.value = value

    def set_next_node(self, next_node):
        self.next_node = next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node
        
    def increment_value(self):
        self.value += 1