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