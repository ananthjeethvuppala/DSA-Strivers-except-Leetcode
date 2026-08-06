# Remove duplicates from sorted DLL

# Problem Statement: Given the head of a doubly linked list with its values sorted in non-decreasing order. Remove all duplicate occurrences of any value in the list so that only distinct values are present in the list.
# Return the head of the modified linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# ---------------- Create Doubly Linked List ----------------
def create_dll(arr):
    if not arr:
        return None

    head = Node(arr[0])
    temp = head

    for value in arr[1:]:
        new_node = Node(value)
        temp.next = new_node
        new_node.prev = temp
        temp = new_node

    return head


# ---------------- Display Doubly Linked List ----------------
def print_dll(head):
    temp = head

    while temp:
        print(temp.data, end="")
        if temp.next:
            print(" <-> ", end="")
        temp = temp.next

    print()

def remove_duplicates(head):
    if not head:
        return head

    curr = head
    while curr and curr.next:

        if curr.data == curr.next.data:

            duplicate = curr.next
            curr.next = duplicate.next

            if duplicate.next:

                duplicate.next.prev = curr

        else:
            curr = curr.next
    return head

# ---------------- Driver Code ----------------

n = int(input("Enter number of nodes: "))

arr = list(map(int, input("Enter sorted elements: ").split()))

head = create_dll(arr)

print("\nOriginal Doubly Linked List:")
print_dll(head)

head = remove_duplicates(head)

print("\nAfter Removing Duplicates:")
print_dll(head)