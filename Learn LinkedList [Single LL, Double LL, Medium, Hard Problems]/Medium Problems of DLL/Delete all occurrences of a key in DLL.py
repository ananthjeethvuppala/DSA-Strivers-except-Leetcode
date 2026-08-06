# Delete all occurrences of a key in DLL

# Problem Statement: Given the head of a doubly linked list and an integer target. Delete all nodes in the linked list with the value target and return the head of the modified linked list.

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

def deleteAllOccurances(head, target):

    curr = head

    while curr:

        next_node = curr.next

        if curr.data == target:

            if curr.prev == None:
                head = curr.next

                if head:
                    head.prev = None

            else:
                curr.prev.next = curr.next

            if curr.next:
                curr.next.prev = curr.prev

        curr = next_node

    return head

# ---------------- Driver Code ----------------

n = int(input("Enter number of nodes: "))

arr = list(map(int, input("Enter elements: ").split()))

target = int(input("Enter value to delete: "))

head = create_dll(arr)

print("\nOriginal Doubly Linked List:")
print_dll(head)

head = deleteAllOccurances(head, target)

print("\nAfter Deleting All Occurrences:")
print_dll(head)