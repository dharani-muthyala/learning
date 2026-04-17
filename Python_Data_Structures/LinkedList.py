# Define the SinglyLinkedListNode class
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Print Elements of a Linked List
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

# Merge two sorted linked lists
def mergeLists(head1, head2):
    # Dummy node to build the merged list
    dummy = SinglyLinkedListNode(0)
    tail = dummy
    a = head1
    b = head2
    # Merge while both lists have nodes
    while a is not None and b is not None:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        
        tail = tail.next

    # Attach remaining nodes
    if a is not None:
        tail.next = a
    else:
        tail.next = b

    # Return head of the merged list
    return dummy.next  

# Get Node Value
def getNode(llist, positionFromTail):
    fast = llist
    slow = llist

    # Move fast pointer positionFromTail steps ahead
    for _ in range(positionFromTail):
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    return slow.data

# Remove Duplicates from a Sorted Linked List
def removeDuplicates(llist):
    current = llist

    # Traverse the linked list
    while current is not None and current.next is not None:
        # If current node and next node have same value -> skip next node
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return llist

# cycle detection
def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return 1    # cycle found

    return 0            # no cycle

# Find the Merge Point of Two Lists
def findMergeNode(head1, head2):
    a = head1
    b = head2

    # Traverse until both pointers meet
    while a != b:
        # If you reach end of a list, switch to the head of the other list
        a = a.next if a is not None else head2
        b = b.next if b is not None else head1

    # The node where they meet is the merge point
    return a.data

# Insert a Node into a Sorted Doubly Linked List
class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def sortedInsert(llist, data):
    new_node = DoublyLinkedListNode(data)

    # Case 1: Empty list
    if llist is None:
        return new_node

    # Case 2: Insert at beginning
    if data <= llist.data:
        new_node.next = llist
        llist.prev = new_node
        return new_node

    current = llist

    # Traverse to find correct position
    while current.next is not None and current.next.data < data:
        current = current.next

    # Insert in middle or end
    new_node.next = current.next
    if current.next is not None:
        current.next.prev = new_node

    current.next = new_node
    new_node.prev = current

    return llist    

# Reverse a Doubly Linked List
def reverseDoublyLinkedList(llist):
    current = llist
    prev = None

    while current is not None:
        # Swap next and prev pointers
        next_node = current.next
        current.next = prev
        current.prev = next_node

        # Move prev and current one step forward
        prev = current
        current = next_node

    return prev  # New head of the reversed list

# Tree: preorder Traversal
def preOrder(root):
    if root is None:
        return
    
    print(root.info, end=' ')   # visit root
    preOrder(root.left)         # traverse left
    preOrder(root.right)        # traverse right

# Tree: postorder Traversal
def postOrder(root):
    if root is None:
        return
    
    postOrder(root.left)        # traverse left
    postOrder(root.right)       # traverse right
    print(root.info, end=' ')   # visit root