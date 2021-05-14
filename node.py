class Node:
    def __init__(self, value, next_node=None): # next_node coud be also named link_node and it's optional
        self.value = value
        self.next_node = next_node
        
    def get_next_node(self): # access next
        return self.next_node
    
    def get_value(self): # access value
        return self.value
    
    def set_value(self, value):
        self.value = value

    def set_next_node(self, next_node):
        self.next_node = next_node
        
    def increment_value(self):
        self.value = self.value + 1

# tests
yacko = Node('likes to yak')
wacko = Node('has a penchant for hoarding snacks')
dot = Node('enjoys spending time in movie lots')

yacko.set_next_node(dot)
dot.set_next_node(wacko)

dots_data = yacko.get_next_node().get_value()
wackos_data = dot.get_next_node().get_value()
print(dots_data)
print(wackos_data)

test = yacko.get_next_node().get_next_node().get_value()
print(test)