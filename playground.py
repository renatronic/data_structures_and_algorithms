from node import Node
from linked_list import LinkedList
from swap_nodes import swap_nodes
from nth_last_node import nth_last_node

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

# .nth_last_node() playground
def generate_test_linked_list():
    linked_list = LinkedList()
    for i in range(50, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list

test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)