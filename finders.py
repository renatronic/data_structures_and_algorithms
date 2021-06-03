from node import Node
from linked_list import LinkedList

'''
The grace of the both solutions is that both have O(n) time complexity, 
and O(1) space complexity. We always use two variables to represent two 
pointers no matter what size the linked list is).
'''

# returns the nth to last element
def nth_last_node(linked_list, n):
    current = None
    tail_seeker = linked_list.head_node
    count = 0

    while tail_seeker:
        tail_seeker = tail_seeker.get_next_node()
        count += 1

        if count >= n + 1:
            
            if current is None:
                current = linked_list.head_node
            else:
                current = current.get_next_node()

    return current

# returns the middle node of a linked list
def find_middle(linked_list):
    fast_pointer = linked_list.head_node
    slow_pointer = linked_list.head_node
    
    while fast_pointer:

        fast_pointer = fast_pointer.get_next_node()
        
        if fast_pointer:
            fast_pointer = fast_pointer.get_next_node()
            slow_pointer = slow_pointer.get_next_node()

    return slow_pointer

'''
Half Speed
Another equally valid solution is to move the fast pointer once with 
each loop iteration but only move the slow pointer every-other 
iteration.
'''

def find_middle_alt(linked_list):
    count = 0
    fast = linked_list.head_node
    slow = linked_list.head_node
    
    while fast:

        fast = fast.get_next_node()

        if count % 2 != 0:
            slow = slow.get_next_node()
        count += 1

    return slow

'''
ERRORS
.nth_last_node RETURNS THE WRONG ELEMENT WHEN I START TO COUNT ON 1
.find_middle() and .find_middle_alt RETURNS ONE MORE THEN THE MIDDLE
'''


# playground

'''
def generate_test_linked_list(length):
    linked_list = LinkedList()
    for i in range(length, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list

test_list = generate_test_linked_list(9)
# print(test_list.stringify_list())
# nth_last = nth_last_node(test_list, 10)
# print(nth_last.value)

mid_nod = find_middle(test_list)
print(mid_nod.value)
'''