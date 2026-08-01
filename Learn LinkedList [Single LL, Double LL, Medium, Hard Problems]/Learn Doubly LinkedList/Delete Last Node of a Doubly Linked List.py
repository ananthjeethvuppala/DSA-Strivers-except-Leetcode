# Delete Last Node of a Doubly Linked List

# Problem Statement: Given a Doubly Linked List, delete the last node of the Doubly Linked List.

def delete_node(head):
    if head is None:
        return None

    if head.next is None:
        return None

    temp = head
    while temp:
        temp = temp.next

    prev_node = temp.prev
    prev_node.next = None

    return head