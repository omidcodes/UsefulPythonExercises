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

    def print_values(self) -> None:

        print(f"self.length = {self.length}")
        
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

    def pop(self):
        if self.length == 0:
            raise Exception("There is no item to pop")
        
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return

        one_before_the_last_node = self.__find_one_before_the_last_node()
        one_before_the_last_node.next = None
        self.tail = one_before_the_last_node

        self.length -= 1

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
        
    def pop_first(self):
        
        if self.length == 0:
            raise Exception("There is no item to pop")
        elif self.length == 1:
            self.head.next = None
            self.head = None
        else:
            second_element = self.head.next
            self.head.next = None
            self.head = second_element

        self.length -=1

    def __validate_index(self, index) -> None:
        if index < 0 or index > self.length - 1 :
            raise IndexError("Index is out of range")

    def __get_node_by_index(self, index: int) -> Node:
        self.__validate_index(index=index)
        
        current_one = self.head

        for _ in range(index):
            current_one = current_one.next

        return current_one

    def get(self, index):
        """ Indexes start from 0 """

        node : Node = self.__get_node_by_index(index=index)

        return node.value
    
    def set_value(self, index, value):

        node : Node = self.__get_node_by_index(index=index)

        node.value = value

    def insert(self, index, value):
        
        self.__validate_index(index=index)


        if index == 0:
            self.prepend(value)
            return

        if index == self.length:
            self.append(value)
            return

        
        node_before : Node = self.__get_node_by_index(index=index-1)
        node_current : Node = node_before.next


        new_node = Node(value)

        node_before.next = new_node

        new_node.next = node_current

        self.length +=1

    def remove(self, index):
        
        self.__validate_index(index)
        
        if self.length == 0 :   # TODO : Check. It may not be necessary
            raise IndexError("Invalid Index")
        
        if index == 0:
            self.pop_first()

        else:
            before_node : Node = self.__get_node_by_index(index=index-1)
            current_node: Node = before_node.next
            after_node = current_node.next

            before_node.next = after_node
            del current_node

        self.length -=1

    def reverse_items(self):
        
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


my_linked_list.print_values()

print("Popping The last item ...")
my_linked_list.pop()                                                                                     

my_linked_list.print_values()

print("Prepending The item ...")
my_linked_list.prepend(7)
my_linked_list.print_values()

print("Popping The First item ...")
my_linked_list.pop_first()
my_linked_list.print_values()

print("getting only the item With Index = `2`")
print(my_linked_list.get(2))

print("`set_value` The item ...")
my_linked_list.set_value(index=0, value=99)
my_linked_list.print_values()

print("`insert` The item ...")
my_linked_list.insert(index=3, value=40)
my_linked_list.print_values()


print("`Removing` The item ...")
my_linked_list.remove(index=3)
my_linked_list.print_values()

print("`Reversing` The items ...")
my_linked_list.reverse_items()
my_linked_list.print_values()