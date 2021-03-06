from node import Node
from linked_list import LinkedList

def swap_nodes(input_list, val1, val2):
    print(f'Swapping {val1} with {val2}.')

    # assigning four variables to track the nodes that'll need to change
    node1 = input_list.head_node
    node2 = input_list.head_node
    node1_prev = None
    node2_prev = None

    # prompt for one edge case: the two nodes to be swapped are the same
    if val1 == val2:
        print('Elements are the same; no swap needed.')
        return

    # finding the matching and preceding nodes
    while node1 is not None:
        if node1.get_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()
    
    while node2 is not None:
        if node2.get_value() == val2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()

    # prompt for another edge case: no matchig node for one of the inputs
    if (node1 is None or node2 is None):
        print('Swap not possible: one or more element(s) is not in the list.')
        return

    # updating the preceding nodes' pointers
    if node1_prev is None:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)
    
    if node2_prev is None:
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)
    
    # updating the nodes' next pointers
    temp = node1.get_next_node() # first we save node1 next node/pointer in a temporary variable, since we're gonna change it
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)


# playground

'''
word1 = Node('hate')
word2 = Node('pain')
word3 = Node('death')
word4 = Node('love')

print(word1.get_value())
'''

'''
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
ll = LinkedList()
for i in range(10):
  ll.insert_beginning(i)

#print(ll.stringify_list())

swap_nodes(ll, 3, 8)

print(ll.stringify_list())
'''