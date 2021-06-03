'''
This hash map implementation uses separate chaining to deal with 
collisions, by implementing a linked list data structure for each 
separate chaining.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node
    
    def insert(self, new_node):
        current_node = self.head_node

        if not current_node:
            self.head_node = new_node

        while(current_node):
            next_node = current_node.get_next_node()
            if not next_node:
                current_node.set_next_node(new_node)
            current_node = next_node

    def __iter__(self):
        current_node = self.head_node
        while(current_node):
            yield current_node.get_value()
            current_node = current_node.get_next_node()


class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [LinkedList() for item in range(array_size)] # instead of creating a list of None objects, we create a list of linked lists
    
    def hash(self, key):
        hash_code = sum(key.encode())
        return hash_code

    def compressor(self, hash_code):
        return hash_code % self.array_size
    
    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        # self.array[array_index] = [key, value]
        payload = Node([key, value])
        list_at_array = self.array[array_index] # list_at_array should be the LinkedList object instantiated at that location in self.array

        for item in list_at_array:
            if item[0] == key:
                item[1] = value
                return # this statement is useful so we don't end up assingn the value above AND adding the new node with the next line. In other words, if we return the value, we won't end up inserting the another node
        
        list_at_array.insert(payload) # if we’ve iterated through the list and not found our key, we need to add it

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        # payload = self.array[array_index] # the variable payload used to store the key/value pair at an array index. Now that the location is a linked list we change the name from payload to list_at_index
        list_at_index = self.array[array_index]

        for item in list_at_index:
            if item[0] == key:
                return item[1]
        
        return None # this line only returns None if the if statement doesn't return any value


# playground

'''
flower_definitions = [['begonia', 'cautiousness'], ['chrysanthemum', 
'cheerfulness'], ['carnation', 'memories'], ['daisy', 'innocence'], 
['hyacinth', 'playfulness'], ['lavender', 'devotion'], 
['magnolia', 'dignity'], ['morning glory', 'unrequited love'], 
['periwinkle', 'new friendship'], ['poppy', 'rest'], 
['rose', 'love'], ['snapdragon', 'grace'], ['sunflower', 'longevity'], 
['wisteria', 'good luck']]

blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))
print(blossom.retrieve('begonia'))
blossom.assign('iza', 'histerism')
print(blossom.retrieve('iza'))
'''