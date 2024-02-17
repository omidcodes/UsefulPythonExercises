class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


##### WRITE SORT_STACK FUNCTION HERE #####
#                                        #
#  This is a separate function that is   #
#  not a method within the Stack class.  #
#                                        #
#  <- INDENT ALL THE WAY TO THE LEFT <-  #
#                                        #
##########################################

def sort_stack(stack: Stack):

    # TODO : Implement me .
    raise NotImplementedError("Please implement me ...")
    # stack_size = stack.size()
    # if stack_size == 0 or stack_size == 1:
    #     return stack
    #
    # sorted_stack = Stack()
    #
    # biggest_number = 0
    #
    # for i in range(stack_size):
    #
    #     for j in range(i):
    #         value = stack.pop()
    #         sorted_stack.push(value)
    #         if value > biggest_number:
    #             biggest_number = value
    #
    #     for j in range(i):
    #         value = sorted_stack.pop()
    #         if value != biggest_number:
    #             stack.push(value)
    #         else:
    #             continue
    #
    #     stack.push(value=biggest_number)
    #
    #     print("stack = ")
    #     stack.print_stack()
    #
    #     print("sorted_stack = ")
    #     sorted_stack.print_stack()

my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()

"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""
