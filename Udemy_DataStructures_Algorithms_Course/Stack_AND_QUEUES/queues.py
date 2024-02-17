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

    def dequeue(self):
        if self.length == 0:
            return None

        temp = self.first

        if self.length == 1:
            self.first = None
            self.last = None

        else:
            self.first = self.first.next
            temp.next = None

        self.length -= 1
        return temp

    def print_queue(self):
        node = self.first
        while node:
            print(str(node.value) + '-> ')
            node = node.next


my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)

print(my_queue.dequeue().value)
print(my_queue.dequeue().value)
print(my_queue.dequeue().value)
print(my_queue.dequeue().value)
# (0) Items - Returns None
print(my_queue.dequeue())

"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    None

"""
