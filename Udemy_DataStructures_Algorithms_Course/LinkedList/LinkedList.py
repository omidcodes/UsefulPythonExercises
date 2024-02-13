from typing import Optional


class Node:
    
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self, value) -> None:
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self) -> None:

        # print(f"self.length = {self.length}")
        
        ptr = self.head

        if ptr is None:
            return

        while True:
            print(ptr.value)

            if ptr.next is None:
                break

            ptr = ptr.next

    def append(self , value):
        new_node = Node(value)

        if self.head is None:
            # If LinkedList is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def __find_one_before_the_last_node(self)->Node:
        
        before_iteration = None
        current_iteration = self.head

        while True:
            if current_iteration.next is None:
                break
            
            before_iteration = current_iteration
            current_iteration = current_iteration.next         

        return before_iteration
    

    def pop(self) -> Optional[Node]:
        if self.length == 0:
            return None
            # raise Exception("There is no item to pop")
        
        if self.length == 1:
            return_node = self.tail
            self.head = None
            self.tail = None

        else:
            one_before_the_last_node : Node = self.__find_one_before_the_last_node()
            one_before_the_last_node.next = None

            return_node = self.tail
            
            self.tail = one_before_the_last_node

        self.length -= 1

        return return_node

    def prepend(self, value):
        """ Add to the beginning of the LinkedList"""

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length +=1
        
    def pop_first(self) -> Optional[Node]:
        
        if self.length == 0:
            return None
            # raise Exception("There is no item to pop")
        elif self.length == 1:
            return_node = self.head
            self.head.next = None
            self.head = None
            self.tail = None
            
        else:
            return_node = self.head
            second_element = self.head.next
            self.head.next = None
            self.head = second_element

        self.length -=1
        return return_node

    def __is_index_out_of_bound(
        self,
        index,
        allow_index_equal_to_length:bool= False) -> bool:

        if allow_index_equal_to_length is True:
            is_out_of_bound = index < 0 or index > self.length
        else:
            is_out_of_bound = index < 0 or index > self.length -1 
        
        return bool(is_out_of_bound)

    def get(self, index) -> Optional[Node]:
        """ Indexes start from 0 """

        if self.__is_index_out_of_bound(index):
            return None
                
        current_node = self.head

        for _ in range(index):
            current_node = current_node.next

        return current_node
    
    def set_value(self, index, value) -> bool:

        node : Optional[Node] = self.get(index=index)

        if node is None:
            return False

        node.value = value
        return True

    def insert(self, index, value) -> bool:
        
        if self.__is_index_out_of_bound(index, allow_index_equal_to_length=True):
            return False

        if index == 0:
            self.prepend(value)
            return True

        if index == self.length:
            self.append(value)        # self.__validate_index(index=index)

        return True

    def remove(self, index) -> Optional[Node]:
        
        if self.__is_index_out_of_bound(index):
            return None
        
        if self.length == 0 :
            return None
        
        if index == 0:
            removed_node = self.pop_first()

        else:
            before_node : Node = self.get(index=index-1)
            current_node: Node = before_node.next
            after_node = current_node.next

            before_node.next = after_node

            removed_node = current_node

            # del current_node

            self.length -=1

        return removed_node

    def reverse(self):
        """ Reverse items """
        
        if self.length == 0 or self.length == 1:
            return

        # Swap head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp


        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
 

my_linked_list = LinkedList(4)

print("Appending some items ...")
my_linked_list.append(10)
my_linked_list.append(8)
my_linked_list.append(3)
my_linked_list.append(2)


print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


my_linked_list.print_list()

print("Popping The last item ...")
my_linked_list.pop()                                                                                     

my_linked_list.print_list()

print("Prepending The item ...")
my_linked_list.prepend(7)
my_linked_list.print_list()

print("Popping The First item ...")
my_linked_list.pop_first()
my_linked_list.print_list()

print("getting only the item With Index = `2`")
print(my_linked_list.get(2))

print("`set_value` The item ...")
my_linked_list.set_value(index=0, value=99)
my_linked_list.print_list()

print("`insert` The item ...")
my_linked_list.insert(index=3, value=40)
my_linked_list.print_list()


print("`Removing` The item ...")
my_linked_list.remove(index=3)
my_linked_list.print_list()

print("`Reversing` The items ...")
my_linked_list.reverse()
my_linked_list.print_list()