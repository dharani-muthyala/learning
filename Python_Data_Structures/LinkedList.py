# Define the SinglyLinkedListNode class
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Print Elements of a Linked List
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

# Insert a Node at the Tail of a Linked List
def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)

    if head is None:
        return new_node

    current = head
    while current.next is not None:
        current = current.next

    current.next = new_node

    return head      

# Insert a Node at the Head of a Linked List
def insertNodeAtHead(llist, data):
    new_node = SinglyLinkedListNode(data)
    new_node.next = llist
    return new_node

# Insert a Node at a Specific Position in a Linked List
def insertNodeAtPosition(llist, data, position):
    new_node = SinglyLinkedListNode(data)

    if position == 0:
        new_node.next = llist
        return new_node
    current = llist
    index = 0
    while index < position - 1:
        current = current.next
        index += 1
    new_node.next = current.next
    current.next = new_node
    return llist

# Delete a Node
def deleteNode(llist, position):
    if position == 0:
        return llist.next
    current = llist
    index = 0
    while index < position - 1:
        current = current.next
        index += 1
    current.next = current.next.next
    return llist

# Print in Reverse
def reversePrint(llist):
    values = []
    # Traverse the list
    current = llist
    while current:
        values.append(current.data)
        current = current.next
    # Print in reverse order
    for value in reversed(values):
        print(value)

# Reverse a Linked List
def reverse(llist):
    # Write your code here
    prev = None
    current = llist

    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev   

# Compare Two Linked Lists
def compare_lists(llist1, llist2):
    a = llist1
    b = llist2

    # Traverse both lists
    while a is not None and b is not None:
        # If data mismatch -> lists are not identical
        if a.data != b.data:
            return 0
        
        a = a.next
        b = b.next

    # If one list is longer than the other -> not identical
    if a is not None or b is not None:
        return 0

    return 1      