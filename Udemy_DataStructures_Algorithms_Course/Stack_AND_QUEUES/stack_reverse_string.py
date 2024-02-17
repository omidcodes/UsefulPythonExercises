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


## WRITE REVERSE_STRING FUNCTION HERE ###
#                                       #
#  This is a separate function that is  #
#  not a method within the Stack class. #
#  Indent all the way to the left.      #
#                                       #


def reverse_string(string):
    if string == "":
        return ""

    stack = Stack()

    for char in string:
        stack.push(char)

    reversed_string = ""

    for i in range(stack.size()):
        reversed_string += stack.pop()

    return reversed_string


my_string = 'hello'

print(reverse_string(my_string))

"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""
