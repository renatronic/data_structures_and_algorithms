from node import Node
from linked_list import LinkedList
from swap_nodes import *
from nth_last_node import *

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
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 3)
print(nth_last.value)

# .swap_nodes() playground
ll = LinkedList()
for i in range(10):
  ll.insert_beginning(i)

print(ll.stringify_list())

swap_nodes(ll, 4, 5)

print(ll.stringify_list())
'''