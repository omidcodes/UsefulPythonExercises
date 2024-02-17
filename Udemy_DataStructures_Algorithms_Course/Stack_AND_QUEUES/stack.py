class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self, value):
        node = Node(value=value)
        self.top = node
        self.height = 1

    def push(self, value):
        node = Node(value=value)
        if self.height != 0:
            node.next = self.top
        self.top = node
        self.height += 1

    def pop(self):

        if self.top is None:
            return None

        old_top = self.top
        self.top = self.top.next
        old_top.next = None
        self.height -= 1
        return old_top

    def print_list(self):
        node = self.top
        while node:
            print(str(node.value) + '-> ')
            node = node.next


stack = Stack(value=1)

stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
stack.pop()

stack.print_list()
