from node import Node
from linked_list import LinkedList
from swap_nodes import swap_nodes
from finders import *
from queue import Queue
from stack import Stack
from hash_map import HashMap

'''
# Node playground
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
'''

'''
# LinkedList and .swap_nodes() playground
word1 = Node('hate')
word2 = Node('pain')
word3 = Node('death')
word4 = Node('love')

# print(word1.get_value())

human = LinkedList('life')
human.insert_beginning(word1.get_value())
human.insert_beginning(word2.get_value())
human.insert_beginning(word3.get_value())
human.insert_beginning(word4.get_value())
human.insert_beginning(word4.get_value())
human.insert_beginning(word4.get_value())
human.remove_node('love')
human.remove_node(word3.get_value())
print(human.stringify_list())
swap_nodes(human, 'hate', 'life')
print(human.stringify_list())
'''

'''
# .swap_nodes() playground 2
ll = LinkedList()
for i in range(10):
  ll.insert_beginning(i)

#print(ll.stringify_list())

swap_nodes(ll, 3, 8)

print(ll.stringify_list())
'''

'''
# .nth_last_node() playground
def generate_test_linked_list(length):
    linked_list = LinkedList()
    for i in range(length, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list

test_list = generate_test_linked_list(9)
print(test_list.stringify_list())
# nth_last = nth_last_node(test_list, 10)
# print(nth_last.value)

mid_nod = find_middle(test_list)
print(mid_nod.value)
'''

'''
# queue playground 1
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
# queue playground 2
sharks_in_the_shark_tank = Queue(5)

sharks_in_the_shark_tank.enqueue("Alex")
sharks_in_the_shark_tank.enqueue("Alisha")
sharks_in_the_shark_tank.dequeue()
sharks_in_the_shark_tank.enqueue("Kenny")
sharks_in_the_shark_tank.dequeue()
'''

'''
# stack playground
# Defining an empty pizza stack
pizza_stack = Stack(6)

# Adding pizzas as they are ready until we have 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
pizza_stack.pop()
'''

hash_map = HashMap(15)

hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')
hash_map.assign('gneiss', 'artifact') # replaces the old value with this new one

print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))