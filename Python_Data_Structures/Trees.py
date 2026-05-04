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

# Tree: inorder Traversal
def inOrder(root):
    if root is None:
        return
    
    inOrder(root.left)         # traverse left
    print(root.info, end=' ')   # visit root
    inOrder(root.right)        # traverse right

# Tree: Height of a Binary Tree
def height(root):
    if root is None:
        return -1
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    
    return max(leftHeight, rightHeight) + 1

# Tree: Top View of a Binary Tree
from collections import deque
from xml.dom import Node

def topView(root):
    if root is None:
        return

    q = deque()
    q.append((root, 0))

    hd_map = {}

    while q:
        node, hd = q.popleft()

        if hd not in hd_map:
            hd_map[hd] = node.info

        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))

    for hd in sorted(hd_map):
        print(hd_map[hd], end=' ')

# Tree: Level Order Traversal
def levelOrder(root):
    if root is None:
        return

    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        print(node.info, end=' ')

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

# Binary Search Tree: Insertion
def insert(self, val):   
        new_node = Node(val)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if val < current.info:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    break

            elif val > current.info:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    break
            else:
                break


# Tree: Huffman Decoding
def decodeHuff(root, s):
    result = ""
    current = root

    for bit in s:
        # Move left or right based on bit
        if bit == '0':
            current = current.left
        else:
            current = current.right

        # If it's a leaf node
        if current.left is None and current.right is None:
            result += current.data
            current = root   # reset to root for next character

    print(result)

# Tree: Binary Search Tree: Lowest Common Ancestor
def lca(root, v1, v2):
    current = root

    while current:
        # both values are smaller -> go left
        if v1 < current.info and v2 < current.info:
            current = current.left

        # both values are greater -> go right
        elif v1 > current.info and v2 > current.info:
            current = current.right

        # split happens here -> this is LCA
        else:
            return current