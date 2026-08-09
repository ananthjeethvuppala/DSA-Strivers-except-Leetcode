# Implement Queue using Linked List

# Problem Statement: Implement a First-In-First-Out (FIFO) queue using a singly linked list. The implemented queue should support the following operations: push, pop, peek, and isEmpty.

# Implement the LinkedListQueue class:

# void push(int x): Adds element x to the end of the queue.
# int pop(): Removes and returns the front element of the queue.
# int peek(): Returns the front element of the queue without removing it.
# boolean isEmpty(): Returns true if the queue is empty, false otherwise.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rare = None

    def push(self, val):
        new_node = Node(val)

        if self.front == None:
            self.front = new_node
            self.rare = new_node

        else:
            self.rare.next = new_node
            self.rare = new_node

    def pop(self):
        if self.front is None:
            return -1

        value = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rare = None

        return value

    def peek(self):
        if self.front is None:
            return -1
        else:
            return self.front.data

    def is_empty(self):
        return self.front is None

# Driver Code
queue = LinkedListQueue()

queue.push(3)
queue.push(7)

print("Peek:", queue.peek())
print("Pop:", queue.pop())
print("Is Empty:", queue.is_empty())