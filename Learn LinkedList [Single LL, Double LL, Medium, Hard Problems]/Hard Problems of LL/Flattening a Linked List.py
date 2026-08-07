# Flattening a Linked List

# Problem Statement: Given a linked list containing ‘N’ head nodes where every node in the linked list contains two pointers:

# ‘Next’ points to the next node in the list
# ‘Child’ pointer to a linked list where the current node is the head

# Each of these child linked lists is in sorted order and connected by a 'child' pointer. Your task is to flatten this linked list such that all nodes appear in a single layer or level in a 'sorted order'.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None

def merge(a, b):

    if not a:
        return b
    if not b:
        return a

    if a.data <= b.data:
        a.child = merge(a.child, b)
        a.next = None
        return a

    else:
        b.child = merge(b.child, a)
        b.next = None
        return b

# ---------------- Flatten ----------------
def flatten(head):

    if not head or not head.next:
        return head

    head.next = flatten(head.next)
    head = merge(head, head.next)

    return head

# ---------------- Display Flattened List ----------------
def print_flattened(head):

    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.child

    print("None")


# ---------------- Driver Code ----------------

# Creating the multilevel linked list manually

head = Node(5)

head.next = Node(10)
head.next.next = Node(19)
head.next.next.next = Node(28)

# Child list of 5
head.child = Node(7)
head.child.child = Node(8)
head.child.child.child = Node(30)

# Child list of 10
head.next.child = Node(20)

# Child list of 19
head.next.next.child = Node(22)
head.next.next.child.child = Node(50)

# Child list of 28
head.next.next.next.child = Node(35)
head.next.next.next.child.child = Node(40)
head.next.next.next.child.child.child = Node(45)

print("Flattened Linked List:")

head = flatten(head)

print_flattened(head)