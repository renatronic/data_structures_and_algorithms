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


# playground

'''
print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# ------------------------ #
# Uncomment the line below:
deli_line.enqueue("western omelet with home fries")
# ------------------------ #
print("------------\nOur first order will be " + deli_line.peek())
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
# ------------------------ #
# Uncomment the line below:
deli_line.dequeue()
# ------------------------ #
'''

'''
sharks_in_the_shark_tank = Queue(5)

sharks_in_the_shark_tank.enqueue("Alex")
sharks_in_the_shark_tank.enqueue("Alisha")
sharks_in_the_shark_tank.dequeue()
sharks_in_the_shark_tank.enqueue("Kenny")
sharks_in_the_shark_tank.dequeue()
'''