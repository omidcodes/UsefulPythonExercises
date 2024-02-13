class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # WRITE SWAP_FIRST_LAST METHOD HERE #
    #                                   #
    #                                   #
    #                                   #
    #                                   #
    #####################################

    def swap_first_last(self):

        if self.length == 0 or self.length == 1:
            return

        if self.length == 2 :
            self.tail.prev = None
            self.tail.next = self.head

            self.head.prev = self.tail
            self.head.next = None
        else:
            # temporarily holds the variables
            after_head = self.head.next
            before_tail = self.tail.prev

            # Last -> First
            self.tail.prev = None
            self.tail.next = after_head
            after_head.prev = self.head

            # First -> Last
            self.head.next = None
            self.head.prev = before_tail
            before_tail.next = self.head

        # swap head<->tail in DoublyLinkedList
        temp = self.head
        self.head = self.tail
        self.tail = temp
    

# my_doubly_linked_list = DoublyLinkedList(1)
# my_doubly_linked_list.append(2)
# my_doubly_linked_list.append(3)
# my_doubly_linked_list.append(4)


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
# my_doubly_linked_list.append(3)
# my_doubly_linked_list.append(4)


print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.swap_first_last()


print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before swap_first_last():
    1
    2
    3
    4

    DLL after swap_first_last():
    4
    2
    3
    1

"""

