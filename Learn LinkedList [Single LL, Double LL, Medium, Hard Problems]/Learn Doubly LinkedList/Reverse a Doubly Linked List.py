# Reverse a Doubly Linked List

# Problem Statement: Given a doubly linked list of size ‘N’ consisting of positive integers, your task is to reverse it and return the head of the modified doubly linked list.

def reverse_dll(head):
    if head is None:
        return None

    temp = head
    last = None

    while temp:
        temp.next, temp.prev = temp.prev, temp.next
        last = temp
        temp = temp.prev
    return last