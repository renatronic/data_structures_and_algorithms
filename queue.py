from node import Node

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
    
    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Adding " + str(item_to_add.get_value()) + " to the queue!")
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add) # set item_to_add as the current tail‘s next node
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")
        
    def dequeue(self):
        if self.get_size() > 0: # checks if the queue is not empty. Another way to check could be "if not self.is_empty():"
            item_to_remove = self.head
            print(str(item_to_remove.get_value()) + " is served!")
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node() # sets the queue’s head equal to the following node using Node‘s handy dandy get_next_node() method
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The queue is totally empty!")
  
    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            print("No orders waiting!")
  
    def get_size(self):
        return self.size
    
    # .has_space() tells us if there is space for us to .enqueue() — or add — an additional value to the end of the queue.
    def has_space(self):
        if self.max_size:
            return self.max_size > self.get_size() # I was trying go write another if-else statement here
        else:
            return True
    
    def is_empty(self):
        return self.size == 0