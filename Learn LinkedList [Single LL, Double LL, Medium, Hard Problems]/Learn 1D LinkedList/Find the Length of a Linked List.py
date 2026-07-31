# Find the Length of a Linked List

# Problem Statement: Given the head of a linked list, print the length of the linked list.

def length(head):
    temp = head
    count = 0

    while temp:
        count += 1
        temp = temp.next
    return count