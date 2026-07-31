# Search an element in a Linked List

# Problem Statement: Given the head of a linked list and an integer value, find out whether the integer is present in the linked list or not. Return true if it is present, or else return false.

def search(head, target):
    temp = head

    while temp:
        if temp.data == target:
            return True
        temp = temp.next
    return False
