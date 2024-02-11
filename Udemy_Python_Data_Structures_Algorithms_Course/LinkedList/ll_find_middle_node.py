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
        

    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    #                                    #
    #                                    #
    #                                    #
    #                                    #
    ######################################

    def find_middle_node(self):

        if self.head == self.tail:
            return self.head
        
        length : int = 0
        current_node = self.head

        while True:
            if current_node.next is None:
                break
            length+=1
            current_node = current_node.next

        current_node = self.head

        mid_index: int = int(length/2) if length%2==0 else int((length+1)/2)

        for _ in range(mid_index):
            current_node = current_node.next

        return current_node





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""