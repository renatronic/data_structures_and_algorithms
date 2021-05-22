from node import Node

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit
    
    def push(self, value):
        if self.has_space(): # checks if the size of the stack is greater than 0
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item # sets the stack instance’s top_item equal to the new item, adding it to the top of the stack
            self.size += 1
            print("Adding {} to the stack!".format(value))
        else:
            print("No room for {}!".format(value))

    def pop(self):
        if not self.is_empty(): # checks if the size of the stack is greater than 0
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Delivering " + item_to_remove.get_value())
            return item_to_remove.get_value()
        print("Nothing to remove here!")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Nothing to see here!")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0