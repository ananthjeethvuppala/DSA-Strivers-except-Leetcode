# Implement stack using linked list

# Problem Statement: Implement a Last-In-First-Out (LIFO) stack using a singly linked list. The implemented stack should support the following operations: push, pop, top, and isEmpty.

# Implement the LinkedListStack class:

# void push(int x): Pushes element x onto the stack.
# int pop(): Removes and returns the top element of the stack.
# int top(): Returns the top element of the stack without removing it.
# boolean isEmpty(): Returns true if the stack is empty, false otherwise.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def pop(self):
        if self.head == None:
            return -1
        value = self.head.data
        self.head = self.head.next
        return value

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def top(self):
        if self.head == None:
            return -1
        return self.head.data

    def is_empty(self):
        return self.head is None

stack = LinkedListStack()

stack.push(3)
stack.push(7)
stack.push(10)
stack.push(12)

print("Pop:", stack.pop())
print("Top:", stack.top())
print("Is Empty:", stack.is_empty())