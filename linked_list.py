from node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
  
    def get_head_node(self):
        return self.head_node
  
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node) # next your new node to the current head node to keep the connection to the following nodes
        self.head_node = new_node
    
    def stringify_list(self):
        string_list = ''
        current_node = self.get_head_node()
        while current_node: # using a while loop and Node's get_next_node() to traverse the list, beginning at the head node, and collect each node’s value in a string
            if current_node.get_value() != None:
              string_list += str(current_node.get_value()) + '\n' # using str() to convert integers to strings and adding "\n" between values so that each value prints on a new line
            current_node = current_node.get_next_node()
        return string_list # once the end of the list has been reached, the method should return the string
  
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node() # it's recommended to create a variable to keep track of the node we are currently looking at as we traverse the list
        if current_node.get_value() == value_to_remove: # check if list's head_node has a value equals to value_to remove
            self.head_node = current_node.get_next_node() # if it does, we’ve found the node we’re looking for and we need to adjust the list’s pointer to head_node. Remember that the list’s second node is the current head_node's next_node
        else:
            while current_node: # traversing the list, by checking if current_node exists (not None)
                next_node = current_node.get_next_node() # it's recommended to create a variable to keep track of current_node‘s next_node
                if next_node.get_value() == value_to_remove: # when value_to_remove is found...
                    current_node.set_next_node(next_node.get_next_node()) # adjusts the links in the list so that current_node is linked to next_node.get_next_node(). In other words, we can remove our next_node by setting our current node’s next_node property equal to the node that follows next_node
                    current_node = None # after you remove the node with a value of value_to_remove, make sure to set current_node to None so that you exit the loop
                else:
                    current_node = next_node

'''
Explanation of the .remove_node() method:
Consider a -> b -> c and we want to remove b_node.
In order to remove node_b, you must first next node_a to node_c (where node_b was nexting). Then you can remove node_b.
This method does this by updating the link within the a_node to match what b_node was pointing to prior to removing it from the linked list.
If a_node is the current_node, current_node.get_next_node() is b.
If b.get_value() == value_to_remove is True, you want to set a's next_node property to c.

So far you’ve built a method to remove the first occurrence of a given value. How do you think you would remove all nodes that have a specific value? Try building a method to do that!

It is not possible to traverse a linked list through its list property, which keeps track of each node in the list.
A linked list only keeps track of the first node in the list.To traverse the list, it needs a method that loops through each node to find the following node.
'''