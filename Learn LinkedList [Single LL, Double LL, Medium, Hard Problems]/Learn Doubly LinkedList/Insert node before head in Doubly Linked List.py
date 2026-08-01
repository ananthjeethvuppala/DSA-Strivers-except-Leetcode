# Insert at end of Doubly Linked List

# Problem Statement: Given a doubly linked list, and a value ‘k’, insert a node having value ‘k’ at the end of the doubly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insert_at_end(head, k):
    new_node = Node(k)

    if head is None:
        return new_node

    temp = head
    while temp:
        temp = temp.next

    new_node.prev = temp
    temp.next = new_node

    return head
