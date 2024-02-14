class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def  __str__(self):
        return self.value


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):

        # TODO : Implement me
        raise NotImplementedError("Please implement me ..")

        # if self.length == 0 or self.length == 1:
        #     return
        #
        # number_of_iterations: int = self.length // 2
        #
        # before = None
        # temp = self.head
        # after = temp.next
        #
        # for i in range(number_of_iterations):
        #
        #     print(f" Before i = {i}")
        #     self.print_list()
        #
        #     # after = temp.next
        #
        #     after.prev = before
        #     if before:
        #         before.next = after
        #     else:
        #         self.head = after
        #
        #     # temp = before
        #
        #     before = temp
        #
        #     # if after.next is None:
        #     #     self.tail = before
        #
        #     temp.prev = after
        #
        #     temp = after
        #     # temp = temp.next
        #     after.next = temp
        #     after = temp.next
        #     print(f" After i = {i}")

    # WRITE SWAP_PAIRS METHOD HERE #
    #                              #
    #                              #
    #                              #
    #                              #
    ################################


my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs()

print('my_dll after swap_pairs:')
my_dll.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""
