# Length of Loop in Linked List

# Problem Statement: Given the head of a linked list, determine the length of a loop present in the linked list. If there's no loop present, return 0.

def countNodesInLoops(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            count = 1
            current = slow.next

            while current != slow:
                count += 1
                current = current.next
                
            return count