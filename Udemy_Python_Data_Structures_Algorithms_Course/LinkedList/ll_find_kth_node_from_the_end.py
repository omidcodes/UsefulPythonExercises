class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
  
        
#### WRITE FIND_KTH_FROM_END FUNCTION HERE ####
#                                             #
#    This is a separate function that is      #
#    not a method within the                  #
#    LinkedList class.                        #
#    INDENT ALL THE WAY TO THE LEFT.          #
#                                             #
###############################################

def find_kth_from_end(linked_list, k:int):

    length : int = 0

    node = linked_list.head

    while True:
        length+=1
        if node.next is None:
            break
        node = node.next


    if k > length or k <= 0:
        # invalid index
        return None
    
    node = linked_list.head

    for _ in range(length-k):
        node = node.next

    return node





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

