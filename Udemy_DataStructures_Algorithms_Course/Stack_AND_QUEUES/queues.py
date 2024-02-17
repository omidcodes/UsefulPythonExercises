class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self, value):
        node = Node(value=value)
        self.first = node
        self.last = node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value=value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def print_queue(self):
        node = self.first
        while node:
            print(str(node.value) + '-> ')
            node = node.next


my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.print_queue()
