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