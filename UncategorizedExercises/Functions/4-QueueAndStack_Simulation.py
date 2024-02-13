# Queue ==> FIFO
def QueueSimulation():
    queue = []

    # Adding elements to the queue
    queue.append('a')
    queue.append('b')
    queue.append('c')

    print("Initial queue")
    print(queue)

    # Removing elements from the queue
    print("\nElements dequeued from queue")
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))

    print("\nQueue after removing elements")
    print(queue)

    print('*'*200)


# Stack ==> FILO
def StackSimulation():
    stack = []

    # append() function to push
    # element in the stack
    stack.append('a')
    stack.append('b')
    stack.append('c')

    print('Initial stack')
    print(stack)

    # pop() fucntion to pop
    # element from stack in
    # LIFO order
    print('\nElements poped from stack:')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    print('\nStack after elements are poped:')
    print(stack)



if __name__ == '__main__':
    QueueSimulation()

    StackSimulation()