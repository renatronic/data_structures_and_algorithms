'''
the only difference between Node2 and Node is the presence of a
a prev_node property ot the class, as well as the .get_prev_node() 
and .set_prev_node() methods in the last one.
'''

class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
        
    def get_next_node(self):
        return self.next_node
    
    def get_prev_node(self):  # access previous
        return self.prev_node
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def set_next_node(self, next_node):
        self.next_node = next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node
        
    def increment_value(self):
        self.value = self.value + 1