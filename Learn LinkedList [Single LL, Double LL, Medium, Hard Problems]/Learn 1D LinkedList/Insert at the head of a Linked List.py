# Insert at the head of a Linked List

# Problem Statement: Given a linked list and an integer value val, insert a new node with that value at the beginning (before the head) of the list and return the updated linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_head(head, val):
    new_node = Node(val)
    new_node.next = head
    head = new_node
    return head