# Sort a Linked List of 0's 1's and 2's by changing links

# Problem Statement: Given a linked list containing only 0's, 1's, and 2's, sort the linked list by rearranging the links (not by changing the data values).


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(arr):
    if not arr:
        return None

    head = Node(arr[0])
    temp = head

    for value in arr[1:]:
        temp.next = Node(value)
        temp = temp.next

    return head


def print_linked_list(head):
    temp = head

    while temp:
        print(temp.data, end=" -> " if temp.next else "")
        temp = temp.next

    print()

def segregate(head):

    if not head or not head.next:
        return head

    zero_dummy = Node(-1)
    one_dummy = Node(-1)
    two_dummy = Node(-1)

    zero_tail = zero_dummy
    one_tail = one_dummy
    two_tail = two_dummy

    curr = head

    while curr:
        next_node = curr.next
        curr.next = None

        if curr.data == 0:
            zero_tail.next = curr
            zero_tail = zero_tail.next

        elif curr.data == 1:
            one_tail.next = curr
            one_tail = one_tail.next

        else:
            two_tail.next = curr
            two_tail = two_tail.next

        curr = next_node

    if one_dummy.next:
        zero_tail.next = one_dummy.next

    else:
        zero_tail.next = two_dummy.next

    one_tail.next = two_dummy.next

    if zero_dummy.next:
        return zero_dummy.next
    elif one_dummy.next:
        return one_dummy.next
    else:
        return two_dummy.next


# ---------------- Driver Code ----------------

n = int(input("Enter number of nodes: "))

arr = list(map(int, input("Enter elements (0,1,2): ").split()))

head = create_linked_list(arr)

print("\nOriginal Linked List:")
print_linked_list(head)

head = segregate(head)

print("\nSorted Linked List:")
print_linked_list(head) 