# Add 1 to a number represented by LL

# Problem Statement: Given the head of a singly linked list representing a positive integer number. Each node of the linked list represents a digit of the number, with the 1st node containing the leftmost digit of the number and so on. The task is to add one to the value represented by the linked list and return the head of a linked list containing the final value.
# The number will contain no leading zeroes except when the value represented is zero itself.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ---------------- Create Linked List ----------------
def create_linked_list(arr):
    if not arr:
        return None

    head = Node(arr[0])
    temp = head

    for value in arr[1:]:
        temp.next = Node(value)
        temp = temp.next

    return head


# ---------------- Display Linked List ----------------
def print_linked_list(head):
    temp = head

    while temp:
        print(temp.data, end="")
        if temp.next:
            print(" -> ", end="")
        temp = temp.next

    print()

def reverse(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

def addOne(head):

    head = reverse(head)
    curr = head
    carry = 1

    while curr and carry:

        total = curr.data + carry

        curr.data = total % 10
        carry = total // 10

        if carry and curr.next == None:
            curr.next = Node(0)

        curr = curr.next

    head = reverse(head)
    return head

# ---------------- Driver Code ----------------

n = int(input("Enter number of digits: "))

arr = list(map(int, input("Enter digits: ").split()))

head = create_linked_list(arr)

print("\nOriginal Number:")
print_linked_list(head)

head = addOne(head)

print("\nAfter Adding One:")
print_linked_list(head)